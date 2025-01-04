import os 
import cv2
from langchain_community.document_loaders import pyPDFLoader
from langachain.text_splitter import RecursiveCharacterTextSplitter as rcts
from langchain_community import embeddings
from langchain_community import FAISS
from langchain_community import Ollama
import ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain as csdc
loader = pyPDFLoader("file")
docs = loader.load()
text_splitter = rcts(chunk_size = 1000,chunk_overlap = 20)
documents = text_splitter.split_documents(docs)

db = FAISS.from_documents(documents[:30], OllamaEmbeddings)

query = "an attention function can be described as mapping a query "
result = db.similarity_search(query)
result[0].page_content
llm = Ollama(model = "mistral")
prompt = ChatPromptTemplate.from_template('''Answer the following question based only on the provided context. 
Think step by step before providing a detailed answer.  
<context>
{context}
</context>
Question: {input} ''')

document_chain = csdc(llm,prompt)

retriever = db.as_retriever()

