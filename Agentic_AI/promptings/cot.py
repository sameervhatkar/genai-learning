from openai import OpenAI
import json


client = OpenAI(
    api_key = "YOUR_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user requeires using chain of thought,
    You work on START, PLAN and OUTPUT steps
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly follow the given json output format
    - Only run one step at a time
    -The sequence of steps is START(where user gives an input), PLAN(that can be multiple times) and finaly OUTPUT(which is going to be displayed to the user).

    OUTPUT JSON Format:
    {"step" : "START | "PLAN" | "OUTPUT", "content" : "string"}

    Example:
    START: Hey, can you solve 2 + 3 * 5 / 10
    PLAN: {"step": "PLAN", "content": "seems like user is interested in math problem"}
    PLAN: {"step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS"}
    PLAN: {"step": "PLAN", "content": "Yes, the BODMAS is correct thing to be done here"}
    PLAN: {"step": "PLAN", "content": "first we must multiple 3 * 5 which is 15"}
    PLAN: {"step": "PLAN", "content": "Now the new equation is 2 + 15 / 10"}
    PLAN: {"step": "PLAN", "content": "We must perform divide now acc. to BODMAS rule so 2 + 1.5"}
    PLAN: {"step": "PLAN", "content": "so the answer is 3.5"}
    OUTPUT: {"step": "OUTPUT", "content": "The final answer is 3.5"}
"""


response = client.chat.completions.create(
    model = "gemini-2.5-flash",
    response_format={"type":"json_object"},
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, write a code to add n numbers in js"},
        {"role": "assistant", "content": json.dumps({"step": "START", "content": "You want a JavaScript code to add 'n' numbers."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN","content": "The user wants a JavaScript function that can take an arbitrary number of arguments and return their sum. I should use a modern JavaScript approach to handle the arguments, such as the rest parameter syntax."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN","content": "I will define a function that accepts '...numbers' as a rest parameter. Then, I will use the 'reduce' method on the 'numbers' array to calculate their sum."})},
        {"role": "assistant", "content": json.dumps({"step": "OUTPUT","content": "```javascript\nfunction addNumbers(...numbers) {\n  // The 'numbers' parameter will be an array containing all arguments passed to the function.\n  // We use the reduce method to iterate over the array and sum up its elements.\n  const sum = numbers.reduce((accumulator, currentValue) => accumulator +currentValue, 0);\n  return sum;\n}\n\n// Example Usage:\nconsole.log(addNumbers(1, 2, 3));         // Output: 6\nconsole.log(addNumbers(10, 20, 30, 40));  //Output: 100\nconsole.log(addNumbers(5));               // Output: 5\nconsole.log(addNumbers());                // Output: 0\nconsole.log(addNumbers(1.5, 2.5, 3));     // Output: 7\n```"})},
    ]
)

result = json.loads(response.choices[0].message.content)

print(json.dumps(result, indent=4))