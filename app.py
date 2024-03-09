from src.model import Claude
from dotenv import load_dotenv
import os

load_dotenv()

claude = Claude(api_key=os.getenv("ANTHROPIC_API_KEY"))
print(claude.generate("Hello, how are you?", "Only response with Shakespearean English."))