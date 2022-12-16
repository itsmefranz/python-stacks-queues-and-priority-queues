import networkx  as nx
from graph import City, load_graph
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

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

#print(nodes["london"])
#print(graph)
    # City(name='City of London', country='England', year=None, latitude=51.507222, longitude=-0.1275)
    # Graph with 70 nodes and 137 edges

#for neighbor, weights in graph[nodes["london"]].items():
    # print(weights["distance"], neighbor.name)
    # Bath
    # Brighton & Hove
    # Bristol        
    # Cambridge      
    # Canterbury     
    # Chelmsford     
    # Coventry       
    # Oxford
    # Peterborough   
    # Portsmouth     
    # Southampton    
    # Southend-on-Sea
    # St Albans      
    # Westminster    
    # Winchester 

nodes, graph = load_graph("roadmap.dot", City.from_dict)

#for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
    #print(f"{weights['distance']:>3} miles, {neighbor.name}")
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

for node in nx.bfs_tree(graph, nodes["edinburgh"]):
    print("📍", node.name)
    if is_twentieth_century(node.year):
        print("Found:", node.name, node.year)
        break
    else:
        print("Not found")

        #📍 Edinburgh
        #Not found
        #📍 Dundee
        #Not found
        #📍 Glasgow
        #Not found
        #📍 Perth
        #Not found
        #📍 Stirling
        #Not found
        #📍 Carlisle
        #Not found
        #📍 Newcastle upon Tyne
        #Not found
        #📍 Aberdeen
        #Not found
        #📍 Inverness
        #Not found
        #📍 Lancaster
        #Found: Lancaster 1937 