import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client  = OpenAI(api_key = os.getenv("OPENAI_API_KEY"),
base_url="https://openrouter.ai/api/v1")

query = "How should a beginner start to learn AI engineering?"

response = client.chat.completions.create(
    model = "openai/gpt-3.5-turbo",

    messages=[
        {
            "role":"system",
            "content": "you suggest good and unique coding projects to beginners"
        },
        {
            "role":"user",
            "content":"suggest a beginner friendly data analysis project"
        },
        {
            "role":"assistant",
            "content":"""
            project: analytics dashboard using simple data,
            difficulty: beginner,
            skills: tableau, powerBI,python, pandas
            """
        },
        {
            "role":"user",
            "content":"suggest a beginner to intermediate AI project"
        }
    ]

)

print(response.choices[0].message.content)