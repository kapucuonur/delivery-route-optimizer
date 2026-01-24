import unittest
from delivery_optimizer import geography, algorithm, ai_utils

class TestDeliveryOptimizer(unittest.TestCase):

    def test_ai_clustering(self):
        """Test K-Means clustering with distinct groups."""
        # Create two distinct groups of points far apart
        # Group 1: Around (0,0)
        group1 = [(0.0, 0.0), (0.1, 0.1), (0.1, 0.0)]
        # Group 2: Around (10,10)
        group2 = [(10.0, 10.0), (10.1, 10.1), (10.0, 10.1)]
        
        locations = group1 + group2
        
        # Cluster into 2 vehicles
        clusters = ai_utils.cluster_locations(locations, num_vehicles=2)
        
        self.assertEqual(len(clusters), 2)
        
        # Check if points are separated correctly
        # We can't guarantee which cluster ID (0 or 1) gets which group, 
        # but the points in each cluster should be close to each other.
        
        c0 = clusters[0]
        c1 = clusters[1]
        
        # Ideally, one cluster has only small coordinates, the other has large.
        avg_c0 = sum(p[0] for p in c0) / len(c0)
        avg_c1 = sum(p[0] for p in c1) / len(c1)
        
        # Distance between centroids should be large (~10+)
        self.assertTrue(abs(avg_c0 - avg_c1) > 5.0)
    
    def test_distance_calculation(self):
        # Distance between same point should be 0
        p1 = (61.4978, 23.7610)
        dist = geography.calculate_distance(p1, p1)
        self.assertAlmostEqual(dist, 0.0)

    def test_optimization_improvement(self):
        # Create a simple line scenario where NN works perfectly
        # Depot at 0,0
        # Points at (1,0), (2,0), (3,0) roughly (using small lat/lon diffs)
        # Random shuffle would likely be worse than 0->1->2->3
        
        # Latitude 1 deg ~= 111km
        locations = [
            (0.00, 0.00), # Depot
            (0.01, 0.00), # Stop 1
            (0.02, 0.00), # Stop 2
            (0.03, 0.00), # Stop 3
        ]
        
        optimized_route, opt_dist = algorithm.solve_nearest_neighbor(
            locations, 
            geography.calculate_distance
        )
        
        # Optimized route should go sequentially 0->1->2->3->0, 
        # Total distance approx: 0.01 + 0.01 + 0.01 + 0.03 (return) = 0.06 deg
        # 0.06 * 111.32 km/deg = 6.67 km approx
        
        self.assertEqual(len(optimized_route), 5) # 4 points + return to start
        self.assertEqual(optimized_route[0], locations[0])
        self.assertEqual(optimized_route[-1], locations[0])

if __name__ == '__main__':
    unittest.main()
