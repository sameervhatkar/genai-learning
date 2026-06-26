from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

PROMPT = """
### Instruction:
You are an expert DSA instructor.
Explain Binary Search to a beginner.

### Input:
The student knows arrays but has never learned Binary Search.

### Response:
"""

response = client.responses.create(
    model="gpt-4o-mini",
    input=PROMPT
)

print(response.output_text)