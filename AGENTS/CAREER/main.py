# main.py
import os
import chainlit as cl
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Load environment variables
load_dotenv()

# Create Async client using Gemini-compatible base URL
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Define a minimal Agent class
class OpenAIChatCompletionsModel:
    def __init__(self, model: str, openai_client: AsyncOpenAI):
        self.model = model
        self.client = openai_client

    async def run(self, messages):
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return response.choices[0].message.content

class Agent:
    def __init__(self, name: str, instructions: str, model: OpenAIChatCompletionsModel):
        self.name = name
        self.instructions = instructions
        self.model = model

    async def chat(self, user_input: str):
        messages = [
            {"role": "system", "content": self.instructions},
            {"role": "user", "content": user_input}
        ]
        return await self.model.run(messages)

class Runner:
    @staticmethod
    async def run(agent: Agent, user_input: str):
        response = await agent.chat(user_input)
        return type("Result", (), {"final_output": response})()  # Simple wrapper

# Chainlit entrypoint
@cl.on_message
async def main(message: cl.Message):
    # Send "Thinking..." indicator
    thinking_msg = cl.Message(content="🤔 Thinking...")
    await thinking_msg.send()

    # Create agent and run
    agent = Agent(
        name="Gemini Assistant",
        instructions="You are a helpful assistant that only talks about careers, education, and skill building.",
        model=OpenAIChatCompletionsModel(
            model="gemini-1.5-flash",  # or gemini-1.5-pro if accessible
            openai_client=client
        )
    )
    result = await Runner.run(agent, message.content)

    # Update message with actual response
    await thinking_msg.update(content=result.final_output)