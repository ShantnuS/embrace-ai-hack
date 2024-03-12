import os
import openai

# OpenAI Config
openai.api_key = "<YOUR_API_KEY>"
openai.api_base = "https://polite-ground-030dc3103.4.azurestaticapps.net/api/v1"
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
deployment_name='gpt-35-hackathon' 

# Variables
messages = []
system_prompt = 'You are an AI assistant that helps people find information.'

# Send query to OpenAI
def send_openai_query(messages):
    response = openai.ChatCompletion.create(
        engine=deployment_name, 
        temperature=0.9,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        max_tokens=150,
        messages = messages
    )
    return response['choices'][0]['message']['content']

def add_to_messages(role, content):
    messages.append(
        {
            "role": role,
            "content": content
        }
    )

add_to_messages("system", system_prompt)

while True:
    # Get input from user
    user_input = input("User: ")
    add_to_messages("user", user_input)
    azure_openai_response = send_openai_query(messages)
    add_to_messages("assistant", azure_openai_response)
    print("Azure OpenAI Service: " + azure_openai_response)