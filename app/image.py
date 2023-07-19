import openai
from decouple import config

openai.api_key = config("API_KEY")

response = openai.Image.create(
    prompt="a white siamese cat",
    n=1,
    size="256x256",
    response_format="b64_json"
)
# image_url = response['data'][0]['url']
# print(image_url)
print(response)
