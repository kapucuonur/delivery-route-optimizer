from flask import Flask, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

# --- IMPORT SHARED OPTIMIZER ---
from delivery_optimizer import geography, algorithm

@app.route('/optimize', methods=['GET'])
def get_optimized_route():
    print("\n" + "="*40)
    print("🚀 V2.1 - CENTRALIZED AI OPTIMIZER LINKED")
    print("="*40 + "\n")

    # Depo (Keskustori)
    depot_dict = {"lat": 61.4980, "lng": 23.7610}
    depot_tuple = (depot_dict["lat"], depot_dict["lng"])

    # Müşteriler (Real Tampere Stops matching Flutter App)
    stops_dicts = [
        {"lat": 61.4955, "lng": 23.7810}, # Tampere Hall
        {"lat": 61.4995, "lng": 23.7945}, # Kaleva Church
        {"lat": 61.4943, "lng": 23.7680}, # Ratina Shopping Centre
        {"lat": 61.4965, "lng": 23.7350}, # Pyynikki Observation Tower
        {"lat": 61.5030, "lng": 23.7800}  # Tammela Stadium
    ]
    
    # Convert dicts to tuples for the algorithm
    stops_tuples = [(d["lat"], d["lng"]) for d in stops_dicts]
    
    # Prepare input for solver (Start + Others)
    # Note: solve_nearest_neighbor expects [Depot, Customer1, Customer2...]
    input_route = [depot_tuple] + stops_tuples

    # Calculate Optimized Route (Nearest Neighbor + 2-Opt)
    optimized_tuples, total_dist = algorithm.solve_nearest_neighbor(
        input_route, 
        geography.calculate_distance
    )
    
    # Convert tuples back to dicts for JSON response
    optimized_dicts = [{"lat": lat, "lng": lng} for lat, lng in optimized_tuples]
    
    print(f"✅ Rota Optimize Edildi. Toplam Durak: {len(optimized_dicts)} | Mesafe: {total_dist:.2f} km")
    return jsonify(optimized_dicts)

if __name__ == '__main__':
    # Port 5001
    app.run(host='0.0.0.0', port=5001, debug=True)