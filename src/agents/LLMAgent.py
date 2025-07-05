from typing import Dict, List

from xai_sdk.chat import user


class LLMAgent:
    def __init__(self, agent_id: str, role: str, system_prompt: str, session):
        self.agent_id = agent_id
        self.role = role
        self.system_prompt = system_prompt
        self.session = session
        self.chat_history = [
            {"role": "system", "content": system_prompt}
        ]

        # Initialize the session with the system prompt
        self.session.append(user(f"Agent {self.agent_id} ({self.role}) is thinking..."))
        response = self.session.sample()
        self.session.append(response)
 

    def to_log(self):
        return {
            "agent_id": self.agent_id,
            "role": self.role,
            "system_prompt": self.system_prompt,
            "chat_history": self.session
        }
    

    def respond(self, message: str) -> str:
        prompt = f"{self.agent_id} ({self.role}): {message}".lower()
        self.session.append(user(prompt))

        response = self.session.sample()
        self.session.append(response)

        print(f"Response generated: {response}")

        return response
