print("Simulation Module Loaded")

    
class PrisonSimulation:
    def __init__(self, agents, max_turns=12):
        self.agents = agents
        self.max_turns = max_turns
        print(f"PrisonSimulation initialized with {len(agents)} agents and max turns: {max_turns}")

    def run(self):
        for turn in range(self.max_turns):
            print(f"Turn {turn + 1}/{self.max_turns}")
            for agent in self.agents:
                message = f"Agent {agent.agent_id} ({agent.role}) is thinking..."
                response = agent.respond(message)
                print(response)
            print("End of turn\n")