from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are an expert DSA instructor."
        },
        {
            "role": "user",
            "content": "Explain Binary Search to a beginner."
        }
    ]
)

print(response.choices[0].message.content)