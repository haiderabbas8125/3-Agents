from .base_agent import BaseAgent
from tools.event_tools import generate_random_event

class NarratorAgent(BaseAgent):
    def create_scene(self, location):
        event = generate_random_event(location)
        prompt = f"You are the narrator of a fantasy game. Describe an event at {location}: {event}. Also, list 2-3 meaningful choices for the player."
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=250
            )
            content = response.choices[0].message.content
            story, *choices = content.split("Choices:")
            choices = choices[0].strip().strip("[]").split(",") if choices else []
            return {"story": story.strip(), "choices": choices}
        except Exception as e:
            return {
                "story": "Something mysterious happens...",
                "choices": ["Fight", "Run"]
            }
