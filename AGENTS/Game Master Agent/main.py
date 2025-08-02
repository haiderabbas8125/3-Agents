# main.py
import chainlit as cl
import random
import google.generativeai as genai
from dotenv import load_dotenv
import os

# 🔐 Load Gemini API key from .env
load_dotenv()
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
    )

# 🎲 Dice Tool
def roll_dice(sides=6):
    return random.randint(1, sides)

# ✨ Event Generator Tool
def generate_event(event_type="item"):
    prompt = f"Generate a short fantasy {event_type} with magical properties."
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text.strip() if response.text else "a mysterious relic"

# 🧙 Agents
class NarratorAgent:
    def respond(self, message, context):
        return f"The journey continues... {message}\nWhat do you do next?"

class MonsterAgent:
    def respond(self, message, context):
        damage = roll_dice(8)
        context["health"] -= damage
        return f"⚔️ A monster appears and strikes you for {damage} damage!\n❤️ Your current health: {context['health']} HP\nWill you fight back or run?"

class ItemAgent:
    def respond(self, message, context):
        item = generate_event("item")
        context["inventory"].append(item)
        return f"🎁 You discovered: **{item}**. It’s added to your inventory."

# 🔁 Agent Handoff Logic
def get_active_agent(message):
    msg = message.lower()
    if any(word in msg for word in ["fight", "attack", "monster", "battle"]):
        return MonsterAgent()
    elif any(word in msg for word in ["item", "inventory", "check inventory", "bag", "my stuff"]):
        return ItemAgent()
    else:
        return NarratorAgent()

# 🚀 Start Game
@cl.on_chat_start
async def start():
    cl.user_session.set("context", {
        "inventory": [],
        "health": 100
    })
    await cl.Message("🧙 Welcome to the *Fantasy Adventure Game!*\nType your action to begin your quest.").send()

# 💬 Handle Player Input
@cl.on_message
async def run(message):
    context = cl.user_session.get("context")

    msg = message.content.lower()

    # 📦 Check inventory manually
    if "check inventory" in msg or "my items" in msg:
        items = context["inventory"]
        if items:
            inventory_text = "\n".join([f"🔹 {item}" for item in items])
            await cl.Message(f"🎒 Your inventory:\n{inventory_text}").send()
        else:
            await cl.Message("📦 Your inventory is empty. Go explore!").send()
        return

    # ❤️ Check health manually
    if "my health" in msg or "check health" in msg:
        await cl.Message(f"❤️ Your current health: {context['health']} HP").send()
        return

    # 🧠 Choose agent
    agent = get_active_agent(message.content)
    reply = agent.respond(message.content, context)
    await cl.Message(reply).send()
