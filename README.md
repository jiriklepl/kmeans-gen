# KMeans data generator

```sh
./kmeans-gen.py -h
```

```text
usage: kmeans-gen [-h] [-s SEED] [-m MAX] [-n POINTS] [-v] [-p] [-r] clusters dimensions

Generate nontrivial test data with unique solution for the k-means algorithm

positional arguments:
  clusters              the number of clusters
  dimensions            the number of dimensions of the space

options:
  -h, --help            show this help message and exit
  -s SEED, --seed SEED  random seed
  -m MAX, --max MAX     maximum absolute value for cluster center dimensions
  -n POINTS, --points POINTS
                        the number of generated points
  -v, --validate        perform validation
  -p, --print_centers   perform validation
  -r, --reflections     include a reflection for each sampled point

output: csv list of points which should be clustered
```
