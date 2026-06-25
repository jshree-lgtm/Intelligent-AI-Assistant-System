import os
import xml.etree.ElementTree as ET
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
MEDQUAD_PATH = "data/medquad"
INDEX_PATH = "medical_db/medical_index.bin"
METADATA_PATH = "medical_db/medical_metadata.pkl"
os.makedirs(
    "medical_db",
    exist_ok=True
)
embedder = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
documents = []
for root, dirs, files in os.walk(
    MEDQUAD_PATH
):
    for file in files:
        if file.endswith(".xml"):
            filepath = os.path.join(
                root,
                file
            )
            try:
                tree = ET.parse(
                    filepath
                )
                root_xml = tree.getroot()
                for qa in root_xml.findall(
                    ".//QAPair"
                ):
                    question = qa.findtext(
                        "Question"
                    )
                    answer = qa.findtext(
                        "Answer"
                    )
                    if (
                        question
                        and answer
                    ):
                        documents.append(
                            {
                                "question": question,
                                "answer": answer
                            }
                        )
            except Exception as e:
                print(
                    "Error:",
                    filepath,
                    e
                )
print(
    f"Loaded {len(documents)} QA pairs"
)
texts = []
for doc in documents:
    texts.append(
        doc["question"]
    )
embeddings = embedder.encode(
    texts,
    show_progress_bar=True
)
embeddings = np.array(
    embeddings,
    dtype="float32"
)
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(
    dimension
)
index.add(
    embeddings
)
faiss.write_index(
    index,
    INDEX_PATH
)
with open(
    METADATA_PATH,
    "wb"
) as f:
    pickle.dump(
        documents,
        f
    )
print(
    "Medical Vector DB Created Successfully!"
)