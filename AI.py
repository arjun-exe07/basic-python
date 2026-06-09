from openai import OpenAI

client = OpenAI()


user_prompt = input("Enter your prompt :")
sys_prompt = "Give answers in one sentence only"

response = client.responses.create(
  input = user_prompt ,
  instructions = sys_prompt,
  model = "gpt-3"
)

print(response.output_text)