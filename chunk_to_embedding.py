import json
import time
import ollama

from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct



client = QdrantClient(url="http://localhost:6333")

with open('chunk-name.json', 'r', encoding='utf-8') as f:
    chunks = json.load(f)
embeddings = []
for chunk in chunks:
    content = chunk['content']
    result = ollama.embeddings(
        model='nomic-embed-text',
        prompt=content
    )
    operation_info = client.upsert(
        collection_name="working_collection",
        wait=True,
        points=[
            PointStruct(id=chunk['id'], 
                        vector=result['embedding'],
                        payload={"content": chunk['content']}   
            ),
        ],
    )

    

