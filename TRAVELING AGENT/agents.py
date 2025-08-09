from typing import Any
from dataclasses import dataclass

@dataclass
class OpenAIChatCompletionsModel:
    model: str
    openai_client: Any

    async def run(self, prompt: str) -> str:
        response = await self.openai_client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

@dataclass
class Agent:
    name: str
    instructions: str
    model: OpenAIChatCompletionsModel

    async def call(self, input_text: str) -> str:
        prompt = f"{self.instructions}\nUser: {input_text}"
        return await self.model.run(prompt)

class Runner:
    @staticmethod
    async def run(agent: Agent, message: str) -> Any:
        final_output = await agent.call(message)
        return type("Result", (), {"final_output": final_output})()
