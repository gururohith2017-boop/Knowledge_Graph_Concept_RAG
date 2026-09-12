from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load API key from .env
load_dotenv()

# Create LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Read the document
with open("sample_document.txt", "r", encoding="utf-8") as file:
    document = file.read()

# Ask the LLM to extract relationships
prompt = f"""
Extract the important relationships between entities in the document.

Return ONLY relationships in this format:

Entity 1 | Relationship | Entity 2

Examples:
Ravi | WORKS_AT | TCS
TCS | HAS_OFFICE_IN | Chennai

Document:
{document}
"""

response = llm.invoke(prompt)

print("Extracted Relationships:")
print(response.content)