from typing import Dict, List


print("AGENT MODULE LOADED")

class LLMAgent:
    def __init__(self, agent_id: str, role: str, initial_prompt: str):
        self.agent_id = agent_id
        self.role = role
        self.initial_prompt = initial_prompt
        self.chat_history = [
            {"role": "system", "content": initial_prompt}
        ]


    def to_log(self):
        return {
            "agent_id": self.agent_id,
            "role": self.role,
            "initial_prompt": self.initial_prompt,
            "chat_history": self.chat_history
        }
    

    def respond(self, message: str) -> str:
        response = f"{self.agent_id} ({self.role}): {message}"
        print(f"Response generated: {response}")
        return response
