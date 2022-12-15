import networkx  as nx
from typing import NamedTuple

graph = nx.nx_agraph.read_dot("roadmap.dot")
graph.nodes["london"]

class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float