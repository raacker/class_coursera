"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib2
from pylab import *
import numpy as np
import alg_dpa_trial
import random
# Set timeout for CodeSkulptor if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

"""graph with dictionary about in-degree distribution"""

def make_complete_graph(num_nodes):
    """
    make a directed graph that fully connected and has num_nodes' vertex
    """
    
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

    return {key: value for key, value in distribution_graph.iteritems() if value > 0}

def nomalize_graph(digraph):
    total = 0
    for dummy_index in digraph:
        total += digraph[dummy_index]
 
    total *= 1.0
    return {degree: indegree_num/total for degree, indegree_num in digraph.iteritems()}

def draw_loglog_graph_of_in_degree(digraph, graph_title):  
    in_degree_graph = in_degree_distribution(digraph)
    result = nomalize_graph(in_degree_graph)

    cite_list_x = []
    cite_list_y = []

    for graph_key, graph_value in result.iteritems(): 
        cite_list_x.append(graph_key)
        cite_list_y.append(graph_value)

    lines = plot(cite_list_x, cite_list_y, 'bo', ms=2.0)
    loglog()
    setp(lines, 'marker', 'o')
    title('In-degree distribution loglog graph of %s' % graph_title)
    xlabel('In-degree Quantity')
    ylabel('Distributions')
    show()

def draw_ER_graph(vertex, probability):
    new_graph = {}
    for index_x in range(0, vertex):
        for index_y in range(0, vertex):
            if index_x != index_y : 
                if random.random() < probability:
                    if index_x in new_graph:
                        new_graph[index_x].append(index_y)
                    else :
                        new_graph[index_x] = []
                        new_graph[index_x].append(index_y)
    return new_graph

def in_degree_counter(a_set):
    total_num = 0
    set_list = list(a_set)
    
    for offset_in in set_list:
        total_num += offset_in

    return total_num


def DPA_algorithm(amount_vertex, start_vertex):
    graph = make_complete_graph(start_vertex)

    num_of_vertex_list = [offset for offset in range(0, start_vertex) for dummy_index in range(0, start_vertex)]
    num_of_vertex = start_vertex
    for iter_index in range(start_vertex, amount_vertex-1):
        vertex_list = set()
        indegree_of_graph = compute_in_degrees(graph)
        total_indegree = 0
        for dummy_index in indegree_of_graph:
            total_indegree += indegree_of_graph[dummy_index]

        for m_offset in range(0, start_vertex): 
            vertex_list.add(random.choice(num_of_vertex_list))

        num_of_vertex_list.append(num_of_vertex)
        num_of_vertex += 1
        graph[iter_index] = vertex_list

    return graph

def in_degree_amount_of_graph(original_graph):
    total = 0
    for dummy_index in original_graph:
        total += graph[dummy_index]
    return total

def out_degree_average_of_graph(graph):
    total = 0
    for dummy_index in graph:
        temp_set = graph[dummy_index]
        temp_list = list(temp_set)
        for list_offset in temp_list:
            total += 1
    
    total /= len(graph)
    return total

def DPA(amount_vertex, start_vertex):
    graph = make_complete_graph(start_vertex)
    dpa_object = alg_dpa_trial.DPATrial(start_vertex)
    for offset in range(start_vertex, amount_vertex):
        graph[offset] = dpa_object.run_trial(start_vertex)
    return graph

#draw_loglog_graph_of_in_degree(load_graph(CITATION_URL), "Energy Physics Theory Papers")
#draw_loglog_graph_of_in_degree(draw_ER_graph(1000, 0.1), "ER Algorithm")
#print DPA_algorithm(1000,13)
average_number =  out_degree_average_of_graph(load_graph(CITATION_URL))
print average_number
draw_loglog_graph_of_in_degree((DPA(27770, average_number)), "DPA Algorithm")
