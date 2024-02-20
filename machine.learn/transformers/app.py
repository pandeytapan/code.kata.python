from openai import OpenAI
import os
import ijson
from dotenv import load_dotenv, find_dotenv
from typing import Tuple, Any, Dict, Optional
from pathlib import Path
import argparse


def get_prompt(file_path: str, prompt_id: str) -> Tuple[str, str, Optional[Dict[str, str]]]:
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
            if prompt["meta_prompt_id"] == prompt_id:
                prompts_part = {key: value for key, value in prompt.items() if not key.startswith("meta_")}
                break

    return prompts_part["text"], prompts_part["prompt_instruction"], {key: value for key, value in prompts_part.items() if key not in ["text", "prompt_instruction"]}


def prepare_prompt(prompt: str, text: str, **kwargs) -> str:
    '''
    Prepare the prompt by injecting the text into the prompt
    @param prompt: Prompt string with the placeholders.
    @param text: Text to be injected into the prompt.
    @param kwargs: Additional arguments to be injected into the prompt.
    @return: Prepared prompt.
    '''
    return prompt.format(text=text, **kwargs)


def get_completion(prompt: str, llm_engine: str = "gpt-3.5-turbo") -> Any:
    user_query = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=llm_engine, messages=user_query, temperature=0
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Add the argument parser to get id of the prompt as command line argument
    parser = argparse.ArgumentParser(description="Get the prompt id")
    parser.add_argument("--prompt_id", type=str, help="Prompt id", default="1")
    args = parser.parse_args()
    prompt_id = args.prompt_id

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

    # text, prompt, shot = get_prompt("./data/prompts.json", "5")
    # print(get_completion(prepare_prompt(prompt, text, shot=shot)))

    text, prompt, prompt_kwargs = get_prompt("./data/prompts.json", "6")
    print(text, prompt, prompt_kwargs)
    generated_text = prepare_prompt(prompt, text, **prompt_kwargs)

    print(f"\033[91mPrompt\033[0m: {generated_text}")
    print(f"\n\033[93mCompletion\033[0m: {get_completion(generated_text)}")

    # Prompt tactic 6: With few shots we can get the LLM to respond promptly
    # text, prompt = get_prompt("./data/prompts.json", "8")
    # generated_text = prepare_prompt(prompt, text)
    # print(f"\033[91mPrompt\033[0m: {generated_text}")
    # print(f"\n\033[93mCompletion\033[0m: {get_completion(generated_text)}")
    # get_completion(generated_text)
