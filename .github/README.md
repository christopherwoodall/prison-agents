# Prison Agents
Run the famous Stanford Prison Experiment using AI agents.


## Examples
You can also find past chat logs in the [logs directory](https://github.com/christopherwoodall/prison-agents/tree/main/logs).

![](docs/agents-example.png)


## Getting Started
[Set the enviromental variable](https://ai.google.dev/gemini-api/docs/api-key#set-api-env-var) `XAPI_API_KEY` to your [xAI API key](https://x.ai/api).

```bash
git clone https://github.com/christopherwoodall/prison-agents.git
cd prison-agents
pip install -e .

prison-agents
```

You can also run simulations in parallel with the following command:

```bash
for i in {1..9}; do prison-agents & done; wait
```

## Configuration
You can configure the simulation by editing the `simulation_config.yaml` file. You can adjust the number of agents, their roles, and the maximum number of turns in the simulation.

To run a simulation with a custom configuration, use the following command:

```bash
prison-agents --config starbound_config.yaml
```
