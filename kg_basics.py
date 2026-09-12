# Simple Knowledge Graph example

entities = [
    "Ravi",
    "TCS",
    "Mumbai"
]

relationships = [
    ("Ravi", "WORKS_AT", "TCS"),
    ("TCS", "BASED_IN", "Mumbai")
]

print("Entities:")
for entity in entities:
    print("-", entity)

print("\nRelationships:")
for source, relation, target in relationships:
    print(f"{source} --[{relation}]--> {target}")