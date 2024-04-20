from AtlasClient import AtlasClient
import os,sys
## Load Settings from .env file
from dotenv import find_dotenv, dotenv_values

# _ = load_dotenv(find_dotenv()) # read local .env file
config = dotenv_values(find_dotenv())

# debug
# print (config)

ATLAS_URI = config.get('ATLAS_URI')

if not ATLAS_URI:
    raise Exception ("'ATLAS_URI' is not set.  Please set it above to continue...")
DB_NAME = 'sample_mflix'
COLLECTION_NAME = 'embedded_movies'


atlas_client = AtlasClient (ATLAS_URI, DB_NAME)
print("Connected to the Mongo Atlas database!")
