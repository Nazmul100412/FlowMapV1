# %%
import folium
import folium.map

# Define the map object
mapObj = folium.Map(location=[5.2614945887933615, 46.99324766424517], zoom_start=6, control_scale=True, tiles=None)


# Basemap layer (different)


# Add overlays
folium.TileLayer("Stamen Toner", attr='Stamen Toner', overlay=True, name='Stamen Toner').add_to(mapObj)
folium.TileLayer("Stamen Watercolor", attr='Stamen Watercolor', overlay=True, name='Stamen Watercolor').add_to(mapObj)



# folium.TileLayer("Stamen Terrain", attr='Stamen Terrain').add_to(mapObj)
# folium.TileLayer(show=True).add_to(mapObj)

# Add Google Road tile layer
google_road = folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
    attr='Google',
    name='Google Road',
    overlay=True,
    control=True
).add_to(mapObj)

# Add Google Satellite tile layer
google_satellite = folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='Google',
    name='Google Satellite',
    overlay=True,
    control=True
).add_to(mapObj)




# Add GeoJSON overlay
json_path = 'Admin2_DistrictBoundary.json'  # Path to your GeoJSON file
try:
    folium.GeoJson(json_path, name='District Boundaries').add_to(mapObj)
except FileNotFoundError:
    print(f"Error: The file {json_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")




# Add overlays if needed (example)
# folium.Marker(location=[5.2614945887933615, 46.99324766424517], popup='Marker').add_to(mapObj)

# Layer control button
folium.LayerControl().add_to(mapObj)


# Save the map to an HTML file
mapObj.save("map.html")


# %%
