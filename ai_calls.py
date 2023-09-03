import openai
import os

def call_ai(prompt):
    
    # Get API KEY from environment
    openai.api_key = os.environ['EXAM_PROTOTYPE_OPENAI_API_KEY']

    # Call AI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
            "role": "user",
            "content": prompt
            }
        ],
        temperature=1,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

    return str(response['choices'][0]['message']['content'])


# Mock function to simulate calling Gen Ai using text version of output prompts
# Useful for testing - not used in live version
def mock_ai(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    return content