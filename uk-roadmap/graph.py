import networkx  as nx
from typing import NamedTuple
from queues import Queue

class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]) or None,
            latitude=float(attrs["latitude"]),
            longitude=float(attrs["longitude"]),
        )

def load_graph(filename, node_factory):
    graph = nx.nx_agraph.read_dot(filename)
    nodes = {
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data=True)
    }

    return nodes, nx.Graph(
        (nodes[name1], nodes[name2], weights)
        for name1, name2, weights in graph.edges(data=True)
    )

def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

def order(neighbors):
    def by_latitude(city):
        return city.latitude
    return iter(sorted(neighbors, key=by_latitude, reverse=True))

def breadth_first_traverse(graph, source):
    queue = Queue(source)
    visited = {source}
    while queue:
        yield (node := queue.dequeue())
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

nodes, graph = load_graph("roadmap.dot", City.from_dict)

# READING DOT FILE TEST
#graph = nx.nx_agraph.read_dot("roadmap.dot")
#print(graph.nodes["london"])

# NEIGHBORS IDENTIFIER TEST
# for neighbor in graph.neighbors(nodes["london"]):
#     print(neighbor.name)

# NEIGHBOR WITH NODES WEIGHTS TEST 
#for neighbor, weights in graph[nodes["london"]].items():
    # print(weights["distance"], neighbor.name)

# SORT NEIGHBOR WITH NODES WEIGHTS TEST
#for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    #print(f"{weights['distance']:>3} miles, {neighbor.name}")


# BREADTH FIRST SEARCH FOR 20TH CENTURY CITY
for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
    else:
         print("Not found")
