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

def sort_by(neighbors, strategy):
    return sorted(neighbors.items(), key=lambda item: strategy(item[1]))

def by_distance(weights):
    return float(weights["distance"])

# print(nodes["london"])
# print(graph)
    # City(name='City of London', country='England', year=None, latitude=51.507222, longitude=-0.1275)
    # Graph with 70 nodes and 137 edges

#for neighbor, weights in graph[nodes["london"]].items():
    #print(weights["distance"], neighbor.name)
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

nodes, graph = load_graph("roadmap.dot", City.from_dict)

for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    print(f"{weights['distance']:>3} miles, {neighbor.name}")
    # 1 miles, Westminster
    # 25 miles, St Albans      
    #  40 miles, Chelmsford     
    # 42 miles, Southend-on-Sea
    # 53 miles, Brighton & Hove
    # 58 miles, Oxford
    # 61 miles, Cambridge      
    # 62 miles, Canterbury     
    # 68 miles, Winchester     
    # 75 miles, Portsmouth     
    # 79 miles, Southampton    
    # 85 miles, Peterborough   
    # 100 miles, Coventry       
    # 115 miles, Bath
    # 118 miles, Bristol   