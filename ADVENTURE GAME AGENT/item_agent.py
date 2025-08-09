from tools.dice_tools import roll_dice

class ItemAgent:
    def reward(self, player):
        loot = ["Gold Coins", "Health Potion", "Magic Ring", "XP Scroll"]
        found = loot[roll_dice(len(loot)) - 1]
        print(f"🎁 Loot: You found a {found}!")

        if found == "Gold Coins":
            player["gold"] += 20
        elif found == "Health Potion":
            player["health"] = min(100, player["health"] + 20)
        elif found == "Magic Ring":
            player["xp"] += 15
        elif found == "XP Scroll":
            player["xp"] += 30

    def use_item(self, player):
        print("🧪 You try to use an item from your bag... (but inventory system isn't active yet)")
