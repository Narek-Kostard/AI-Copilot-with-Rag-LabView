from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(url="http://localhost:6333")

client.recreate_collection(
    collection_name="working_collection",
    vectors_config=VectorParams(size=768, distance=Distance.COSINE),
)
