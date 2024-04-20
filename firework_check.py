from fireworks.client import Fireworks

client = Fireworks(api_key="et9MwRyCcuEHGK5JQqTHKIgWAZEaYwB5GAbnlA0RkF8ZAaZT")
response = client.chat.completions.create(
  model="accounts/fireworks/models/llama-v2-7b-chat",
  messages=[{
    "role": "user",
    "content": "Say this is a test",
  }],
)
print(response.choices[0].message.content)
