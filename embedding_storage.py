from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import openai

uri = "mongodb+srv://pgarg4:TE8HRkPMv18iBj64@cluster0.7y0k8ar.mongodb.net" # you can copy uri from MongoDB Atlas Cloud Console https://cloud.mongodb.com


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
fw_client = openai.OpenAI(
  api_key="et9MwRyCcuEHGK5JQqTHKIgWAZEaYwB5GAbnlA0RkF8ZAaZT", # you can find Fireworks API key under accounts -> API keys
  base_url="https://api.fireworks.ai/inference/v1"
)


def check_mongodb_connection():
    try:
        # Attempt to fetch a list of databases
        databases = client.list_database_names()
        print("MongoDB connection successful. Databases:", databases)
    except Exception as e:
        print("Failed to connect to MongoDB:", e)

def check_fireworks_connection():
    try:
        # Assuming there's an endpoint to fetch user/account info or similar lightweight operation
        response = fw_client.Completion.create(prompt="Test", max_tokens=5)  # This is OpenAI's API, adjust if different
        print("Fireworks API connection successful. Response:", response)
    except Exception as e:
        print("Failed to connect to Fireworks API:", e)

def main():
    check_mongodb_connection()
    check_fireworks_connection()

if __name__ == "__main__":
    main()
