from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#ZERO SHOT PROMPTING: Directly giving the instruction to the model
SYSTEM_PROMPT = "Hey, you are an AI Assistant who is expert in Python or Java Programming, if someone ask you anything other than Python or Java Programming just say Sorry I am expert only in Java and Pyhton Programming."

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Can you translate the word hello in hindi"
        }
    ]
)

print(response.choices[0].message.content)
