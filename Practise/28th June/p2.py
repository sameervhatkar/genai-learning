import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """

        YOU ARE AN EXPERT IN TECHNOLOGICAL FIELD

"""

response = client.chat.completions.create(
    model = "gemini-2.5-flash",
    messages = [
        {"role" : "system", "content" : SYSTEM_PROMPT},
        {"role" : "user", "content" : "Hey how are you and who you are?"}
    ]
)

print(response.choices[0].message.content)