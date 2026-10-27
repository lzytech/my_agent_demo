#tokenizer+context_summary+sliding_window
from deepseek_tokenizer import ds_token
from dotenv import load_dotenv
import openai
import os
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
client=openai.OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
# 定义函数：接收一个对话列表 message_history
def tokens_by_messages(message_history: list):
    tokens = 0   # 初始化token总数，从0开始累加
    # 循环：遍历对话历史里每一条消息（system/user/assistant消息）
    for msg in message_history:
        # 取出这条消息里面的文字内容 content
        text = msg['content']
        # 把文字编码成token id列表，取长度，加到总数上
        tokens += len(ds_token.encode(text))
    # 循环结束，返回全部消息的总token数量
    return tokens
#print(tokens_by_messages(message_history))

# ========== 图片里的【摘要函数】，修好bug，复制进来 ==========
def context_summary(message_list):
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "user", "content": f"请对以下对话内容进行总结：{message_list}"}
        ],
    )
    summary_text = response.choices[0].message.content
    # 返回总结，作为一条system消息
    return [{"role": "system", "content": f"此前对话内容的总结：{summary_text}"}]

def context_sliding_window(message_list: list, k=1):
    # message_list：完整的对话列表；k默认保留最近2轮对话
    new_message_list: list = message_list[-2*k:]
    # 切片 [-2*k:] 👉 取列表【最后 2*k 条消息】
    # 一轮对话 = user + assistant，所以一轮是2条，k轮就是2*k条
    # 先在全部历史里，搜索system消息
    system_msg = None
    for msg in message_list:
        if msg['role'] == "system":
            system_msg = msg
            break   # 找到第一个system就停下
    if new_message_list[0]['role'] != "system":
        if system_msg is not None:
            new_message_list.insert(0, system_msg)

    return new_message_list
# =========下面是使用示例=========
# 用来存放对话历史的列表
message_history = []

# 系统提示词，给AI设定规则、身份、行为逻辑
system_prompt = """
你运行在一个思考、行动、观察和回答的循环，在循环结束时，你输出最终的答案。
用"思考"来描述你对被问问题的想法，
用"操作"运行你可用的操作之一，
"观察"将是运行这些操作的结果。
"答案"将是分析观察结果的结果。
"""
# 把系统提示词，加到对话历史里，角色是 system
message_history.append({"role": "system", "content": system_prompt})

# 用户的提问
query = "比赛场上，篮球队的球员人数乘以排球队的球员人数，结果是多少"
# 把用户提问，加到对话历史里，角色是 user
message_history.append({"role": "user", "content": query})
message_history.append({"role": "user", "content": query})
message_history.append({"role": "user", "content": "1+1=?"})
message_history.append({"role": "user", "content": "再加1呢？"})

print(context_summary(message_history))

