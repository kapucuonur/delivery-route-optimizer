import random
import math
from typing import List, Tuple, Dict

def cluster_locations(locations: List[Tuple[float, float]], num_vehicles: int) -> Dict[int, List[Tuple[float, float]]]:
    """
    Groups locations into clusters using a custom K-Means algorithm implementation.
    Written in pure Python to demonstrate algorithmic understanding and avoid heavy dependencies.
    """
    if num_vehicles <= 1 or not locations:
        return {0: locations}

    # 1. Initialize Centroids (Randomly pick k points)
    centroids = random.sample(locations, num_vehicles)
    
    for _ in range(20): # Run for 20 iterations (usually enough for convergence)
        # Create empty clusters
        clusters = {i: [] for i in range(num_vehicles)}
        
        # 2. Assignment Step
        for lat, lon in locations:
            # Find nearest centroid
            nearest_idx = -1
            min_dist = float('inf')
            
            for idx, (c_lat, c_lon) in enumerate(centroids):
                # Euclidean distance is sufficient for clustering logic locally
                d = (lat - c_lat)**2 + (lon - c_lon)**2
                if d < min_dist:
                    min_dist = d
                    nearest_idx = idx
            
            clusters[nearest_idx].append((lat, lon))
        
        # 3. Update Step (Recalculate centroids)
        new_centroids = []
        for i in range(num_vehicles):
            points = clusters[i]
            if not points:
                # If a cluster is empty, keep old centroid to avoid crash
                new_centroids.append(centroids[i])
                continue
                
            avg_lat = sum(p[0] for p in points) / len(points)
            avg_lon = sum(p[1] for p in points) / len(points)
            new_centroids.append((avg_lat, avg_lon))
        
        if new_centroids == centroids:
            break # Converged
        centroids = new_centroids

    return clusters
