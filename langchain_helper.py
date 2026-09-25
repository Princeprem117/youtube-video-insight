from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI , OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
import os

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="openai/text-embedding-3-small",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

video_url = "https://www.youtube.com/watch?v=lG7Uxts9SXs"
def create_vectordb_from_yt_url(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url,language=["en","tamil"],
                                            add_video_info=False)
    transcript = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript )
    db = FAISS.from_documents(docs , embeddings)
    return db

def get_response_from_query(db , query, k=4):

    docs = db.similarity_search(query,k=k)
    docs_page_content = "\n".join([doc.page_content for doc in docs])

    llm = ChatOpenAI(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        base_url="https://openrouter.ai/api/v1",api_key=os.getenv("OPENROUTER_API_KEY"),
        temperature=0,
    )

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
        You are a helpful assistant that that can answer questions about youtube videos 
        based on the video's transcript.
        
        Answer the following question: {question}
        By searching the following video transcript: {docs}
        
        Only use the factual information from the transcript to answer the question.
        
        If you feel like you don't have enough information to answer the question, say "I don't know".
        
        Your answers should be verbose and detailed.
        """,
    )

    chain = prompt | llm

    result = chain.invoke({
        "question": query,
        "docs": docs_page_content
    })

    response = result.content

    return response.strip()

db = create_vectordb_from_yt_url(video_url)

response = get_response_from_query(
    db,
    "give the summary in simple and easy to understand way"
)

print(response)