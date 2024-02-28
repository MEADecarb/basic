import folium
import json
import requests

# Define a color palette
color_palette = ["#2C557E", "#fdda25", "#B7DCDF", "#000000", "#ff69b4", "#8A2BE2"]  # Updated color palette with more colors

# Create a base map centered over Maryland
m = folium.Map(location=[39.0458, -76.6413], zoom_start=8)

def add_geojson_from_url(geojson_url, name, color, map_obj):
    feature_group = folium.FeatureGroup(name=name)
    style_function = lambda x: {'fillColor': color, 'color': color}
    response = requests.get(geojson_url)
    if geojson_url.endswith(".pjson"):  # Handle ArcGIS pjson format
        geojson_data = json.loads(response.text.replace("pjson", "json"))
    else:
        geojson_data = response.json()

    geojson_layer = folium.GeoJson(
        geojson_data,
        style_function=style_function
    )

    # Customize pop-ups based on the feature group name
    if name == "MD HB550 Overburdened Census Tracts":
        # Example customization, adjust according to the available properties
        geojson_layer.add_child(folium.GeoJsonPopup(fields=['PropertyName'], aliases=['Property:'], labels=True))
    elif name == "Electric Retail Service Territories":
        # Example customization, adjust according to the available properties
        geojson_layer.add_child(folium.GeoJsonPopup(fields=['PropertyName'], aliases=['Property:'], labels=True))
    elif name == "Justice40 Tracts May 2022":
        # Example customization, adjust according to the available properties
        geojson_layer.add_child(folium.GeoJsonPopup(fields=['PropertyName'], aliases=['Property:'], labels=True))
    # Add more elif blocks for other specific customizations

    geojson_layer.add_to(feature_group)
    feature_group.add_to(map_obj)

# Add each GeoJSON source as a separate feature group with a color, label, and pop-up
github_geojson_sources = [
    ("https://geodata.md.gov/imap/rest/services/UtilityTelecom/MD_OffshoreWindEnergyPlanning/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson", "Offshore Wind Energy Planning"),
    ("https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MDOT_SHA_County_Boundaries/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson", "MDOT SHA County Boundaries"),
    ("https://meadecarb.github.io/GEO/map.geojson", "MD HB550 Overburdened Census Tracts"),
    ("https://services1.arcgis.com/Hp6G80Pky0om7QvQ/arcgis/rest/services/Retail_Service_Territories/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson", "Electric Retail Service Territories"),
    ("https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/Justice40_Tracts_May_2022/FeatureServer/0?f=pjson", "Justice40 Tracts May 2022")
]

for i, (url, name) in enumerate(github_geojson_sources):
    color = color_palette[i % len(color_palette)]
    add_geojson_from_url(url, name, color, m)

# Add Layer Control to toggle feature groups
folium.LayerControl().add_to(m)

# Display the map
m
