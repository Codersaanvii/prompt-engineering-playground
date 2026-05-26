import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client  = OpenAI(api_key = os.getenv("OPENAI_API_KEY"),
base_url="https://openrouter.ai/api/v1")

query = "How should a beginner start to learn AI engineering?"

system_prompts = [
        "you are a strict professor",
        "you explain in a polite friendly manner",
        "you are a motivational mentor",
        "you are a renowned startup CEO",
        "you are a concise expert"
    ]

for i,prompt in enumerate(system_prompts, start = 1):
        print(f"\nSYSTEM PROMPT:\n{prompt}")

        response = client.chat.completions.create(
            model = "openai/gpt-3.5-turbo",

            messages = [
                {
                    "role":"system",
                    "content":prompt
                
                },
                {
                    "role":"user",
                    "content":query
                }
            ]
        )
        answer = response.choices[0].message.content
        print("Question:",query)
        print("Answer:",answer)
        print(f"\nTokens used:{response.usage.total_tokens}")


