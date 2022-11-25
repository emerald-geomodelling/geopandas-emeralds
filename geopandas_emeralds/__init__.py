import cython_bbox
import pandas as pd
import scipy.sparse

def bounds_distance_matrix(a, b, max_distance, output_type="dok_matrix"):
    abounds = a.bounds
    bbounds = b.bounds

    abounds["minx"] -= max_distance
    abounds["miny"] -= max_distance
    abounds["maxx"] += max_distance
    abounds["maxy"] += max_distance

    bbounds["minx"] -= max_distance
    bbounds["miny"] -= max_distance
    bbounds["maxx"] += max_distance
    bbounds["maxy"] += max_distance

    distancem = cython_bbox.bbox_overlaps(abounds.values, bbounds.values, True)
    close_enough = pd.DataFrame(distancem.keys(), columns=["i", "j"])

    close_enough_a = a[close_enough.i.values]
    close_enough_b = b[close_enough.j.values]

    distances = close_enough_a.distance(close_enough_b, align=False).values

    res = pd.DataFrame({
        "i": close_enough.i,
        "j": close_enough.j,
        "v": distances})

    if output_type == "ndarray":
        return mres.to_records(index=False)
    
    mres = scipy.sparse.dok_matrix((len(a), len(b)), float)
    mres._update(zip(list(res[["i", "j"]].itertuples(index=False, name=None)), res["v"]))
        
    if output_type == "coo_matrix":
        return mres.tocoo()
    elif output_type == "dict":
        return dict(zip(mres.keys(), mres.values()))
    
    return mres
