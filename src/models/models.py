import os
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory
)

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=os.environ.get("GOOGLE_API_KEY") or "AIzaSyDtMlbtG6HhOSeJeoMxabLsJ0piFQC_PwA",
    max_output_tokens=8192,
    convert_system_message_to_human=False,
    verbose=False,
    safety_settings={
      HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }
)
