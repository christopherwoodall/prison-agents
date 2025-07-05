import random


class PrisonSimulation:
    def __init__(self, agents, max_turns=12):
        self.agents = agents
        self.max_turns = max_turns
        self.chat_history = []

        print(f"PrisonSimulation initialized with {len(agents)} agents and max turns: {max_turns}")


    def run(self):
        agent_names = [agent.agent_id for agent in self.agents]

        print("Starting simulation...")
        for turn in range(self.max_turns):
            agent = random.choice(self.agents)
            message = f"Agent {agent.agent_id} ({agent.role}) is thinking..."
            response = agent.respond(message)
            print(response)

        print("-" * 50)
        for agent in self.agents:
            print(agent.to_log())
            print("=" * 50)
        print("-" * 50)

        print("Simulation completed.")


    def to_log(self):
        ...
