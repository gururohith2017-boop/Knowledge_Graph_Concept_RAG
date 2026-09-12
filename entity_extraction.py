import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load API key from .env
load_dotenv()

# Create LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Read document
with open("sample_document.txt", "r", encoding="utf-8") as file:
    document = file.read()

# Ask the LLM for structured entities
prompt = f"""
Extract the important entities from the document below.

Classify each entity into one of these categories:
PERSON, COMPANY, LOCATION, TECHNOLOGY, DOMAIN, OTHER

Return ONLY this format:

Entity | Type

Document:
{document}
"""

response = llm.invoke(prompt)

print("Structured Entities:")
print(response.content)