import openai

def generate_text(prompt):
    openai.api_key = 'secret'
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
