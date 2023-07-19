import openai
from decouple import config


openai.api_key = config("API_KEY")

messages = [
    {"role": "system", "content": "Você é um assistente útil."},
    {"role": "user", "content": "Quem ganhou a série mundial em 2020?"},
    {"role": "assistant", "content": "Os Los Angeles Dodgers venceram a World Series em 2020."},
    {"role": "user", "content": "Onde foi tocado?"}
]

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=messages
)

response_message = response['choices'][0]['message']['content']
usage = response['usage'].to_dict()

print(response_message)
print(usage)
