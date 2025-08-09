from .base_agent import BaseAgent
from tools.dice_tools import roll_dice

class MonsterAgent(BaseAgent):
    def fight(self, player):
        print("\n⚔️ A monster appears!")
        player_roll = roll_dice(20)
        monster_roll = roll_dice(20)

        print(f"You roll: {player_roll} | Monster rolls: {monster_roll}")

        if player_roll >= monster_roll:
            print("✅ You defeated the monster!")
            return {"won": True, "damage": 0}
        else:
            damage = roll_dice(10)
            print(f"💥 The monster hits you! Damage taken: {damage}")
            return {"won": False, "damage": damage}
