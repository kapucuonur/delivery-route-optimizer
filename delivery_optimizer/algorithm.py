from typing import List, Tuple, Callable

def calculate_route_distance(route: List[Tuple[float, float]], distance_fn: Callable) -> float:
    """Calculates total distance of a route sequence."""
    total_dist = 0
    if not route:
        return 0.0
        
    for i in range(len(route) - 1):
        total_dist += distance_fn(route[i], route[i+1])
        
    # Return to start if implied? 
    # In this specific problem, we explicitly want a tour (depot -> customers -> depot)
    # The route passed in usually includes depot at start.
    # We should add distance from last point back to first point if it's a closed loop.
    # However, the previous implementation added it explicitly.
    # Let's check the route list. If route[-1] != route[0], we need to add the return leg?
    # Or, the algorithm normally constructs the full path including return.
    # Let's assume the input route is the sequence of visits.
    
    # Matching previous logic:
    # "dist += self.calculate_distance(current, self.depot) # Return home"
    
    # If the route list already contains the depot at the end, we don't double count.
    # If not, we should probably just calculating the sum of segments.
    # Let's stick to simple sum of segments for flexibility, and ensure the route list HAS the return trip.
    
    return total_dist

def two_opt(route: List[Tuple[float, float]], distance_fn: Callable) -> List[Tuple[float, float]]:
    """
    Refines the route using the 2-Opt algorithm to remove crossing paths.
    """
    best_route = route[:]
    improved = True
    
    # We don't change start (0) and end (-1) because they are the fixed depot location
    # BUT for a TSP tour, start and end are the same point.
    # The segment between i and k is reversed.
    
    while improved:
        improved = False
        for i in range(1, len(best_route) - 2):
            for k in range(i + 1, len(best_route) - 1):
                # Current edges: (i-1, i) and (k, k+1)
                # New edges:     (i-1, k) and (i, k+1)
                
                # Calculate lengths
                d_current = distance_fn(best_route[i-1], best_route[i]) + \
                            distance_fn(best_route[k], best_route[k+1])
                            
                d_new = distance_fn(best_route[i-1], best_route[k]) + \
                       distance_fn(best_route[i], best_route[k+1])
                
                if d_new < d_current:
                    # Reverse segment from i to k
                    best_route[i:k+1] = best_route[i:k+1][::-1]
                    improved = True
                    
    return best_route

def solve_nearest_neighbor(locations: List[Tuple[float, float]], distance_fn: Callable) -> Tuple[List[Tuple[float, float]], float]:
    """
    Optimized route using Nearest Neighbor heuristic followed by 2-Opt refinement.
    Assumes locations[0] is the depot.
    Returns: (Full Route including return to depot, Total Distance)
    """
    if not locations:
        return [], 0.0

    depot = locations[0]
    unvisited = locations[1:] # Exclude depot
    
    current = depot
    route = [depot]
    
    # 1. Initial Greedy Construction (Nearest Neighbor)
    while unvisited:
        nearest = min(unvisited, key=lambda x: distance_fn(current, x))
        current = nearest
        route.append(current)
        unvisited.remove(current)
        
    # Return to depot
    route.append(depot)
    
    # 2. Refine with 2-Opt
    optimized_route = two_opt(route, distance_fn)
    
    # 3. Recalculate Total Distance
    total_dist = calculate_route_distance(optimized_route, distance_fn)
    
    return optimized_route, total_dist
