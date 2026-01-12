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

def solve_nearest_neighbor(locations: List[Tuple[float, float]], distance_fn: Callable) -> Tuple[List[Tuple[float, float]], float]:
    """
    Optimized route using Nearest Neighbor heuristic.
    Assumes locations[0] is the depot.
    Returns: (Full Route including return to depot, Total Distance)
    """
    if not locations:
        return [], 0.0

    depot = locations[0]
    unvisited = locations[1:] # Exclude depot
    
    current = depot
    route = [depot]
    total_dist = 0
    
    while unvisited:
        nearest = min(unvisited, key=lambda x: distance_fn(current, x))
        total_dist += distance_fn(current, nearest)
        current = nearest
        route.append(current)
        unvisited.remove(current)
        
    # Return to depot
    total_dist += distance_fn(current, depot)
    route.append(depot)
    
    return route, total_dist
