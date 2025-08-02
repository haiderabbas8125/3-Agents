# 🎮 Game Master Agent (Fantasy Adventure)

## 🧠 What It Does
A fantasy adventure game using multi-agent AI to create an interactive story. Features:
- **NarratorAgent**: Advances the storyline
- **MonsterAgent**: Creates combat encounters
- **ItemAgent**: Introduces magical item events
- **Tools**:
  - `roll_dice()`: Random number for events
  - `generate_event()`: Generates monster or item
- **Dynamic Handoff**: Switches between agents based on player input (e.g., "fight", "search", "continue")

## 🔧 Setup
1. Clone repo and create `.env` file:
    ```
    GEMINI_API_KEY=your_google_gemini_key
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Run Chainlit app:
    ```
    chainlit run main.py
    ```

## ✅ Features
- Uses OpenAI Agent SDK + Runner via Chainlit
- 3 agents with handoff logic
- Modular structure
