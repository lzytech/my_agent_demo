import os
from openai import OpenAI
os.environ['OPENAI_BASE_URL']="https://api.deepseek.com"
os.environ['OPENAI_API_KEY']="sk-53a9be44d63840b3a3b359b4dab03864"
client=OpenAI()
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