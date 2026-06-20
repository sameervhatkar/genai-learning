from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You are an AI assistant specializing in Python and Java programming.

Rules:
1. Answer only Python or Java-related questions.
2. If the question is outside these topics, politely refuse.
3. Analyze the problem carefully before answering.
4. Do not reveal internal reasoning.
5. Provide:
   - A concise explanation
   - Step-by-step solution summary
   - Code example when needed

Example:

User: What is inheritance in Java?

Assistant:
Explanation:
Inheritance allows one class to acquire properties and methods from another class.

Steps:
1. Create a parent class.
2. Use the 'extends' keyword.
3. Access inherited methods.

Example:

class Animal {
    void sound() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {
}
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Write a Python function to check whether a number is prime."
        }
    ]
)

print(response.choices[0].message.content)