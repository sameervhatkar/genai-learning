from openai import OpenAI

client = OpenAI(
    api_key="your_new_gemini_key",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {
            "role": "system",
            "content": "Hey, you are an AI Assistant who is expert in Python or Java Programming, if someone ask you anything other than Python or Java Programming just say Sorry I am expert only in Java and Pyhton Programming."
        },
        {
            "role": "user",
            "content": "Can you explain what is Java"
        }
    ]
)

print(response.choices[0].message.content)
