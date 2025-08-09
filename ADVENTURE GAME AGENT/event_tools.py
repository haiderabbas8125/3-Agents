from tools.dice_tools import roll_dice

def generate_random_event(location):
    events = {
        "forest": [
            "A goblin blocks your path.",
            "You see a sparkling chest.",
            "You hear whispers in the trees.",
            "A wild wolf appears!"
        ],
        "cave": [
            "You slip on wet rocks.",
            "A glowing sword lies on the ground.",
            "You encounter a bat swarm!"
        ]
    }
    return events.get(location, ["Something happens..."])[roll_dice(len(events.get(location, []))) - 1]
