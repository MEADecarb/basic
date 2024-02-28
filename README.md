**Maryland GeoJSON Map**

This project creates an interactive map of Maryland that displays various geographic datasets with customized pop-ups and color schemes.
URL: https://meadecarb.github.io/basic/
**Features**

* **GeoJSON Datasets:** The map integrates multiple GeoJSON datasets, including:
    * Offshore Wind Energy Planning
    * MDOT SHA County Boundaries
    * MD HB550 Overburdened Census Tracts
    * Electric Retail Service Territories
    * Justice40 Tracts May 2022
* **Color Coding:** Each GeoJSON dataset is visually differentiated using  a distinct color palette.
* **Customizable Pop-ups:** The map includes custom pop-ups tailored to the specific properties of each dataset, providing relevant information on click.
* **Layer Control:** Users have the ability to toggle the visibility of individual GeoJSON layers, allowing for focused analysis.

**Dependencies**

* **folium:** Python library for creating interactive maps. 
* **requests:**  Library for making HTTP requests to fetch GeoJSON data.
* **json:**  Library for working with JSON data.

**Installation**

```bash
pip install folium requests json
```

**Usage**

1. Clone this repository.
2. Run the code  (e.g., `python map_script.py` if your code is in a file named "map_script.py")

The map will be rendered in your default web browser.

**Configuration**

The following sections in the code can be modified to customize the map's appearance and behavior:

* **`color_palette`:** Edit the list of colors to create your own color scheme.
* **`add_geojson_from_url` function:** Add or remove `geojson_url` and `name` pairs in the `github_geojson_sources` list to include different datasets.
* **`geojson_layer.add_child` sections**: Customize the content of pop-ups in these sections by adjusting the `fields`, `aliases`, and `labels` parameters of `folium.GeoJsonPopup`.

**Contributing**

We welcome contributions! If you have new GeoJSON datasets,  suggestions for improvement, or want to fix a bug, please submit a pull request.

**License**

This project is licensed under the MIT License – see the LICENSE file for details.


