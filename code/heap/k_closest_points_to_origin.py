def find_k_closest_points_to_origin(points, k):
    def dist(p):
        return p[0] ** 2 + p[1] ** 2

    return sorted(points, key=dist)[:k]
