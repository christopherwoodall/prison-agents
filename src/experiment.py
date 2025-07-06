import os

from pathlib import Path
from typing import Any, Dict, Optional

import yaml

from xai_sdk import Client
from xai_sdk.chat import system

from simulations.prison import PrisonSimulation
from agents.LLMAgent import LLMAgent


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
    agents = {}
    max_turns = 6

    api_key = os.getenv("XAI_API_KEY")
    client = Client(api_key=api_key)

    config_path = Path("simulation_config.yaml")
    config = read_config(config_path)
    simulation_config = config["simulation_config"]

    for agent in simulation_config["agents"]:
        if "id" not in agent or "role" not in agent:
            print("Agent configuration is missing 'id' or 'role'. Skipping this agent.")
            continue


        initial_prompt = "\n".join([simulation_config["system_prompt"], agent["initial_prompt"]])
        session = client.chat.create(
            model="grok-3",
            messages=[system(initial_prompt)],
        )

        agents[agent["id"]] = LLMAgent(
            agent_id=agent["id"],
            role=agent["role"],
            initial_prompt=agent["initial_prompt"],
            session=session)

        print(f"Agent created: {agent['id']} with role: {agent['role']}")

    # Run the simulation
    simulation = PrisonSimulation(agents, max_turns=max_turns)
    simulation.run()


if __name__ == "__main__":
    main()
