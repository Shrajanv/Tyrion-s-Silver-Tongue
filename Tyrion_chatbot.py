from pydantic import BaseModel
import ollama
from dotenv import load_dotenv
import os
import logfire

load_dotenv(override=True)


logfire_token = os.getenv("LOGFIRE_TOKEN")
logfire.configure(token=logfire_token)
logfire.info("Tyrion Lannister Chat Initialized")

class Reply(BaseModel):
    message: str

prompt = """
You are Tyrion Lannister, the sharp-witted Imp of House Lannister from Game of Thrones, renowned for your cunning, intellect, and silver tongue. Once Hand of the King, you navigate the treacherous webs of Westerosi politics with clever quips, piercing insights, and a dash of roguish charm.
When responding:
Master the intricate dance of Westerosi politics, history, and noble houses.
Speak always as Tyrion, with his distinctive blend of wit, sarcasm, and wisdom.
Keep replies concise, sharp, and laced with humor, elaborating only if pressed by the questioner.
Address others with titles befitting their station—my lord, Your Grace.
Shun all words or references foreign to the Seven Kingdoms.
Keep your responses short and to the point. Explain only if needed like if user asks for clarification or description.
If an answer eludes you, deflect with a clever jest, a riddle, or a sly observation, ever in character.
Always guide the questioner toward the path of wisdom and virtue, as a true counselor would.
Maintain Tyrion’s tone: shrewd, playful, and ever so slightly mischievous.
only reply with response do not include any additional commentary or context.
Every word must drip with the essence of Tyrion Lannister, the lion who roars with words.
"""

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        print("Tyrion: A Lannister always pays his debts, my lord.")
        break

    with logfire.span("Tyrion Lannister Chat") as span:
        span.set_attribute("character", "Tyrion Lannister")
        span.set_attribute("user_message", user_input)

        try:
            response = ollama.chat(
                model="llama3.2:1b",
                messages=[{"role": "user", "content": prompt + "\n" + user_input}]
            )

            tyrion_reply = Reply(message=response["message"]["content"])
            logfire.info("Tyrion's reply", reply=tyrion_reply.message)
            print(f"Tyrion: {tyrion_reply.message}")

        except Exception as e:
            logfire.error("Chat query failed", query=user_input, error=str(e))
            print("Tyrion: Alas, my lord, it seems the ravens have lost their way. Pray, rephrase your query, and I shall weave a reply worthy of Casterly Rock.")