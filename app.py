from src.model import Claude
from dotenv import load_dotenv
import os

load_dotenv()

with open("src/prompts/title.txt", "r") as file:
    prompt = file.read()

claude = Claude(api_key=os.getenv("ANTHROPIC_API_KEY"))
response = claude.generate("I want to create E-Commerce store for keyboard enthusiast", prompt)
print(response[0].text)