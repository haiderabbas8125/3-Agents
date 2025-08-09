import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_status(player):
    print("\n--------------------------------------------------")
    print(f"🧍 Player: {player['name']} (Level {player['level']})")
    print(f"📍 Location: {player['location']}")
    print(f"❤️ Health: {player['health']}/100")
    print(f"💰 Gold: {player['gold']}, 🌟 XP: {player['xp']}")
    print("--------------------------------------------------")
