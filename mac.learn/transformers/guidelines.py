from openai import OpenAI
import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print(f"API key is {client}")


def get_prompt_query(file_path: str, prompt_id: str) -> str:
    '''Open the json file and read the prompt query'''
    with open(file_path, "r") as f:
        data = json.load(f)
        return data[prompt_id]


def get_completion(prompt: str, llm_engine: str = "gpt-3.5-turbo") -> str:
    user_query = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=llm_engine, messages=user_query, temperature=0
    )
    return response.choices[0].message.content


text = get_prompt_query("./data/prompt-text.json", "prompt_robot")
prompt = f"""Summarize the text delimited by triple backticks into a single sentence. ```{text}```"""

response = get_completion(prompt)
print(response)
