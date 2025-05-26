# Postquake Priority Mapper

A disaster response mapping tool that ranks locations for urgent UAV response based on AI model outputs such as damage levels, survivor detections, roadblocks, and accessibility.

## 📌 Use Case
After an earthquake, drones collect vision and sensor data. This tool prioritizes locations using a simple scoring system to help first responders focus on:
- Collapsed buildings
- Survivors detected
- Blocked roads
- Proximity to hospitals/shelters

## 🧠 Logic
Each region gets a priority score based on:
- Structural damage (segmentation map input)
- Survivor detections (bounding box count)
- Road accessibility (map or classification)
- Distance to nearest critical infrastructure

## 📁 Structure
- `scripts/`: Priority logic, zone scoring
- `notebooks/`: Visual simulation and map plotting
- `assets/`: Heatmap or priority zone samples
- `data/`: Grid simulation input or CSVs

## 🔮 Future Work
- Integrate with GIS systems
- Real-time mission planning integration
- Export to ground team tablets
