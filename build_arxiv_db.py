import json
import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

# Paths
ARXIV_FILE = "data/arxiv/arxiv-metadata-oai-snapshot.json"

INDEX_PATH = "vector_db/faiss_index.bin"
METADATA_PATH = "vector_db/metadata.pkl"

# Load embedding model
embedder = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

documents = []

print("Reading arXiv papers...")

with open(
    ARXIV_FILE,
    "r",
    encoding="utf-8"
) as f:

    count = 0

    for line in f:

        try:

            paper = json.loads(line)

            categories = paper.get(
                "categories",
                ""
            )

            # Only Computer Science papers
            if "cs." in categories:

                title = paper.get(
                    "title",
                    ""
                )

                abstract = paper.get(
                    "abstract",
                    ""
                )

                text = f"""
Title:
{title}

Abstract:
{abstract}
"""

                documents.append(text)

                count += 1

                # Take first 1000 papers
                if count >= 1000:
                    break

        except:
            continue

print(
    f"Loaded {len(documents)} papers"
)

# Create embeddings

print(
    "Generating embeddings..."
)

embeddings = embedder.encode(
    documents,
    show_progress_bar=True
)

embeddings = np.array(
    embeddings,
    dtype="float32"
)

# Create FAISS index

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(
    embeddings
)

# Save index

faiss.write_index(
    index,
    INDEX_PATH
)

# Save metadata

with open(
    METADATA_PATH,
    "wb"
) as f:

    pickle.dump(
        documents,
        f
    )

print(
    "arXiv vector database created successfully!"
)