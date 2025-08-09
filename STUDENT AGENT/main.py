import os 
from dotenv import load_dotenv

from openai import AsyncOpenAI
import chainlit as cl
from agents import Agent, Runner, OpenAIChatCompletionsModel


load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key = GEMINI_KEY,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

def productive_tip():
    return(
        "🧠*Learning Tip of the Day:*\n"
        "Try the *Pomodoro Technique* - 25 minuter focused study followed by a 5-minute break. It helps fight burnout and keeps you fresh!"
    )

def generate_summary(content:str)->str:
    content = content.strip()
    if len(content) < 40:
        return "⚠️ Please input a longer paragraph to summarize effectively."

    return f"📘 Summart Preview:\n{content[:80]}..."

@cl.on_chat_start
async def on_chat_start():
    await cl.Message("""🎓 Welcome! I'm your **Smart Student Agent Assistant**.\n Let's boost your knowledge together!""").send()


@cl.on_message
async def process_user_input(message:cl.Message):
    input_text = message.content.strip().lower()

    try:
        if input_text in {"hi","hello","start"}:
            await cl.Message(
                "👋 Hey there! Here's how I can help:\n"
                "- Type 'idea' for a learning strategy.\n"
                "- Use 'summarize: your text...' to get a brief summary.\n"
                "- Or just ask me a question – academic or motivational!"
            ).send()

        elif input_text.startswith("summarize:"):
            text_to_summarize = message.content.split("summarize:", 1)[1].strip()
            await cl.Message(generate_summary(text_to_summarize)).send()

        elif "idea" in input_text:
            await cl.Message(productive_tip()).send()

        else:
            response = await client.chat.completions.create(
                model = "gemini-2.0-flash",
                messages = [
                    {"role": "system","content":"you are a friendly AI tutor assisting student with knowledge, summaries , and motivation."},
                    {"role":"user","content": message.content}
                ],
                max_tokens = 400
            )
            await cl.Message(response.choices[0].message.content).send()

    except Exception as error:
        await cl.Message(f"🚨 Oops! something went wrong:\n{str(error)}").send()

