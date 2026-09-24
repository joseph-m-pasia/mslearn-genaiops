import os
from pathlib import Path

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

# Load environment variables from .env
load_dotenv()

# Read instructions from prompt file
prompt_file = Path(__file__).parent / "prompts" / "v1_instructions.txt"

with open(prompt_file, "r", encoding="utf-8") as f:
    instructions = f.read().strip()

# Create Azure AI Foundry project client
project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

# Get the model deployment name
model_name = os.environ["MODEL_NAME"]

print(f"Project endpoint: {os.environ['AZURE_AI_PROJECT_ENDPOINT']}")
print(f"Model deployment: {model_name}")

# Create agent version
agent = project_client.agents.create_version(
    agent_name=os.environ["AGENT_NAME"],
    definition=PromptAgentDefinition(
        model=model_name,
        instructions=instructions,
    ),
)

print(
    f"Agent created (id: {agent.id}, "
    f"name: {agent.name}, "
    f"version: {agent.version})"
)