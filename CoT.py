import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

questions = [
    "why is it difficult to start learning AI engineering?",
    "how do i choose the right project to begin with?",
    "how should i learn AI engineering?",
    "can you suggest a roadmap for the same?"
]

for question in questions:
    print("normal response")
    normal_response = client.chat.completions.create(
        model = "openai/gpt-3.5-turbo",

        messages = [
            {
                "role":"user",
                "content":question
            }
        ]
    )
    print(normal_response.choices[0].message.content)

    print("chain of thought")
    cot_response = client.chat.completions.create(
        model = "openai/gpt-3.5-turbo",
        messages = [
            {
                "role":"user",
                "content":f"think step by step {question}"
            }
        ]
    )
    print(cot_response.choices[0].message.content)

