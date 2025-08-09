import os
import chainlit as cl
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner

load_dotenv()

# Set up the Gemini client (Gemini is OpenAI-compatible when using v1beta/openai/)
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

@cl.on_message
async def main(message: cl.Message):
    agent = Agent(
        name="TravelGenie",
        instructions="""
You are TravelGenie 🌍✈️ — a professional travel planner assistant.

Your job is to help users plan exciting, affordable, and practical travel experiences.
When a user mentions a destination or asks for a travel plan, reply with:

1. ✈️ Flight suggestions (mock data is fine)
2. 🏨 Top hotels and why they're great
3. 🍽️ Best places to eat local food
4. 📍 Must-see attractions and hidden gems
5. 💡 Budget tips if the user mentions affordability
6. 📅 Create a sample 3-day or 5-day itinerary if possible

Make it engaging, useful, and tailored to the user input. Be concise but helpful. Always use emoji where appropriate.
""",
        model=OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",
            openai_client=client
        ),
    )

    result = await Runner.run(agent, message.content)
    await cl.Message(content=result.final_output).send()
