from pymongo import MongoClient
import json
import os

# Connect to MongoDB
client = MongoClient("mongodb://root:password@localhost:27017")

# Select the database
db = client['entreprise']

# choose the collection
collection = db['clients']

# Récupérer les fichiers json
path = 'data/data-json/data-json/'
files = os.listdir(path)
print(files)

for file in files:
    if file.endswith('.json'):
        collection = db[file.split('.')[0]]
        # Insert les données depuis le fichier json
        with open(f'data/data-json/data-json/{file}') as f:
            data = json.load(f)
            collection.insert_many(data)
            print(f"Data from {file} inserted")

# Close the connection
client.close()
print("Connexion closed")
print("Done!")