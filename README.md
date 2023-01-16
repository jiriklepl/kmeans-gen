# KMeans data generator

```sh
./kmeans-gen.py --help
```

```text
usage: kmeans-gen [-h] [-s SEED] [-m MAX] [-n POINTS] [-v] [-p] [-r] clusters dimensions

Generate nontrivial test data with unique solution for the k-means algorithm

positional arguments:
  clusters              the number of clusters
  dimensions            the number of dimensions of the space

options:
  -h, --help            show this help message and exit
  -s SEED, --seed SEED  random seed (default: None)
  -m MAX, --max MAX     maximum absolute value for cluster center dimensions (default: 1000)
  -n POINTS, --points POINTS
                        the number of generated points (default: 1000)
  -v, --validate        perform validation (default: False)
  -p, --print_centers   perform validation (default: False)
  -r, --reflections     include a reflection for each sampled point (default: False)

output: csv list of points which should be clustered
```
