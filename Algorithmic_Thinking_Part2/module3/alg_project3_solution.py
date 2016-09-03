"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster

######################################################
# Code for closest pairs of clusters


def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters

    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    if len(cluster_list) <= 1:
        return (-1, 0, 0)

    min_point = (float('inf'), -1, -1)

    for index_u in range(len(cluster_list)):
        for index_v in range(len(cluster_list)):
            if index_u != index_v:
                min_point = find_min_point(pair_distance(cluster_list, index_u, index_v), min_point)
    return min_point


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.
    """
    cluster_list.sort(key = lambda cluster: cluster.horiz_center())

    number_of_points = len(cluster_list)
    if number_of_points <= 3:
        min_point = slow_closest_pair(cluster_list)

    else:
        mid_pivot = number_of_points // 2
        left_cluster = cluster_list[:mid_pivot]
        right_cluster = cluster_list[mid_pivot:]

        left_min_point = fast_closest_pair(left_cluster)
        right_min_point = fast_closest_pair(right_cluster)

        min_point = find_min_point(left_min_point, (right_min_point[0], right_min_point[1] + mid_pivot, right_min_point[2] + mid_pivot))
        mid = (cluster_list[mid_pivot-1].horiz_center() + cluster_list[mid_pivot].horiz_center())/2
        min_point = find_min_point(min_point, closest_pair_strip(cluster_list, mid, min_point[0]))

    return min_point


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip

    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.
    """

    clusters = list()
    for iters in range(len(cluster_list)):
        if abs(cluster_list[iters].horiz_center() - horiz_center) < half_width:
            clusters.append(iters)

    clusters.sort(key = lambda index: cluster_list[index].vert_center())

    cluster_length = len(clusters)
    min_point = (float('inf'), -1, -1)
    for index_u in range(cluster_length-1):
        for index_v in range(index_u+1, min(index_u+4, cluster_length)):
            min_point = find_min_point(min_point, pair_distance(cluster_list, clusters[index_u], clusters[index_v]))
    return min_point


def find_min_point(left_point, right_point):
    """
    Find minimum point of given two argument points
    """
    min_point = (lambda left, right: left if left[0] < right[0] else right)(left_point, right_point)
    return min_point

######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list

    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """

    clusters = cluster_list
    while len(clusters) > num_clusters:
        min_cluster_tuple = fast_closest_pair(clusters)
        new_cluster = clusters[min_cluster_tuple[1]].merge_clusters(clusters[min_cluster_tuple[2]])
        del clusters[min_cluster_tuple[2]]
        del clusters[min_cluster_tuple[1]]
        clusters.append(new_cluster)
    return clusters


######################################################################
# Code for k-means clustering


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list

    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations

    temp_cluster = []
    for cluster in cluster_list:
        temp_cluster.append(cluster.copy())

    temp_cluster.sort(key = lambda cluster: cluster.total_population())

    number_of_points = len(cluster_list)
    centers = list()

    iters = 0
    while iters < num_clusters:
        cluster = temp_cluster.pop()
        centers.append([cluster.horiz_center(), cluster.vert_center()])
        iters += 1

    iters = 0
    while iters < num_iterations:
        empty_set = []
        for center_index in range(num_clusters):
            empty_set.append(alg_cluster.Cluster(set(), centers[center_index][0], centers[center_index][1], 0, 0))
        for point_index in range(number_of_points):
            min_dist = float('inf')
            min_index = -1
            for center_index in range(num_clusters):
                dist = euclidean_distance(cluster_list[point_index], centers[center_index])
                if dist < min_dist:
                    min_index = center_index
                    min_dist = dist
            empty_set[min_index] = empty_set[min_index].merge_clusters(cluster_list[point_index])
        for center_index in range(num_clusters):
            centers[center_index][0] = empty_set[center_index].horiz_center()
            centers[center_index][1] = empty_set[center_index].vert_center()
        iters += 1
    return empty_set


def euclidean_distance(left_point, right_point):
    """
    Calculate distance of cluster point and center point
    """
    cur_dist = math.sqrt(pow(left_point.horiz_center() - right_point[0], 2) + pow(left_point.vert_center() - right_point[1], 2))
    return cur_dist
