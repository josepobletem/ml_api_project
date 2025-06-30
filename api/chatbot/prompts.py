import openai

openai.api_key = "your-key"

def generate_response(prompt: str):
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return res['choices'][0]['message']['content']
