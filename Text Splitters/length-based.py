from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader(file_path='pypdf.pdf')

data = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=' ',
)

result = splitter.split_documents(data)
print(result[0].page_content)
print(result[1].page_content)