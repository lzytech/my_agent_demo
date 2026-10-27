import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
client=OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
# for t in [0,0.3,0.6,0.9,1.2,1.5,1.8,2]:
completion=client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            # {
            #     'role':'system',
            #     'content':'回复内容不少于十个字'
            # },
            {
            "role":"user",
            "content":"你是谁？"
             }
            ],
    temperature=0.9,
    stream=True
)
# print(completion.choices[0].message.content)
# print('......')
for chunk in completion :
    print(chunk.choices[0].delta.content,end='|')