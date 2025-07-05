from typing import Dict, List


class LLMAgent:
    def __init__(self, agent_id: str, role: str, system_prompt: str, session):
        self.agent_id = agent_id
        self.role = role
        self.system_prompt = system_prompt
        self.chat_history = [
            {"role": "system", "content": system_prompt}
        ]


    def to_log(self):
        return {
            "agent_id": self.agent_id,
            "role": self.role,
            "system_prompt": self.system_prompt,
            "chat_history": self.chat_history
        }
    

    def respond(self, message: str) -> str:
        response = f"{self.agent_id} ({self.role}): {message}"
        print(f"Response generated: {response}")
        
        # while True:
        #     prompt = input("You: ")
        #     if prompt.lower() == "exit":
        #         break
        #     chat.append(user(prompt))
        #     response = chat.sample()
        #     print(f"Grok: {response.content}")
        #     chat.append(response)

        return response
