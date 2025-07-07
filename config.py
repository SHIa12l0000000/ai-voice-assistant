import openai

# Replace this with your actual API key
openai.api_key = "your-openai-api-key"

def ask_openai(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a helpful AI assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']
  
