# 🍃 ClayVein: Passive Mineral-Cyanobacteria Soil Remediation Framework

A 100% passive biopunk architecture designed to remediate heavy-metal and chemically contaminated clay soils using capillary pressure, ion exchange, and biological symbiosis.

## 🛠 1. Thermodynamic & Biological Architecture

- **Targeted Macro-Punctures:** Vertical shafts drilled into the soil substrate using a standard Ø 100 mm (10 cm) auger, scaled dynamically to the depth of the toxin plume.
- **Crushed Mineral Core:** Shafts filled with high-surface-area minerals (e.g., Zeolite, Bentonite) that draw contaminated pore-water via capillary action.
- **Photosynthetic Cyanobacteria Cap:** A living *Nostoc* matrix on the surface that utilizes photosynthesis for bioaccumulation and neutralizes chemical vapors.

```text
       [Sunlight / Atmosphere]
                  |
     +------------v------------+

     |   Cyanobacteria Cap     |  <-- Bioaccumulation & Harvesting Zone
     +------------+------------+
                  |
     +------------v------------+

     |  Crushed Mineral Core   |  <-- Passively draws and binds toxic
     |   (Zeolite / Bentonite) |      pore-water from surrounding clay
     +-------------------------+
                  |
                  v
       [Remediated Soil Base]
```

## 📐 2. Engineering Framework & Variable Scaling

Layout geometry scales dynamically based on local environmental variables:
1. **Depth Parameter ($D$):** Calibrated to the lowest vector of discovered soil contamination.
2. **Spacing Parameter ($S$):** Determined by the active radius and flocculation capacity of the chosen mineral core.

## 📋 3. Standard Deployment Scenarios

The framework includes pre-configured parameters for the three most common environmental contamination profiles. 

See the full [use-cases.md](use-cases.md) guide for detailed field instructions:
*   **Scenario A: Heavy Metal Lockdown ($Pb^{2+}$, $Cd^{2+}$, $Cu^{2+}$)** – 70:30 Zeolite/Bentonite mix tailored for industrial or urban runoff.
*   **Scenario B: Hydrocarbon Sponge (Fuel Oil, Diesel)** – 30:70 Zeolite/Bentonite dense grid optimized for hydrophobic organic compounds.
*   **Scenario C: Fertilizer & Nutrient Recovery ($NH_4^+$, Phosphate)** – 80:20 Zeolite/Bentonite wide grid designed to turn agricultural runoff into recyclable biomass.

These scenarios can be simulated directly using the `calculate_use_case_requirements()` function within `calculations.py`.


## 🔬 4. Scientific Grounding & Mechanics

- **Geochemical Ion-Exchange:** Zeolite matrices utilize a crystalline aluminosilicate framework to capture heavy metal cations ($Pb^{2+}$, $Cd^{2+}$) via ion-exchange [modified zeolite application](https://maxapress.com) and [zeolite for toxic metal uptake](https://mdpi.com), while mineral cores trigger localized flocculation to open dense clay structures [effect of biochar, zeolite and bentonite](https://sciencedirect.com).
- **Cyanobacterial Biosorption:** Extracellular polymeric substances of *Nostoc* strains bind upward-migrating heavy metals with a verified removal efficiency of up to 91–98% through passive biosorption and active intracellular bioaccumulation [bioaccumulation and biosorption study](https://researchgate.net).

## 📄 License

This project is licensed under the **MIT License** – Copyright (c) 2026 masakertsa.
