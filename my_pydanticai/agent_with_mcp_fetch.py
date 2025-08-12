from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

import logfire
from dotenv import load_dotenv
import os

load_dotenv()
logfire.configure(token=os.getenv('LOGFIRE_TOKEN'))

fetch_server = MCPServerStdio('python', ["-m", "mcp_server_fetch"])

agent = Agent('anthropic:claude-3-5-sonnet-latest',
                instrument=True,
                mcp_servers=[fetch_server])


async def main():
    async with agent.run_mcp_servers():
        result = await agent.run("hello!")
        while True:
            print(f"\n{result.data}")
            user_input = input("\n> ")
            result = await agent.run(user_input,
                                     message_history=result.new_messages())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())