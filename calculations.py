"""
ClayVein - Grid Geometry & Mineral Performance Calculator
MIT License - Copyright (c) 2026 masakertsa
"""

def calculate_grid_density(contamination_depth, soil_porosity, mineral_type):
    """
    Calculates the required shaft depth and horizontal grid spacing 
    based on soil conditions and chosen mineral properties.
    """
    # 1. Depth is directly tied to contamination depth
    shaft_depth = contamination_depth
    
    # 2. Establish baseline spacing multiplier based on mineral specs
    # High flocculation = wider spacing allowed
    mineral_profiles = {
        "zeolite_high": {"radius_modifier": 1.5, "efficiency": 0.92},
        "bentonite_medium": {"radius_modifier": 1.0, "efficiency": 0.85},
        "lime_flocculant": {"radius_modifier": 1.2, "efficiency": 0.78}
    }
    
    profile = mineral_profiles.get(mineral_type, {"radius_modifier": 0.8, "efficiency": 0.50})
    
    # 3. Dynamic Spacing Logic (Pascal & Capillary response simulation)
    # Higher porosity + high mineral modifier = wider spacing
    optimal_spacing = 2.0 * soil_porosity * profile["radius_modifier"]
    
    return {
        "recommended_depth_meters": round(shaft_depth, 2),
        "recommended_spacing_meters": round(optimal_spacing, 2),
        "system_efficiency_rating": profile["efficiency"]
    }

if __name__ == "__main__":
    # Test Scenario: Deep contaminated clay site
    print("--- ClayVein Simulation Vector ---")
    results = calculate_grid_density(
        contamination_depth=3.5,  # 3.5 meters deep
        soil_porosity=0.4,        # Dense clay baseline
        mineral_type="zeolite_high"
    )
    print(f"Injection Shaft Depth: {results['recommended_depth_meters']} m")
    print(f"Inter-vessel Grid Spacing: {results['recommended_spacing_meters']} m")
    print(f"Expected Remediation Factor: {results['system_efficiency_rating'] * 100}%")
