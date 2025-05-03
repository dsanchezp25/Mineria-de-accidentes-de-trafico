import json
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

# Eliminar el índice si ya existe 
with open("data/accidentes_trafico_procesado.json", encoding="utf-8") as f:
    data = json.load(f)

for i, doc in enumerate(data):
    es.index(index="accidentes_cataluna", id=i, document=doc)

print("Indexación completa.")
