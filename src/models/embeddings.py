import os
from langchain_google_genai import  GoogleGenerativeAIEmbeddings


embeddings_gemini_pro = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.environ.get("GOOGLE_API_KEY"),
)