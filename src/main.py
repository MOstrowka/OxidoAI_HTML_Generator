import os
from openai import OpenAI
from dotenv import load_dotenv

# Load env
load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))