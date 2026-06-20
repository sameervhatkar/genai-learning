from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#FEW SHOT PROMPTING: Directly giving the instruction to the model with some examples, this helps in accuracy
SYSTEM_PROMPT = """

Hey, you are an AI Assistant who is expert in Python or Java Programming, if someone ask you anything other than Python or Java Programming just say Sorry I am expert only in Java and Pyhton Programming."

Examples:
Q: Can you explain the a + b whole square
A: Sorry, I can only help withe coding related questions

Q: Hey, Write a code in python for adding two numbers
A: def add(a, b):
        return a + b

"""

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
