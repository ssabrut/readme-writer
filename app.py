from src.model import Claude
from dotenv import load_dotenv
import os

load_dotenv()

with open("src/prompts/title.txt", "r") as file:
    prompt = file.read()
#     name = "E-Commerce store for keyboard enthusiast"

#     goals = """A platform for keyboard enthusiasts to buy and sell custom keyboards, keycaps, and other accessories. Also have a community forum for users to discuss and share their builds."""

#     technologies = """1. MongoDB
# 2. Express.js
# 3. React.js
# 4. Node.js"""

#     # replace [NAME] on prompt
#     prompt = prompt.replace("[NAME]", name)

#     prompt = prompt.replace("[GOALS]", goals)
#     prompt = prompt.replace("[TECHNOLOGIES]", technologies)

claude = Claude(api_key=os.getenv("ANTHROPIC_API_KEY"))
response = claude.generate("I want to create E-Commerce store for keyboard enthusiast", prompt)
print(response[0].text)