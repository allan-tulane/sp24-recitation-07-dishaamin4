from collections import defaultdict
from heapq import heappush, heappop 

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    def reachable_helper(visited, frontier):
        if len(frontier) == 0:
            return visited
        else:
            node = frontier.pop()
            
            if node in visited:
                return reachable_helper(visited, frontier)
            else:
                visited.add(node)
                neighbors = graph[node] # type set
                for neighbor in neighbors: # iterate the set of neighbors
                    frontier.add(neighbor)
                    
                return reachable_helper(visited, frontier)
        
    visited = set([])
    frontier = set([])
    frontier.add(start_node)
    return reachable_helper(visited, frontier)

def connected(graph):
    reachable_nodes = reachable(graph, list(graph.keys())[0])
    return len(reachable_nodes) == len(graph)

def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    if connected(graph):
        return 1
        
    else:
        neighbor_set=[]
        for node in graph.keys(): # produce reach for every key in graph
            reach_set = reachable(graph, node)
            if reach_set not in neighbor_set: # unique sets of reach will be added to list
                neighbor_set.append(reach_set)

        return len(neighbor_set)
            
