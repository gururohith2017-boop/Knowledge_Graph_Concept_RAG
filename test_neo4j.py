import neo4j
from dotenv import load_dotenv
import os

load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")
DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")

driver = neo4j.GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

try:
    driver.verify_connectivity()
    print("SUCCESS: Connected to Neo4j Aura")

    with driver.session(database=DATABASE) as session:
        result = session.run("RETURN 1 AS test")
        print("Database test:", result.single()["test"])

finally:
    driver.close()