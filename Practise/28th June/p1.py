from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """

You are an AI chatbot

"""

response = client.chat.completions.create(
    model = "gpt-4o",
    messages=[
        {"role" : "system" , "content" : SYSTEM_PROMPT},
        {"role" : "user" , "content" : "Hey there!"}
    ]
)

print(response.choices[0].message.content)