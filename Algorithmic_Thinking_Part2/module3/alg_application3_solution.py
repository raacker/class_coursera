import random
import alg_cluster
import matplotlib.pyplot as plt
# import alg_clusters_matplotlib
from alg_project3_viz import *
from alg_project3_solution import *
from time import *
import copy

def gen_random_clusters(num_clusters):
    clusters = []
    for iters in range(num_clusters):
        clusters.append(alg_cluster.Cluster(set(), random.randrange(-1000000,1000000)/1000000, random.randrange(-1000000,1000000)/1000000,0,0))

    return clusters


def question1():

    slow_count = list()
    fast_count = list()

    for i in xrange(199):
        clusters = gen_random_clusters(i+2)

        start_time = time()
        slow_closest_pair(clusters)
        end_time = time()

        slow_count.append(end_time - start_time)

        start_time = time()
        fast_closest_pair(clusters)
        end_time = time()

        fast_count.append(end_time - start_time)

    x_range = xrange(199)
    plt.plot(x_range, slow_count, color='green', label='slow_closest_pair')
    plt.plot(x_range, fast_count, color='red', label='fast_closest_pair')
    plt.legend(loc='upper right')
    plt.title('Graph of measuring time of slow_closest_pair and fast_closest_pair\nat random clusters')
    plt.xlabel('Amount of clusters')
    plt.ylabel('Taken time to find closest pair')
    plt.show()

def compute_distortion(cluster_list, data_table):
    distortion = 0
    for cluster in cluster_list:
        distortion += cluster.cluster_error(data_table)
    return distortion

def question7():
    data_table = load_data_table(DATA_290_URL)

    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

    singleton_list_copy = copy.deepcopy(singleton_list)
    hierarchical_list = alg_project3_solution.hierarchical_clustering(singleton_list, 16)
    print "Displaying", len(hierarchical_list), "hierarchical_clustering"

    kmean_list = alg_project3_solution.kmeans_clustering(singleton_list_copy, 16, 5)
    print "Displaying", len(kmean_list), "kmeans_clustering"

    print "Distortion of hierarchical_clustering : ", compute_distortion(hierarchical_list, data_table)
    print "Distortion of kmeans_clustering : ", compute_distortion(kmean_list, data_table)

def question10_111():
    data_table_111 = load_data_table(DATA_111_URL)
    singleton_list_111 = generate_singleton_list(data_table_111)
    result_hierarchial_111 = []
    result_kmean_111 = []

    for index_x in range(6,21):
        singleton_list_111_copy = copy.deepcopy(singleton_list_111)
        hierarchical_list = alg_project3_solution.hierarchical_clustering(singleton_list_111_copy, index_x)
        result_hierarchial_111.append(compute_distortion(hierarchical_list, data_table_111))

        singleton_list_111_copy = copy.deepcopy(singleton_list_111)
        kmean_list = alg_project3_solution.kmeans_clustering(singleton_list_111_copy, index_x, 5)
        result_kmean_111.append(compute_distortion(kmean_list, data_table_111))

    x_range = range(6,21)
    plt.plot(x_range, result_hierarchial_111, color='green', label='Hierarchical Clustering on 111 Data')
    plt.plot(x_range, result_kmean_111, color='red', label='KMean Clustering on 111 Data')

    plt.legend(loc='upper right')
    plt.title('Graph of distortion of Hierarchial Clustering and KMean Clustering\non 111 Data Set')
    plt.xlabel('Amount of clusters')
    plt.ylabel('Amount of distortions')
    plt.show()

def question10_290():

    data_table_290 = load_data_table(DATA_290_URL)
    singleton_list_290 = generate_singleton_list(data_table_290)
    result_hierarchial_290 = []
    result_kmean_290 = []

    for index_x in range(6,21):
        singleton_list_290_copy = copy.deepcopy(singleton_list_290)
        hierarchical_list = alg_project3_solution.hierarchical_clustering(singleton_list_290_copy, index_x)
        result_hierarchial_290.append(compute_distortion(hierarchical_list, data_table_290))

        singleton_list_290_copy = copy.deepcopy(singleton_list_290)
        kmean_list = alg_project3_solution.kmeans_clustering(singleton_list_290_copy, index_x, 5)
        result_kmean_290.append(compute_distortion(kmean_list, data_table_290))

    x_range = range(6,21)
    plt.plot(x_range, result_hierarchial_290, color='green', label='Hierarchical Clustering on 290 Data')
    plt.plot(x_range, result_kmean_290, color='red', label='KMean Clustering on 290 Data')

    plt.legend(loc='upper right')
    plt.title('Graph of distortion of Hierarchial Clustering and KMean Clustering\non 290 Data Set')
    plt.xlabel('Amount of clusters')
    plt.ylabel('Amount of distortions')
    plt.show()

def question10_896():

    data_table_896 = load_data_table(DATA_896_URL)
    singleton_list_896 = generate_singleton_list(data_table_896)
    result_hierarchial_896 = []
    result_kmean_896 = []

    for index_x in range(6,21):
        singleton_list_896_copy = copy.deepcopy(singleton_list_896)
        hierarchical_list = alg_project3_solution.hierarchical_clustering(singleton_list_896_copy, index_x)
        result_hierarchial_896.append(compute_distortion(hierarchical_list, data_table_896))

        singleton_list_896_copy = copy.deepcopy(singleton_list_896)
        kmean_list = alg_project3_solution.kmeans_clustering(singleton_list_896_copy, index_x, 5)
        result_kmean_896.append(compute_distortion(kmean_list, data_table_896))

    x_range = range(6,21)

    plt.plot(x_range, result_hierarchial_896, color='green', label='Hierarchical Clustering on 896 Data')
    plt.plot(x_range, result_kmean_896, color='red', label='KMean Clustering on 896 Data')

    plt.legend(loc='upper right')
    plt.title('Graph of distortion of Hierarchial Clustering and KMean Clustering\non 896 Data Set')
    plt.xlabel('Amount of clusters')
    plt.ylabel('Amount of distortions')
    plt.show()

def generate_singleton_list(data_table):
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
    return singleton_list

question7()
#question10_111()
#question10_290()
#question10_896()
