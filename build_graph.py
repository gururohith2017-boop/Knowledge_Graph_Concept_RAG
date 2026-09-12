from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

entities = [
    "Ravi",
    "TCS",
    "Chennai",
    "Mumbai",
    "Python",
    "LangChain"
]

relationships = [
    ("Ravi", "TCS", "WORKS_AT"),
    ("TCS", "Chennai", "HAS_OFFICE_IN"),
    ("TCS", "Mumbai", "HAS_OFFICE_IN"),
    ("Ravi", "Python", "USES"),
    ("Ravi", "LangChain", "USES")
]


def create_graph(tx):
    for entity in entities:
        tx.run(
            "MERGE (n:Entity {name: $name})",
            name=entity
        )

    for source, target, relationship in relationships:
        tx.run(
            """
            MATCH (a:Entity {name: $source})
            MATCH (b:Entity {name: $target})
            MERGE (a)-[r:RELATED {type: $relationship}]->(b)
            """,
            source=source,
            target=target,
            relationship=relationship
        )


try:
    driver.verify_connectivity()
    print("SUCCESS: Connected to Neo4j Aura")

    with driver.session(database=DATABASE) as session:
        session.execute_write(create_graph)

    print("SUCCESS: Graph created in Neo4j Aura")

finally:
    driver.close()