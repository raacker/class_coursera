from alg_upa_trial import *
from alg_application2_provided import *
from module2_submit import *
from pylab import *
import matplotlib.patches as mpatches
import numpy as np
import random
import math
from time import *

EX_GRAPH0 = {0:set([1,2]), 1:set(), 2:set()}
EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([0]), 
            4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 
            4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1,2]),
            9:set([0,3,4,5,6,7])}


def make_complete_graph(num_nodes):
    """make a undirected graph that fully connected and has num_nodes' vertex"""
    new_graph = {}
    full_number_list = list()

    if num_nodes == 0:
        new_graph = {0:set()}
        return new_graph

    full_number_list = list(range(num_nodes))

    for dummy_index in range(num_nodes):
        new_graph[dummy_index] = set(full_number_list[0:num_nodes])
        new_graph[dummy_index].remove(dummy_index)

    return new_graph

def draw_ER_graph(vertex, probability):
    new_graph = {key: set() for key in xrange(vertex)}
    for index_x in xrange(vertex):
        for index_y in xrange(vertex):
            if index_x != index_y : 
                if random.random() < probability:                
                    new_graph[index_x].add(index_y)   
                    new_graph[index_y].add(index_x)

    return new_graph

def random_order(ugraph):
    key_list = ugraph.keys()
    random.shuffle(key_list)

    return key_list

def UPA(amount_vertex, start_vertex):
    graph = make_complete_graph(start_vertex)
    upa_object = UPATrial(start_vertex)
    for offset in range(start_vertex, amount_vertex):
        adj = upa_object.run_trial(start_vertex)
        graph[offset] = adj
        for adj_offset in adj:
            graph[adj_offset].add(offset)
    return graph

def get_probability(num_of_nodes, num_of_edges):
    return num_of_edges/math.pow(float(num_of_nodes),2.0)

def decreasing(x, y): 
    if x > y: 
        return True

def fast_targeted_order(ugraph):
    degree_set = []
  
    for i in xrange(len(ugraph)):
        degree_set.append(set())
    
    for graph_key in ugraph.keys():
        degree = len(ugraph[graph_key])
        degree_set[degree] |= set([graph_key])

    degree_list = []
    list_len = 0
    offset = len(ugraph)-1

    while offset >= 0:   

        while degree_set[offset] != set():
            u = list(degree_set[offset])[0] 
            degree_set[offset] -= set([u])
            
            if ugraph[u]:
                for adj in ugraph[u]:
                    d = len(ugraph[adj])
                    degree_set[d] -= set([adj])
                    degree_set[d-1] |= set([adj])

                degree_list.append(u)
                list_len += 1 
                delete_node(ugraph,u)    
                
        offset -= 1
   
    degree_list.sort(reverse=True)

    return degree_list

def q1_attack_network(ER_graph, UPA_graph, network_graph, order_function, title_name, pic_name):
    dummy_network_graph = copy_graph(network_graph)
    network_order = order_function(dummy_network_graph) 
    ER_resilience = compute_resilience(ER_graph, network_order)
    UPA_resilience = compute_resilience(UPA_graph, network_order)
    network_resilience = compute_resilience(network_graph, network_order)

    plot(range(len(ER_resilience)), ER_resilience, color='red',label='ER Graph(p = 0.00198)')
    plot(range(len(UPA_resilience)), UPA_resilience, color='blue',label='UPA Graph(m = 2)')
    plot(range(len(network_resilience)), network_resilience, color='green',label='Computer Network')
    
    legend(loc='upper right') 
    title_concat ="Resilience of graph ER_graph, UPA_graph, network_graph\nby " + title_name
    title(title_concat)
    xlabel('Number of removed nodes')
    ylabel('Maximum size of Connected Components on specific nodes')
    picture_location = "./pic/" + pic_name + ".png"
    savefig(picture_location)

def q3_target_order_graph():

    targeted_list = {}
    fast_targeted_list = {}

    for num_of_node in range(10,1000,10):
        UPA_graph = UPA(num_of_node, 5)
        
        start_time = time()
        targeted_max = targeted_order(UPA_graph)
        end_time = time()
        targeted_travel = end_time-start_time
        targeted_list[num_of_node] = targeted_travel
 
        start_time = time()
        fast_targeted_max = fast_targeted_order(UPA_graph)
        end_time = time()
        fast_targeted_travel = end_time-start_time
        fast_targeted_list[num_of_node] = fast_targeted_travel
   
    targeted_y_range = [value for (key,value) in sorted(targeted_list.items())]
    fast_targeted_y_range = [value for (key,value) in sorted(fast_targeted_list.items())]
    x_range = range(10,1000,10)
    plot(x_range, targeted_y_range, color='green', label='targeted_order')
    plot(x_range, fast_targeted_y_range, color='red',label='fast_targeted_order') 
    
    legend(loc='upper right')
    title('Graph of travel time(using time.time() methon in time module)\nfor removing nodes of target/fast target order in UPA graph')
    xlabel('Number of Nodes')
    ylabel('Taken time to compute maximal degree in UPA graph')
    savefig("./pic/question3.png")
        
def main():
    network_graph = load_graph(NETWORK_URL)
    network_len = len(network_graph)
    ER_graph = draw_ER_graph(network_len, 0.00198)
    UPA_graph = UPA(network_len, 2)
    
    q1_attack_network(ER_graph, UPA_graph, network_graph, random_order,"random order", "question1")
    print "Question1 completed"
    cla()
    q3_target_order_graph()
    print "Question3 completed"
    cla()
    q1_attack_network(ER_graph, UPA_graph, network_graph, targeted_order, "targeted order", "question4")
    print "Question4 completed"
    cla()

if __name__ == '__main__':
    main()
#print fast_targeted_order(EX_GRAPH2)
