from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredWordDocumentLoader, PyPDFLoader, CSVLoader




class DocumentChunker:
    def __init__(self, chunk_size=1000, chunk_overlap=100, length_function=len, separators="\n", embeddings=None):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.length_function = length_function
        self.separators = separators
        self.embeddings = embeddings

    def chunk_word_document(self, doc_path):
        doc = UnstructuredWordDocumentLoader(doc_path).load()
        text_splitter = CharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
        chunk = text_splitter.split_documents(doc) #or text_splitter.split_text(text)
        return chunk

    def chunk_pdf(self, doc_path):
        doc = PyPDFLoader(doc_path).load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=self.length_function,
            separators=self.separators
        )
        chunk = text_splitter.split_documents(doc)
        return chunk
    

    def chunk_csv(self, doc_path):
        doc =  CSVLoader(doc_path, csv_args={
        "delimiter": ",",
        
        }).load()


        return doc
    
    def chunk_semantic(self, doc_path):
        if not self.embeddings:
            raise ValueError("Embeddings not provided for semantic chunking.")
        
        doc = UnstructuredWordDocumentLoader(doc_path).load()
        #text_splitter = SemanticChunker(embeddings=self.embeddings)
        #text_splitter.create_documents([doc])
        # You might want to return something meaningful from semantic chunking
        return "Semantic chunking result"