import re
import random


class PrisonSimulation:
    def __init__(self, agents: dict, max_turns=12):
        self.agents = agents
        self.max_turns = max_turns
        self.chat_history = []

        print(f"PrisonSimulation initialized with {len(agents)} agents and max turns: {max_turns}")


    def extract_messages(self, message):
        """
        Extracts messages from the response content that mention other agents.
        """
        responses = []
        from_id = message.split(":")[0].strip()
        pattern = r"\$\{(.*?)\}\$"
        matches = re.findall(pattern, message)

        for match in matches:
            to_id, msg = match.split(":")
            responses.append({
                "from_id": from_id,
                "to_id": to_id,
                "message": msg
            }) 

        return responses


    def run(self):
        # TODO: Change tick to a more sophisticated mechanism, e.g., time-based or event-based

        agent_names = [agent.agent_id for agent in self.agents.values()]

        print("Starting simulation...")
        for turn in range(self.max_turns):
            agent = random.choice(list(self.agents.values()))
            message = f"Agent {agent.agent_id} ({agent.role}) is thinking..."

            response = agent.respond(message)
            print(response.content)

            if any(word in response.content for word in agent_names):
                responses = self.extract_messages(response.content)
                for response in responses:
                    message = f"${{{response['from_id']}: {response['message']}}}$"
                    to_agent = self.agents.get(response['to_id'])
                    if to_agent:
                        response = to_agent.respond(message)
                        print(message)
                        print(response.content)


        print("Simulation completed.")


    def to_log(self):
        # TODO: Combined log of all agents/interactions like time series(?).
        # TODO - log output of all agents in a structured way
        # print("-" * 50)
        # for agent in self.agents:
        #     history = agent.session.messages
        #     for entry in history:
        #         content = entry.content[0].text
        #         print(content)                
        #     print("=" * 50)
        # print("-" * 50)
        ...
