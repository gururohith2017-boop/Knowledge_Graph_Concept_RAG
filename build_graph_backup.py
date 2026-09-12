import networkx as nx

# Create a directed graph
graph = nx.DiGraph()

# Add nodes
entities = [
    "Ravi",
    "TCS",
    "Chennai",
    "Mumbai",
    "Python",
    "LangChain"
]

graph.add_nodes_from(entities)

# Add relationships
relationships = [
    ("Ravi", "TCS", "WORKS_AT"),
    ("TCS", "Chennai", "HAS_OFFICE_IN"),
    ("TCS", "Mumbai", "HAS_OFFICE_IN"),
    ("Ravi", "Python", "USES"),
    ("Ravi", "LangChain", "USES")
]

for source, target, relationship in relationships:
    graph.add_edge(
        source,
        target,
        relationship=relationship
    )

# Display nodes
print("Nodes:")
for node in graph.nodes:
    print("-", node)

# Display relationships
print("\nRelationships:")
for source, target, data in graph.edges(data=True):
    print(f"{source} --[{data['relationship']}]--> {target}")