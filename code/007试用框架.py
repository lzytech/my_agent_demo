from agents import Agent,Runner
import local_settings
agent=Agent(
    name='AI助手',
    instructions='你是一个友好的AI助手,使用中文进行问答'
)
result=Runner.run_sync(agent,input='你是谁？')
print(result.final_output)