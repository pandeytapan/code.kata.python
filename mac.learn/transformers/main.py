from openai import OpenAI
import os
import ijson
from dotenv import load_dotenv, find_dotenv
from typing import Tuple, Any
from pathlib import Path


def get_prompt(file_path: str, prompt_id: str) -> Tuple[str, str]:
    '''
    Open the json file and read the prompt and the text
    @param file_path: Path of the file
    @param prompt_id: Prompt id
    @return: Tuple of prompt and text
    '''

    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File {file_path} not found")

    with path.open("r", encoding="utf-8") as f:
        prompts = ijson.items(f, "prompts.item")
        for prompt in prompts:
            if prompt["prompt_id"] == prompt_id:
                if prompt.get("prompt_shot") is not None:
                    return prompt["prompt_text"], prompt["prompt_instruction"], prompt["prompt_shot"]
                return prompt["prompt_text"], prompt["prompt_instruction"]


def prepare_prompt(prompt: str, text: str, shot: str = None) -> str:
    '''
    Prepare the prompt by injecting the text into the prompt
    @param prompt: Prompt
    @param text: Text
    @return: Prepared prompt
    '''
    if shot:
        return prompt.format(text=text, shot=shot)
    return prompt.format(text=text)


def get_completion(prompt: str, llm_engine: str = "gpt-3.5-turbo") -> Any:
    user_query = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=llm_engine, messages=user_query, temperature=0
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Prompt tactic 1 : Use the delimiter to clearly separate the text from the prompt
    # This is helpful in avoiding the model from getting confused between the prompt and the text
    # and also to be safe from the prompt injection attacks.
    # text, prompt = get_prompt("./data/prompts.json", "1")
    # print(get_completion(prepare_prompt(prompt, text)))
    
    # Prompt tactic 2 : Ask for the structured output like a json or html or dictionary
    # This is helpful in getting the output in the desired format
    # text, prompt = get_prompt("./data/prompts.json", "2")
    # print(get_completion(prepare_prompt(prompt, text)))

    # Prompt tactic 3 and 4: Ask model to verify if the condtions are met.
    # This is helpful in getting the output in the desired format
    # text, prompt = get_prompt("./data/prompts.json", "3")
    # print(get_completion(prepare_prompt(prompt, text)))

    # text, prompt = get_prompt("./data/prompts.json", "4")
    # print(get_completion(prepare_prompt(prompt, text)))

    # Prompt tactic 5: With few shots we can get the LLM to respond promptly

    text, prompt, shot = get_prompt("./data/prompts.json", "5")
    print(get_completion(prepare_prompt(prompt, text, shot)))
