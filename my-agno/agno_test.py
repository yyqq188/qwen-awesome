import os
from dotenv import load_dotenv
load_dotenv()


from agno.agent import Agent
from agno.models.openai import OpenAIChat
# Qwen 的 OpenAI 兼容 API 仅接受标准角色：['system', 'assistant', 'user', 'tool', 'function']
qwen_role_map = {
    "system": "system",  # Keep as system, don't map to developer
    "user": "user",
    "assistant": "assistant",
    "tool": "tool",
    "model": "assistant",
}

agent = Agent(
    model=OpenAIChat(
        id="qwen-plus",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
        role_map=qwen_role_map,
    ),
    instructions="You are a helpful assistant",
)

agent.print_response("你是谁")
