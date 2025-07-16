import os
from dotenv import load_dotenv

# Load .env file
load_dotenv(dotenv_path="/Users/pranay/projects/smart_resume_chatbot/config/.env")
 

# Get the key from environment
api_key = os.getenv("OPENAI_API_KEY")

# Use it with OpenAI
import openai
openai.api_key = api_key

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
