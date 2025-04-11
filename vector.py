import chromadb 
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
def store_in_vector_db(analyzed_data):
    client = chromadb.Client()

    collection = client.get_or_create_collection("cve_analysis")

    documents = []
    metadatas = []
    ids = []
    
    for category, cves in analyzed_data.items():
        for cve_id, details in cves.items():
            doc = f"CVE: {cve_id}, Risk: {details.get('Risk Assessment', 'N/A')}, Action: {details.get('Action', 'N/A')}"
            metadata = {"category": category, "cve_id": cve_id}
        documents.append(doc)
        metadatas.append(metadata)
        ids.append(cve_id)
    embed= model.encode(documents)
    collection.upsert(
        documents=documents,
        embeddings=embed,
        metadatas=metadatas,
        ids=ids
    )
    return collection

def query_vector_db(collection, query_text):
    query_embedding = model.encode([query_text])
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=5  
    )
    return results['documents'][0] 

