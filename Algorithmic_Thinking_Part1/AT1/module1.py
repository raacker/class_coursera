"""graph with dictionary about in-degree distribution"""

EX_GRAPH0 = {0:set([1,2]), 1:set(), 2:set()}
EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([0]), 
            4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 
            4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1,2]),
            9:set([0,3,4,5,6,7])}

EX_GRAPH3 = {0:set([1,2,3]), 1:set([]), 2:set([]), 3:set([])}
def make_complete_graph(num_nodes):
    """make a directed graph that fully connected and has num_nodes' vertex"""
    new_graph = {}
    full_number_list = list()

    if num_nodes == 0:
        new_graph = {0:set()}
        return new_graph

    for dummy_index in range(0, num_nodes):
        full_number_list.append(dummy_index)

    for dummy_index in range(0, num_nodes):
        new_graph[dummy_index] = set(full_number_list[0:num_nodes])
        new_graph[dummy_index].remove(dummy_index)

    return new_graph

def compute_in_degrees(digraph):
    """count each vertexs' in-degree edges of digraph"""
    indegree_list = {}
    
    for dummy_index in digraph:
        indegree_list[dummy_index] = 0

    for dummy_index in digraph: 
        for edges in digraph[dummy_index]:
            indegree_list[edges] += 1
 
    return indegree_list
    
def in_degree_distribution(digraph): 
    """evaluate distribution of in-degree of digraph's nodes"""
    indegree_graph= compute_in_degrees(digraph)
    
    distribution_graph = {}

    for dummy_index in indegree_graph:
        if indegree_graph[dummy_index] in distribution_graph:
            distribution_graph[indegree_graph[dummy_index]] += 1
        else:
            distribution_graph[indegree_graph[dummy_index]] = 1

    return distribution_graph


print in_degree_distribution(EX_GRAPH3)
