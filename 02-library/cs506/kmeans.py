from collections import defaultdict
from math import inf
import random
import csv
from cs506 import sim


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)

    Returns a new point which is the center of all the points.
    """
    if len(points) == 0:
        return []

    average = [0]*(len(points[0]))

    for index, elementP in enumerate(points):
        for i in range(len(elementP)):
            average[i] += elementP[i]

    for index, element in enumerate(average):
        average[index] = element/len(points)

    return average


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    sortedAs = sorted(set(assignments))
    grps = dict()

    for data, task in zip(dataset, assignments):
        grps.setdefault(task, [])
        grps[task].append(data)

    centroids = [point_avg(grps[lbl]) for lbl in sortedAs]
    return centroids


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    return sim.euclidean_dist(a, b)


def distance_squared(a, b):
    return distance(a, b) ** 2


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    centroids = random.sample(list(dataset), k)

    return centroids


def cost_function(clustering):
    all_sum = 0.0
    for cluster in clustering.values():
        centroid = point_avg(cluster)
        dist_vect = [distance(centroid, point) for point in cluster]
        all_sum += sum(dist_vect)
    return all_sum


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    centroids = random.sample(list(dataset), 1)

    while(len(centroids) < k):
        max_d = 0
        max_item = []
        for item in dataset:
            distance = sum([distance_squared(item, centroid)
                           for centroid in centroids])
            if distance > max_d:
                max_d = distance
                max_item = item
        centroids.append(max_item)

    return centroids


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for task, point in zip(assignments, dataset):
        clustering[task].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
