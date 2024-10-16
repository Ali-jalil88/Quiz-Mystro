from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.http.models import PointStruct
from langchain.embeddings import OllamaEmbeddings


client = QdrantClient(host='localhost', port=6333)
# Load a pre-trained model from Hugging Face (BERT-based or similar for embeddings)
model = OllamaEmbeddings(model="llama3.2")

# Sample sentences
sentences = [
    "The sky is blue and beautiful.",
    "I love programming in Python.",
    "Artificial intelligence is the future."
]

# Convert sentences to embeddings and then to a NumPy array
sentence_embeddings = model.embed_documents(sentences)
sentence_embeddings = np.array(sentence_embeddings)

client.create_collection(
    collection_name="new_collection_Ollama",
    vectors_config=VectorParams(size=3072, distance=Distance.DOT),
)

points = [
    PointStruct(
        id=i + 1,  # Assign a unique ID to each point
        vector=embedding.tolist()  # Convert embedding to a list for insertion
    )
    for i, embedding in enumerate(sentence_embeddings)  # Loop through embeddings and create PointStruct
]

client.upsert(
    collection_name="new_collection_Ollama",
    points=points  # Insert all points into the collection
)

# Initialize FAISS index
embedding_dimension = sentence_embeddings.shape[1]  # Dimension of embeddings
index = faiss.IndexFlatL2(embedding_dimension)  # L2 similarity measure

# Store embeddings in FAISS index
index.add(sentence_embeddings)

# You can print the number of embeddings stored
print(f"Number of stored embeddings: {index.ntotal}")

# Function to find the most similar sentence
def find_most_similar(query_sentence):
    # Convert the query sentence to an embedding
    query_embedding = model.encode([query_sentence])
    query_embedding = np.array(query_embedding)  # Convert to NumPy array
    
    # Perform a similarity search (finding the nearest neighbor)
    distances, indices = index.search(query_embedding, k=1)  # k=1 to get the closest match
    
    # Return the most similar sentence
    most_similar_sentence = sentences[indices[0][0]]
    return most_similar_sentence

# Test the system with a new query
query = "I enjoy coding in Python."
most_similar = find_most_similar(query)
print(f"Most similar sentence: {most_similar}")
