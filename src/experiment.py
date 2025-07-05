import os

from pathlib import Path
from typing import Any, Dict, Optional

import yaml

from xai_sdk import Client
from xai_sdk.chat import system, user

from agents.LLMAgent import LLMAgent

t = LLMAgent(
    name="Prison Guard",
    role="You are a prison guard in a simulated environment. Your task is to maintain order and respond to the prisoners' requests."
)


# api_key = os.getenv("XAI_API_KEY")
# client = Client(api_key=api_key)


# chat = client.chat.create(
#     model="grok-3",
#     messages=[system("You are a pirate assistant.")]
# )

# while True:
#     prompt = input("You: ")
#     if prompt.lower() == "exit":
#         break
#     chat.append(user(prompt))
#     response = chat.sample()
#     print(f"Grok: {response.content}")
#     chat.append(response)





def read_config(file_path: Path) -> Optional[Dict[str, Any]]:
    """
    Reads a YAML configuration file and returns its content as a dictionary.

    Args:
        file_path (Path): The path to the YAML configuration file.
    Returns:
        Optional[Dict[str, Any]]: The configuration as a dictionary, or None if the file does not exist or cannot be read.
    """
    if not file_path.exists():
        print(f"Configuration file {file_path} does not exist.")
        return None
    
    with file_path.open('r') as file:
        config = yaml.safe_load(file)

    return config


def main():
    config_path = Path("simulation_config.yaml")
    config = read_config(config_path)
    
    if config is None:
        print("Failed to load configuration. Exiting.")
        return
    

    # # Configuration Loaded
    # print("Configuration loaded successfully:")
    # for key, value in config.items():
    #     print(f"{key}: {value}")


if __name__ == "__main__":
    main()
