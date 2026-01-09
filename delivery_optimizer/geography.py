import random
import math
from typing import List, Tuple

# Tampere Center Coordinates
TAMPERE_COORDS = (61.4978, 23.7610)

def generate_locations(num_stops: int, center: Tuple[float, float] = TAMPERE_COORDS) -> List[Tuple[float, float]]:
    """Generates random GPS coordinates around a center point."""
    locations = []
    # First point is the depot (center itself or very close to it? 
    # Original code made random points around center, and took 0th as depot. 
    # Let's keep consistent: generate random points around center.
    
    for _ in range(num_stops):
        # Random offset roughly within 3-5km
        lat = center[0] + random.uniform(-0.03, 0.03)
        lon = center[1] + random.uniform(-0.05, 0.05)
        locations.append((lat, lon))
    return locations

def calculate_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    """Haversine formula to calculate distance between two GPS points in km."""
    R = 6371  # Earth radius in km
    lat1, lon1 = math.radians(p1[0]), math.radians(p1[1])
    lat2, lon2 = math.radians(p2[0]), math.radians(p2[1])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c
