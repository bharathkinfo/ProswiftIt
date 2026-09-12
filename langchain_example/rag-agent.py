from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

loader = PyPDFLoader(
    "week2 Tasks.pdf"
)
document = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 800,
    chunk_overlap = 25
)
chunk = splitter.split_documents(
    document
)

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=chunk,
    embedding=embeddings,
    collection_name="week2_tasks"
)
retriever = vectorstore.as_retriever(
    search_kwargs={
        "k" : 3
    }
)

results = retriever.invoke(
    "FastAPI & API Development"
)

# results = vectorstore.similarity_search(
#     "what are the python Fundamentals in Day1",
#     k = 3
# )

for rank,doc in enumerate(results, start=1):
    print(f"\nRank Order of Similarlity", {rank})
    print(doc.page_content)
    print("!@#$%^&*()@#$%^&*()@#$%^&*()!@#$%^&*()")

# chunk_vector = embeddings.embed_query(
#     chunk[0].page_content
# )
# print(chunk_vector)
# print(len(chunk_vector))


#===========================================
# vector = embeddings.embed_query(
#     "Helloworld, Agent AI"
# )
# print(vector)
# print(len(vector))
# print(chunk[0].page_content)
# print(chunk[0].metadata)
# print("Documents : ",len(document))
# print("Chunks : ",len(chunk))
# print(document[0])
# print(document[0].page_content)
# print(document[0].metadata)
#================================================