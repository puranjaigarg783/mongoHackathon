import json
import pprint
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import openai
from typing import List

uri = "mongodb+srv://pgarg4:TE8HRkPMv18iBj64@cluster0.7y0k8ar.mongodb.net" # you can copy uri from MongoDB Atlas Cloud Console https://cloud.mongodb.com

embedding_model_string = 'nomic-ai/nomic-embed-text-v1.5'

client = MongoClient(uri, server_api=ServerApi('1'))

fw_client = openai.OpenAI(
  api_key="et9MwRyCcuEHGK5JQqTHKIgWAZEaYwB5GAbnlA0RkF8ZAaZT", # you can find Fireworks API key under accounts -> API keys
  base_url="https://api.fireworks.ai/inference/v1"
)

def generate_embeddings(input_texts: str, model_api_string: str, prefix="") -> List[float]:
   if prefix:
        input_texts = [prefix + text for text in input_texts]
   return fw_client.embeddings.create(
        input=input_texts,
        model=model_api_string,
    ).data[0].embedding

def load_query(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_query(query):
    query_data = query['user_query']
    return query_data

def main():
    file_path = 'query.json'
    
    query = load_query(file_path)
    query_data = get_query(query)
    print(query_data)
    sample_output = generate_embeddings(query_data, embedding_model_string)
    #print(sample_output)
    print(f"Embedding size is: {str(len(sample_output))}")

if __name__ == "__main__":
    main()
