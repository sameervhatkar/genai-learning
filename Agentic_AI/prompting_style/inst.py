from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

PROMPT = """
You are an expert DSA instructor.

Task:
Explain Binary Search to a beginner.

Requirements:
- Use simple language.
- Give one real-life analogy.
- Explain the algorithm.
- Show Java code.
"""

response = client.responses.create(
    model="gpt-4o-mini",
    input=PROMPT
)

print(response.output_text)