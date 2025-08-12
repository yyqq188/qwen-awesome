from agno.agent import Agent
from agno.models.qwen import Qwen  # Custom Qwen class

agent = Agent(
    model=Qwen(
        api_key="your-qwen-api-key",
        # No need for manual role_map - OpenAILike handles it correctly
    ),
    instructions="You are a helpful assistant.",
)