#!/usr/bin/env python

import numpy as np
import sklearn.cluster
import sklearn.metrics
import scipy.spatial.distance
import argparse
import csv
import sys

parser = argparse.ArgumentParser(
    prog='kmeans-gen',
    description='Generate nontrivial test data with unique solution for the k-means algorithm',
    epilog='output: csv list of points which should be clustered',
    add_help=True,
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('clusters', type=int, help='the number of clusters')
parser.add_argument('dimensions', type=int, help='the number of dimensions of the space')
parser.add_argument('-s', '--seed',  type=int, default=None, help='random seed')
parser.add_argument('-m', '--max',  type=int, default=1000, help='maximum absolute value for cluster center dimensions')
parser.add_argument('-n', '--points',  type=int, default=1000, help='the number of generated points')
parser.add_argument('-v', '--validate',  action='store_true', default=False, help='perform validation')
parser.add_argument('-p', '--print_centers',  action='store_true', default=False, help='perform validation')
parser.add_argument('-r', '--reflections',  action='store_true', default=False, help='include a reflection for each sampled point')

if __name__=="__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)

    if args.clusters <= 1:
        raise ValueError('the number of clusters has to be greater than 1; given: ' + str(args.clusters))
        exit(1)

    if args.dimensions < 1:
        raise ValueError('the number of dimensions has to be positive; given: ' + str(args.dimensions))

    if args.seed is not None:
        np.random.seed(args.seed)

    centroids = np.random.uniform(low=-args.max, high=args.max, size=(args.clusters, args.dimensions))

    cluster_size = np.min(scipy.spatial.distance.pdist(centroids)) / 2

    distances = np.random.uniform(low=0, high=1, size=args.points) ** (1 / args.dimensions)
    thetas = np.random.normal(size=(args.points, args.dimensions))
    thetas = thetas * (cluster_size * distances / np.maximum(np.sqrt(np.sum(thetas ** 2, axis=-1)), 1e-15)).reshape((thetas.shape[0], 1))
    clusters = np.random.randint(low=0, high=args.clusters, size=args.points)

    points = centroids[clusters] + thetas

    if args.reflections:
        points = np.concatenate([points, centroids[clusters] - thetas], axis=0)

    np.random.shuffle(points)

    if args.print_centers:
        cluster_writer = csv.writer(sys.stderr)
        print('centroids:', file=sys.stderr)
        cluster_writer.writerows(centroids)

    point_writer = csv.writer(sys.stdout)
    point_writer.writerows(points)

    if args.validate:
        print('validation:', file=sys.stderr)

        kmeans = sklearn.cluster.KMeans(n_clusters=args.clusters)
        kmeans.fit(points)

        centroids = np.sort(centroids, axis=0)
        kmeans.cluster_centers_ = np.sort(kmeans.cluster_centers_, axis=0)

        print('rmse: ' + str(sklearn.metrics.mean_squared_error(centroids, kmeans.cluster_centers_, squared=False)), file=sys.stderr)
