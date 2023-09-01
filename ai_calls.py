import openai

def call_ai(prompt):
    
    openai.api_key = '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'
    
    print(prompt)
    print(openai.api_key)

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

    print(response['choices'][0]['message']['content'])

    return str(response['choices'][0]['message']['content'])