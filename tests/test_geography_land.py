import unittest
from delivery_optimizer import geography

class TestGeographyLand(unittest.TestCase):
    def test_no_water_points(self):
        """Generate 100 points and ensure none are in the exclusion zones."""
        # Force a known seed if possible, but geography uses random.
        # We just want to check that the filtering logic works.
        
        points = geography.generate_locations(100)
        self.assertEqual(len(points), 100)
        
        for lat, lon in points:
            # Manually check against the zones defined in geography.py
            # geography.is_on_land should return True for all these
            self.assertTrue(geography.is_on_land(lat, lon), f"Point {lat}, {lon} failed is_on_land check")
            
            # Double check against the explicit zones to be sure
            in_water = False
            for (lat_min, lat_max, lon_min, lon_max) in geography.LAKE_ZONES:
                if lat_min <= lat <= lat_max and lon_min <= lon <= lon_max:
                    in_water = True
                    break
            
            self.assertFalse(in_water, f"Point {lat}, {lon} fell into exclusion zone!")

if __name__ == '__main__':
    unittest.main()
