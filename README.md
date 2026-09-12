planned pipeline is correct:

Document → Entity Extraction → Relationship Mapping → Graph Storage → Graph Query → RAG Answer

And we’ll implement graph storage in this order:

Neo4j Aura first ☁️
NetworkX second 🐍

Our learning approach

We’ll use Python + LangChain, and at each step you will run the code and verify the output before we move on.

Step	What we'll learn
1	Create project + virtual environment
2	Install required packages
3	Load a small document
4	Extract entities
5	Create relationships
6	Understand the Knowledge Graph structure
7	Connect to Neo4j Aura
8	Store entities/relationships in Neo4j
9	Run graph queries
10	Connect graph retrieval with LangChain RAG
11	Build the complete KG-RAG application
12	Rebuild the same graph using NetworkX


------------------------------------------
Our learning pipeline is now:
------------------------------------
sample_document.txt
        ↓
Entity Extraction
        ↓
7 entities
        ↓
Relationship Extraction
        ↓
5 relationships
        ↓
Python
        ↓
Neo4j Aura
        ↓
Knowledge Graph ✅