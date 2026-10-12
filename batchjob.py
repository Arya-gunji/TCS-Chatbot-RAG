from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import faiss
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore

#step 1 : load tcs report pdf file, store into documents

loaders = PyPDFLoader(
    r"D:\FinalGenAiProject\TcsChatBotProject\documents\tcsreport.pdf"
)

mydocuments = loaders.load()

print("Number of pages:", len(mydocuments))

print(type(mydocuments[0]))

print(mydocuments[1])



# Step 2: Convert documents into smaller chunks

text_splitter = RecursiveCharacterTextSplitter(
    # set a really small chunk size just to show
    chunk_size=2000,
    chunk_overlap=500
)

# Load chunks
mychunks = text_splitter.split_documents(mydocuments)

print("Total chunks:", len(mychunks))

print(mychunks[0])

print(mychunks[0].page_content)

print(mychunks[0].metadata)

#Step 3 : create embedding model
model = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-mpnet-base-v2')

# Step 4: Create FAISS database

index = faiss.IndexFlatL2(len(model.embed_query("hello world")))

vector_store = FAISS(
    embedding_function=model,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={}
)


'''
#step 4 : create faiss db & store documents
vector_store : FAISS.from_documents(documents = mychunks, 
embedding = embeddings, ) '''



# Step 5 : store our chunks into vector database
vector_store.add_documents(mychunks)

print("FAISS database created successfully")

# Step 6 : store vector store [database] permently

vector_store.save_local("tcs_doc_index")
print("successfully stored vector database locally")



'''
from real time python file, if you want to use faiss we need to load faiss.
my_vector_store = FAISS.1oad_1ocal('faiss_index',
emebeddings, 
allow dangerous deserialization=True)
docs = new_vector_store.similarity_search('question') '''
