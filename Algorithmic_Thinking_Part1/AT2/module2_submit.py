"""Project for BFS Algorithm and Resilience of Graph"""
from collections import deque

EX_GRAPH0 = {0:set([1,2]), 1:set(), 2:set()}
EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([0]), 
            4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 
            4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1,2]),
            9:set([0,3,4,5,6,7])}


def bfs_visited(ugraph, start_node):
    """Breath-First Search Algorithm on ugraph. Start from start_node"""
    queue = deque()
    visited = set([start_node])
    
    queue.append(start_node)

    while len(queue) != 0:
        popped = queue.pop()

        if (ugraph[popped] - visited) != set([]):
            left_set = ugraph[popped] - visited
            for adj_element in left_set:
                queue.append(adj_element)
            visited |= left_set

    return visited

def cc_visited(ugraph):
    """Find Connected Components of ugraph"""

    remaining_nodes = dict([(pair[0], set(pair[1])) for pair in ugraph.items()])

    connected_components = []
    
    while len(remaining_nodes) != 0:
        visiting_node = 0
        
        for remain_key in remaining_nodes.keys():
            visiting_node = remain_key
            break
       
        visited = bfs_visited(remaining_nodes, visiting_node)
        connected_components.append(visited)

        for iter_value in remaining_nodes.values():
            iter_value -= visited

        for visited_element in visited:
            if visited_element in remaining_nodes:
                del remaining_nodes[visited_element]
        
    return connected_components
    
def largest_cc_size(ugraph):
    """Return largest connected Components size"""
     
    connected_components = cc_visited(ugraph)
    
    max_len = 0

    if connected_components:
        max_len = len(connected_components[0])
        for offset_cc in connected_components: 
            max_len = max(max_len, len(offset_cc)) 

    return max_len

def compute_resilience(ugraph, attack_order):
    """Computer Resilience of ugraph by given attack_order"""
    ugraph = dict([(pair[0], set(pair[1])) for pair in ugraph.items()])
    resilience_list = []

    resilience_list.append(largest_cc_size(ugraph))
    for attack_node in attack_order:
        if attack_node in ugraph:
            for graph_value in ugraph.values():
                if attack_node in graph_value:
                    graph_value.remove(attack_node)
            del ugraph[attack_node]

            resilience_list.append(largest_cc_size(ugraph))        
    
    return resilience_list
