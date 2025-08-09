from dotenv import load_dotenv
from utils.game_utils import clear_screen, display_status
from agents.narrator_agent import NarratorAgent
from agents.monster_agent import MonsterAgent
from agents.item_agent import ItemAgent

load_dotenv()

def main():
    clear_screen()
    print("🎮 Welcome to the Fantasy Adventure Game!")
    print("This is a text-based adventure powered by AI agents.\n")

    name = input("Enter your character's name: ")
    print(f"\n🌟 Welcome, {name}! Your adventure begins...")

    player = {
        "name": name,
        "level": 1,
        "location": "forest",
        "health": 100,
        "gold": 50,
        "xp": 0
    }

    narrator = NarratorAgent()
    monster = MonsterAgent()
    item = ItemAgent()

    print("\n🎮 Starting Fantasy Adventure Game...")
    print("=" * 60)
    print("🎮 Game Master Agent System Active...")
    print("=" * 60)

    turns = 0
    while turns < 3 and player["health"] > 0:
        display_status(player)

        scene = narrator.create_scene(player["location"])
        print("\n📘 Story:", scene["story"])
        print("📘 Choices:", scene["choices"])

        choice = input("\nWhat will you do? ").lower()

        if "fight" in choice:
            result = monster.fight(player)
            if result["won"]:
                item.reward(player)
                player["xp"] += 20
            else:
                player["health"] -= result["damage"]

        elif "sneak" in choice:
            print("You tried to sneak past... (rolls dice...)")
            # add dice logic or agent decision

        elif "feed" in choice or "use" in choice:
            item.use_item(player)

        turns += 1

    print("\n🎬 Game Over!")
    display_status(player)
    if player["health"] > 0:
        print("🏆 You survived the adventure!")
    else:
        print("💀 You were defeated. Try again!")

if __name__ == "__main__":
    main()
