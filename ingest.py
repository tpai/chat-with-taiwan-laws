from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import DirectoryLoader, PyPDFLoader

# Initialize a DirectoryLoader with the specified path and file type
loader = DirectoryLoader('./docs', glob="**/*.pdf", loader_cls=PyPDFLoader)
# Load and split the documents into pages
pages = loader.load_and_split()
# Initialize OpenAIEmbeddings for generating embeddings
embeddings = OpenAIEmbeddings()
# Create a FAISS index from the documents using the embeddings
db = FAISS.from_documents(pages, embeddings)
# Save the FAISS index locally
db.save_local("faiss_index")
