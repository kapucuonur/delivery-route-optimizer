import argparse
import random
from delivery_optimizer import geography, algorithm, visualizer, ai_utils

def main():
    parser = argparse.ArgumentParser(
        description='Wolt Delivery Route Optimizer - AI Powered Fleet Management'
    )
    parser.add_argument(
        '--stops', 
        type=int, 
        default=20, 
        help='Total number of delivery orders'
    )
    parser.add_argument(
        '--vehicles', 
        type=int, 
        default=1, 
        help='Number of available drivers/vehicles'
    )
    args = parser.parse_args()

    print(f"🚀 Initializing AI Logistics for {args.vehicles} vehicle(s) and {args.stops} orders...")
    
    # 1. Generate Data
    # For simulation, we create one big pool of orders around Tampere
    full_locations = geography.generate_locations(args.stops)
    depot = full_locations[0] # Assume the first generated point is the depot for simplicity
    
    # Remove depot from the list to cluster roughly just the customers, 
    # then re-add depot to each cluster later.
    customers = full_locations[1:]

    # 2. AI Clustering (Fleet Management)
    if args.vehicles > 1:
        print(f"🤖 AI: Clustering orders into {args.vehicles} zones using K-Means...")
        clusters = ai_utils.cluster_locations(customers, args.vehicles)
    else:
        clusters = {0: customers}

    # 3. Optimization (Per Driver)
    fleet_routes = []
    total_fleet_distance = 0
    
    print("-" * 40)
    for vehicle_id, assigned_customers in clusters.items():
        if not assigned_customers:
            continue
            
        # Each driver starts at Depot -> Customers -> Depot
        # We construct the list for the TSP solver
        route_points = [depot] + assigned_customers
        
        optimized_route, dist = algorithm.solve_nearest_neighbor(
            route_points, 
            geography.calculate_distance
        )
        
        fleet_routes.append(optimized_route)
        total_fleet_distance += dist
        print(f"🚗 Driver #{vehicle_id+1}: {len(assigned_customers)} orders | Route: {dist:.2f} km")

    print("-" * 40)
    print(f"🏁 Total Fleet Distance: {total_fleet_distance:.2f} km")
    
    # 4. Visualization
    visualizer.generate_map(
        fleet_routes, 
        geography.TAMPERE_COORDS,
        "delivery_map.html"
    )

if __name__ == "__main__":
    main()
