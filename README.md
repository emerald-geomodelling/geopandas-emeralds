# geopandas-emeralds

Collection of tools for geopandas:

* bounds_distance_matrix - sparse distance matrix between two geoseries (not computing distances for pairs further apart than some max_distance)

This repo requires a patched version of cython_bbox available here: https://github.com/emerald-geomodelling/cython_bbox/tree/sparse (pending merge of [this PR](https://github.com/samson-wang/cython_bbox/pull/7))
