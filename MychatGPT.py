import os
import openai
from dotenv import load_dotenv
from promptlayer import PromptLayer
PromptLayer.templates.get("MychatGPT", {"MYchatGPT": "prod"})
load_dotenv('.env')
promptlayer_client = PromptLayer(api_key=os.getenv(""))
OpenAI = promptlayer_client.openai.OpenAI
client = OpenAI()
user_input = input("Welcome to MychatGPT! How can I help?\n> ")
# Grab the prompt from PromptLayer
MYchatGPT_prompt = promptlayer_client.templates.get("MychatGPT", {
    "provider": "openai",
    "input_variables": {
        "question": user_input
    }
})
response = client.chat.completions.create(
    **mychatgpt_prompt['llm_kwargs'],
    pl_tags=["MYchatGPT-dev"],
)
print(response.choices[0].message.content)
messages = mychatgpt_prompt['llm_kwargs']['messages']
response_message = response.choices[0].message
messages.append(response_message)
while True:
    user_input = input("> ")
    messages.append({"role": "user", "content": user_input})
    # Send it to the LLM
    mychatgpt_prompt['llm_kwargs']['messages'] = messages
    response = client.chat.completions.create(
        **mychatgpt_prompt['llm_kwargs'],
        pl_tags=["MYchatGPT-dev"],
    )
    response_message = response.choices[0].message
    # Update the prompt with the newest response
    messages.append(response_message)
    print(response_message.content)
