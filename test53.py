import folium
import requests

# Load India GeoJSON data with states
url = "https://raw.githubusercontent.com/datameet/india-geojson/master/india/india-states.geojson"
geojson_data = requests.get(url).json()

# Create a map centered on India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add GeoJSON overlay for states
folium.GeoJson(geojson_data, name="India States").add_to(m)

# Show the map
m
