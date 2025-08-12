from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
import os
from dotenv import load_dotenv
load_dotenv()
model = OpenAIModel(model_name="qwen-plus",provider=OpenAIProvider(api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",))
agent = Agent(model)
"""

"""

async def main():
    result = await agent.run("hello!")
    while True:
        print(f"\n{result}")
        user_input = input("\n> ")
        result = await agent.run(user_input,
                                 message_history=result.new_messages(),
                                 )


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
