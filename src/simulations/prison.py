import random


class PrisonSimulation:
    def __init__(self, agents, max_turns=12):
        self.agents = agents
        self.max_turns = max_turns
        self.chat_history = []

        self.agent_dict = {agent.agent_id: agent for agent in agents}
        # TODO: Make it so that agents can address each other by name

        print(f"PrisonSimulation initialized with {len(agents)} agents and max turns: {max_turns}")


    def run(self):
        # TODO: Change tick to a more sophisticated mechanism, e.g., time-based or event-based

        agent_names = [agent.agent_id for agent in self.agents]

        print("Starting simulation...")
        for turn in range(self.max_turns):
            agent = random.choice(self.agents)
            message = f"Agent {agent.agent_id} ({agent.role}) is thinking..."
            response = agent.respond(message)
            # print(response)

            if any(word in response.content for word in agent_names):
                print(f"Agent {agent.agent_id} mentioned another agent in their response.")
            
            print(response.content)

        print("-" * 50)
        for agent in self.agents:
            history = agent.session.messages
            for entry in history:
                content = entry.content[0].text
                print(content)                
            print("=" * 50)
        print("-" * 50)

        print("Simulation completed.")


    def to_log(self):
        # TODO: Combined log of all agents/interactions as time series.
        ...
