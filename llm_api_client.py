import os
import json
import time
from groq import Groq

# Initialize the Groq client with your API key
client = Groq(
    api_key=os.environ.get("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"),  
)

# defining the paths for input and output files
input_file_path = 'input.txt'
output_file_path = 'output.json'

# Read the input prompts from the text file
with open(input_file_path, 'r') as file:
    prompts = file.readlines()

responses = []

# Loop through each prompt and get the response from the API
for prompt in prompts:
    prompt = prompt.strip()  # Remove any whitespace
    if prompt:
        time_sent = int(time.time())  # Record the time the prompt was sent

        # API call
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",
        )

        # Record the time the response was received
        time_recvd = int(time.time())

        # Get the response message
        message = chat_completion.choices[0].message.content

        # create a response object in the required format
        responses.append({
            "Prompt": prompt,
            "Message": message,
            "TimeSent": time_sent,
            "TimeRecvd": time_recvd,
            "Source": "Groq"
        })

# to write the responses to a .json file
with open(output_file_path, 'w') as outfile:
    json.dump(responses, outfile, indent=4)

print(f"API responses have been saved to {output_file_path}")
