import folium
from typing import List, Tuple

def generate_map(routes: List[List[Tuple[float, float]]], center_coords: Tuple[float, float], filename: str = "delivery_map.html"):
    """
    Generates an interactive map using Folium.
    Supports visualizing multiple routes (Fleet Management) with distinct colors.
    """
    # Create map centered at Tampere
    m = folium.Map(location=center_coords, zoom_start=13, tiles="CartoDB positron")
    
    # Aesthetic colors for different drivers
    colors = ["#2962FF", "#D50000", "#00C853", "#FFD600", "#AA00FF", "#00B8D4"]
    
    # Handle single route case (backward compatibility)
    # If the first item is a tuple (lat,lon) instead of a list, wrap it
    if routes and isinstance(routes[0], tuple):
        routes = [routes]

    for vehicle_id, route in enumerate(routes):
        color = colors[vehicle_id % len(colors)]
        
        # Draw the path
        folium.PolyLine(route, color=color, weight=4, opacity=0.8).add_to(m)
        
        # Add markers
        for i, (lat, lon) in enumerate(route):
            # Start and End (Depot) - Only add depot marker once (or simple text)
            # To avoid clutter if all start at same depot, we check vehicle_id
            if i == 0 or i == len(route)-1:
                # Depot
                folium.Marker(
                    [lat, lon], 
                    popup="<b>Depot (Wolt Market)</b>", 
                    icon=folium.Icon(color="black", icon="home", prefix='fa')
                ).add_to(m)
            else:
                # Customers
                folium.Marker(
                    [lat, lon], 
                    popup=f"Driver #{vehicle_id+1} - Stop #{i}", 
                    icon=folium.Icon(color="white", icon_color=color, icon="user", prefix='fa')
                ).add_to(m)

    m.save(filename)
    print(f"✅ Map generated: {filename}")
