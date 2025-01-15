import matplotlib.pyplot as plt
import networkx as nx

# Create the map as a graph
G = nx.Graph()

# Define locations and connections
locations = {
    "Hollow Plaza": (0, 0),
    "Rusted Spire": (-2, 4),
    "Bleeding Market": (3, 3),
    "Iron Chapel": (-3, -3),
    "Infernal Rails": (4, -4),
    "Abyssal Gears Tavern": (1, -2),
    "Cogwrights' Foundry": (-4, 2),
    "Hollow Streets Entrance": (-1, 1),
}

connections = [
    ("Hollow Plaza", "Rusted Spire"),
    ("Hollow Plaza", "Bleeding Market"),
    ("Hollow Plaza", "Abyssal Gears Tavern"),
    ("Hollow Plaza", "Hollow Streets Entrance"),
    ("Rusted Spire", "Cogwrights' Foundry"),
    ("Bleeding Market", "Infernal Rails"),
    ("Iron Chapel", "Abyssal Gears Tavern"),
    ("Iron Chapel", "Hollow Streets Entrance"),
    ("Hollow Streets Entrance", "Cogwrights' Foundry"),
]

# Add nodes and edges to the graph
for location, pos in locations.items():
    G.add_node(location, pos=pos)

for connection in connections:
    G.add_edge(*connection)

# Extract positions for plotting
positions = nx.get_node_attributes(G, 'pos')

# Plot the map
plt.figure(figsize=(10, 10))
nx.draw(
    G, 
    pos=positions, 
    with_labels=True, 
    node_size=3000, 
    node_color="lightcoral", 
    font_size=10, 
    font_weight="bold",
    edge_color="black",
    linewidths=1.5
)

plt.title("Map of Ashvale", fontsize=16, fontweight="bold")
plt.show()
