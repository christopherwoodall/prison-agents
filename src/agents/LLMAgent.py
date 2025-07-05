print("AGENT MODULE LOADED")

class LLMAgent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        print(f"LLMAgent created with name: {self.name} and role: {self.role}")

    def respond(self, message: str) -> str:
        response = f"{self.name} ({self.role}): {message}"
        print(f"Response generated: {response}")
        return response
