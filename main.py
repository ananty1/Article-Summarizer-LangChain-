import os
import streamlit as st
import time
import pickle

from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_cohere import CohereRerank
from langchain_community.llms import Cohere
from langchain.chains import RetrievalQA

cohere_api_key = st.secrets["COHERE_API_KEY"]

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
    }
    .main {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }
    .stSidebar {
        background-color: #2c3e50;
    }
    .stSidebar h1 {
        color: white;
    }
    .stButton>button {
        background-color: #2980b9;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #1f5f7a;
    }
    h1, h2 {
        color: #2980b9;
    }
    .stTextInput>div>div>input {
        border: 1px solid #2980b9;
        border-radius: 5px;
        padding: 0.5rem;
    }
    .stTextInput>div>div>input:focus {
        border: 1px solid #1f5f7a;
        outline: none;
        box-shadow: 0 0 5px rgba(41, 128, 185, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True
)



st.title("Article Summarizer")

st.sidebar.title("Article URLs")
urls = [st.sidebar.text_input(f"URL {i+1}") for i in range(3)]

def pretty_print_docs(docs):
    print(
        f"\n{'-' * 100}\n".join(
            [f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]
        )
    )


process_url_clicked = st.sidebar.button("Process URLs")

main_placefolder = st.empty()
# llm = Cohere(temperature=0)
compressor = CohereRerank(model="rerank-english-v3.0")
# compression_retriever = None

# Initialize session state for retriever
if 'compression_retriever' not in st.session_state:
    st.session_state.compression_retriever = None


if process_url_clicked:
    loader = UnstructuredURLLoader(urls=urls)
    main_placefolder.text("Data Loading... Started ....")

    data = loader.load()

    # Splitting the data
    main_placefolder.text("Text Splitter... Started ....")
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=400
    )

    docs = text_splitter.split_documents(data)

    retriever = FAISS.from_documents(
        docs, CohereEmbeddings(model="embed-english-v3.0")
    ).as_retriever(search_kwargs={"k": 2})


    st.session_state.compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=retriever
    )
    

    # with open("retriever_pkl.pkl", "wb") as file:
    #     pickle.dump(compression_retriever, file)
    # Create embeddings
    # embeddings = CohereEmbeddings(model="embed-english-v3.0")
    # documents_with_embeddings = embeddings.embed_documents(docs)

    # Initialize Cohere Retriever
    # retriever = CohereRagRetriever.from_documents(documents_with_embeddings)
    main_placefolder.text("Done Loading... Started ....")
    # main_placefolder.text("Embeddings and Retriever Setup Completed.")
    time.sleep(2)

query = main_placefolder.text_input("Question")
if query:
    if st.session_state.compression_retriever is None:
            st.error("Please process the URLs first.")

    else:
        try:
            # Create the retrieval chain
            chain = RetrievalQA.from_chain_type(
                llm=Cohere(temperature=0.8), retriever=st.session_state.compression_retriever
            )
            result = chain({"query": query})

            # Display the result
            st.markdown(f"**Query:** {query}")
            st.markdown(f"**Result:**\n\n{result['result']}")  # A
        except Exception as e:
            st.error(f"Error processing query: {str(e)}")
   
#  Optional: to clear the retriever and quit
if st.sidebar.button("Quit"):
    st.session_state.compression_retriever = None
    st.sidebar.text("Retriever cleared. Session ended.")


st.markdown(
    """
    ## How to Use

    1. **Enter URLs**: Use the sidebar to input up to three URLs of news articles you want to summarize.
    2. **Process URLs**: Click the "Process URLs" button to start the data processing. This will:
       - Load and parse the articles from the provided URLs.
       - Split the text into manageable chunks.
       - Create embeddings and build a retriever for querying.
    3. **Ask Questions**: Once the URLs are processed, enter your question in the "Question" field and hit Enter to get a summary of the articles relevant to your query.
    4. **View Results**: The summary will be displayed below the question input field.

    **Note**: Make sure to process the URLs before asking questions. If you try to query without processing, you will receive an error.

    ## Documentation

    For more information on how the summarizer works, refer to the official [Langchain Documentation](https://python.langchain.com/v0.2/docs/integrations/retrievers/cohere/) and the [Cohere Documentation](https://cohere.ai/). These resources provide detailed explanations of the models and techniques used in this application.
    """
)