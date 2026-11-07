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

def calculate_use_case_requirements(use_case, area_sqm, contamination_depth, soil_porosity, shaft_diameter_mm=100):
    """
    Calculates dynamic spacing, mineral ratios, and total material weight in kilograms
    for specific contamination scenarios (heavy_metals, hydrocarbons, fertilizers).
    """
    # Define profiles based on the three core scenarios
    scenarios = {
        "heavy_metals": {
            "name": "Heavy Metal Lockdown",
            "zeolite_pct": 0.70,
            "bentonite_pct": 0.30,
            "spacing_modifier": 0.8,  # Standard grid
            "base_efficiency": 0.95
        },
        "hydrocarbons": {
            "name": "Hydrocarbon Sponge",
            "zeolite_pct": 0.30,
            "bentonite_pct": 0.70,
            "spacing_modifier": 0.4,  # Very dense grid due to oil viscosity
            "base_efficiency": 0.88
        },
        "fertilizers": {
            "name": "Fertilizer & Nutrient Recovery",
            "zeolite_pct": 0.80,
            "bentonite_pct": 0.20,
            "spacing_modifier": 1.3,  # Wider grid allowed for highly soluble nutrients
            "base_efficiency": 0.91
        }
    }
    
    spec = scenarios.get(use_case)
    if not spec:
        raise ValueError(f"Unknown use case: {use_case}. Choose from: heavy_metals, hydrocarbons, fertilizers")
        
    # 1. Determine baseline mineral profile for the spacing logic
    mineral_type = "zeolite_high" if spec["zeolite_pct"] >= spec["bentonite_pct"] else "bentonite_medium"
    base_grid = calculate_grid_density(contamination_depth, soil_porosity, mineral_type)
    
    # 2. Scale the spacing based on the contamination type modifier
    final_spacing = max(0.2, base_grid["recommended_spacing_meters"] * spec["spacing_modifier"])
    
    # 3. Calculate grid layout mechanics (estimated shaft count on a square grid)
    shafts_per_meter = 1.0 / final_spacing
    total_shafts = round((area_sqm * (shafts_per_meter ** 2)))
    if total_shafts == 0:
        total_shafts = 1
        
    # 4. Volumetric and mass calculations for the mineral core
    # Material bulk density estimation: ~1100 kg/m3 for crushed dry minerals
    bulk_density_kg_m3 = 1100
    radius_m = (shaft_diameter_mm / 2) / 1000
    shaft_volume_m3 = 3.14159 * (radius_m ** 2) * contamination_depth
    total_volume_m3 = shaft_volume_m3 * total_shafts
    total_weight_kg = total_volume_m3 * bulk_density_kg_m3
    
    return {
        "scenario_name": spec["name"],
        "calculated_spacing_meters": round(final_spacing, 2),
        "total_shafts_required": total_shafts,
        "mix_ratio": f"{int(spec['zeolite_pct']*100)}% Zeolite / {int(spec['bentonite_pct']*100)}% Bentonite",
        "total_zeolite_needed_kg": round(total_weight_kg * spec["zeolite_pct"], 1),
        "total_bentonite_needed_kg": round(total_weight_kg * spec["bentonite_pct"], 1),
        "total_material_weight_kg": round(total_weight_kg, 1),
        "expected_efficiency": spec["base_efficiency"]
    }

if __name__ == "__main__":
    print("--- ClayVein Original Simulation Vector ---")
    results = calculate_grid_density(
        contamination_depth=3.5,
        soil_porosity=0.4,
        mineral_type="zeolite_high"
    )
    print(f"Injection Shaft Depth: {results['recommended_depth_meters']} m")
    print(f"Inter-vessel Grid Spacing: {results['recommended_spacing_meters']} m")
    print(f"Expected Remediation Factor: {results['system_efficiency_rating'] * 100}%\n")
    
    print("--- ClayVein Use Case Field Vectors ---")
    # Test Scenario: 100 sqm plot, 2.0 meters deep contamination, dense clay (porosity 0.35)
    site_area = 100
    site_depth = 2.0
    clay_porosity = 0.35
    
    for case in ["heavy_metals", "hydrocarbons", "fertilizers"]:
        field_data = calculate_use_case_requirements(
            use_case=case,
            area_sqm=site_area,
            contamination_depth=site_depth,
            soil_porosity=clay_porosity,
            shaft_diameter_mm=100  # 10cm standard auger
        )
        print(f"[{field_data['scenario_name']}]")
        print(f"  -> Recommended Grid Spacing: {field_data['calculated_spacing_meters']} m")
        print(f"  -> Total Shafts to Drill for {site_area} m²: {field_data['total_shafts_required']} pcs")
        print(f"  -> Core Mix Recipe: {field_data['mix_ratio']}")
        print(f"  -> Material Weights: Zeolite {field_data['total_zeolite_needed_kg']} kg | Bentonite {field_data['total_bentonite_needed_kg']} kg")
        print(f"  -> Total Mass: {field_data['total_material_weight_kg']} kg (~{round(field_data['total_material_weight_kg']/25)} säkkiä à 25kg)")
        print(f"  -> Target Remediation Efficiency: {field_data['expected_efficiency'] * 100}%\n")
