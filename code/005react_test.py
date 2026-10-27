import openai
import json
import os

client=openai.OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)#在终端运行$env:DEEPSEEK_API_KEY="sk-xxxx你的key"


def get_ballgame(game_name:str):
    data=[
        {
            'name':'篮球(Basketball)',
            'description':'两支球队通过投篮得分，比赛分为四节，每节时间因联赛而异。',
            'team_members':12,
            'players_on_field':5
        },
        {
            "name": "排球 (Volleyball)",
            "description": "两队隔网对抗，通过击球过网并使其落在对方场地得分。",
            "team_members": 12,
            "players_on_field": 6 
        },
        {
            "name": "沙滩排球 (Beach Volleyball)",
            "description": "排球的变种，在沙地上进行，每队人数较少。",
            "team_members": 2,
            "players_on_field": 2
        },
        {
            "name": "网球 (Tennis)",
            "description": "单打或双打比赛，球员用球拍击球过网，使对手无法回击。",
            "team_members": 1,
            "players_on_field": 1
        },
        {
            "name": "棒球 (Baseball)",
            "description": "进攻方击球后跑垒得分，防守方投球并试图使击球手出局。",
            "team_members": 9,
            "players_on_field": 9
        },
        {
            "name": "冰球 (Ice Hockey)",
            "description": "在冰面上进行，球员用球棍击打冰球进入对方球门。",
            "team_members": 20,
            "players_on_field": 6
        },
        {
            "name": "乒乓球 (Table Tennis)",
            "description": "两名或四名球员在球桌上用球拍击打小球。",
            "team_members": 1,
            "players_on_field": 1
        },
        {
            "name": "羽毛球 (Badminton)",
            "description": "球员用球拍击打羽毛球过网，使对手无法回击。",
            "team_members": 1,
            "players_on_field": 1
        }
    ]
    ret=[]
    for d in data:
        if game_name.lower() in d['name'].lower():
            ret.append(d)
    return ret

tools=[
    {
        'type':'function',
        'function':{
            'name':'get_ballgame',
            'description':'获取球类比赛的基本信息和人数规模',
            'parameters':{
                'type':'object',
                'properties':{
                    'game_name':{'type':'string'},
                },
                'required':['game_name'],
                'additionalProperties':False
            },
            'strict':True
        }
    }
]

system_prompt = """
你运行在一个思考、行动、观察和回答的循环，在循环结束时，你输出最终的答案。
用“思考”来描述你对被问问题的想法。
用“操作”运行您可用的操作之一。
“观察”将是运行这些操作的结果。
“答案”将是分析观察结果的结果。
"""
message_history = [{"role": "system", "content": system_prompt}]


def get_completion():
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=message_history,
        tools=tools,
    )
    return response.choices[0].message


def agent(query):
    max_turns = 5
    current_turns = 1
    message_history.append({"role": "user", "content": query})

    while current_turns <= max_turns:
        msg = get_completion()
        # 把assistant消息放进对话历史
        message_history.append(msg)
        print("模型输出content：", msg.content)

        if msg.tool_calls:
            # ✅ 重点修复：循环处理全部tool_calls，一个一个执行、一个一个追加tool消息
            for tool_call in msg.tool_calls:
                func_name = tool_call.function.name
                func_args = json.loads(tool_call.function.arguments)
                if func_name == "get_ballgame":
                    res = get_ballgame(**func_args)
                else:
                    res = f"函数 {func_name} 不存在"
                print(f"观察: {res}")
                # 每个tool_call单独追加一条tool消息，一一对应id
                message_history.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(res, ensure_ascii=False)
                })
            current_turns +=1
        else:
            # 没有工具调用，结束循环
            print("✅最终回答：", msg.content)
            break


if __name__ == '__main__':
    query = '比赛场上，篮球队的球员人数乘以排球队的球员人数，结果是多少'
    agent(query)
