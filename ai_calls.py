import openai
import os

def call_ai(prompt):
    
    openai.api_key = os.environ['EXAM_PROTOTYPE_OPENAI_API_KEY']

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