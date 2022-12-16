import networkx  as nx
from typing import NamedTuple

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

nodes, graph = load_graph("roadmap.dot", City.from_dict)
# print(nodes["london"])
# print(graph)
    # City(name='City of London', country='England', year=None, latitude=51.507222, longitude=-0.1275)
    # Graph with 70 nodes and 137 edges

for neighbor, weights in graph[nodes["london"]].items():
    print(weights["distance"], neighbor.name)
    #Bath
    #Brighton & Hove
    #Bristol        
    #Cambridge      
    #Canterbury     
    #Chelmsford     
    #Coventry       
    #Oxford
    #Peterborough   
    #Portsmouth     
    #Southampton    
    #Southend-on-Sea
    #St Albans      
    #Westminster    
    #Winchester 