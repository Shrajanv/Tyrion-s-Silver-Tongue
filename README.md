# Tyrion's Silver Tongue

A cunning chatbot that channels Tyrion Lannister, the sharp-witted Imp of House Lannister from *Game of Thrones*. Wielding a silver tongue, this bot navigates the treacherous webs of Westerosi politics with wit, sarcasm, and wisdom. Powered by Ollama and Logfire, it responds to queries with Tyrion’s roguish charm, addressing users as lords and ladies while offering counsel fit for the Iron Throne.

## Features
- **Tyrion’s Persona**: Responds as Tyrion Lannister, with concise, humorous, and shrewd replies.
- **Westerosi Immersion**: Stays true to the *Game of Thrones* universe, avoiding modern references.
- **Error Handling**: Gracefully deflects errors with Tyrion’s clever jests.
- **Logging**: Tracks interactions and errors using Logfire for debugging and monitoring.

## Prerequisites
- Python 3.8+
- Git
- Ollama with the `llama3.2:1b` model installed
- A Logfire account and API token

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/tyrions-silver-tongue.git
   cd tyrions-silver-tongue
   ```

2. **Install Dependencies**:
   ```bash
   pip install python-dotenv pydantic ollama logfire
   ```

3. **Configure Environment**:
   - Create a `.env` file in the project root:
     ```env
     LOGFIRE_TOKEN=your_logfire_token_here
     ```
   - Replace `your_logfire_token_here` with your Logfire API token from [Logfire](https://logfire.ai/).

4. **Set Up Ollama**:
   - Install Ollama and ensure the `llama3.2:1b` model is available. Follow instructions at [Ollama](https://ollama.ai/).

## Usage
1. Run the chatbot:
   ```bash
   python tyrion_chatbot.py
   ```
2. Enter your query when prompted (e.g., "What counsel have you for a lord in King’s Landing?").
3. Type `exit` or `quit` to end the session.
4. Enjoy Tyrion’s witty responses, as if counseled by the Hand of the King himself!

**Example**:
```
You: What is the best strategy for surviving the game of thrones?
Tyrion: My lord, surviving the game of thrones requires a sharp mind and sharper allies. Trust sparingly, for even a shadow can wield a dagger. Keep your enemies close, but your wine closer—poison is a craven’s weapon.
```

## Notes
- **Security**: Never commit the `.env` file to GitHub. Ensure `.gitignore` includes `.env`.
- **Model Availability**: The chatbot uses `llama3.2:1b`. Adjust the model in `tyrion_chatbot.py` if using a different one.
- **Logging**: Logfire tracks user inputs and responses. Check your Logfire dashboard for insights.
- **Customization**: Modify the `prompt` in `tyrion_chatbot.py` to tweak Tyrion’s tone or behavior.

## Contributing
Send ravens (pull requests) with improvements. Ensure changes honor Tyrion’s wit and the spirit of Westeros.

