import pandas
import folium

#===================================================================================================
#Adding multiple markers from files to the Map area--------------------------------------------------------------------

data = pandas.read_csv("volcanos.txt")

latitudes = list(data["LAT"])
longitudes = list(data["LON"])
names = list(data["NAME"])
elevations = list(data["ELEV"])
locations = list(data["LOCATION"])
html = """<h4>Volcano information:</h4>
Name: %s<br>
Height: %s m<br>
Location: %s
"""

#layer 1 - Map
map = folium.Map(location=[32, 0], zoom_start=4.3, tiles = "CartoDB positron", max_zoom = 100)

fgv = folium.FeatureGroup(name="Volcanos" )

def color(ele):
    if ele < 1500:
        return 'green'
    elif ele >=1500 and ele <3000:
        return 'orange'
    else:
        return 'red' 

#layer 2 - Mountain Location
for lat,lon, name, ele , loca, in zip(latitudes, longitudes, names, elevations, locations):
    iframe = folium.IFrame(html=html % (name ,str(ele), loca), width=200, height=120)
    fgv.add_child(folium.CircleMarker(location=[lat, lon], radius = 6, popup=folium.Popup(iframe), fill_color=color(ele), color = 'grey', fill_opacity=.9))

fgp = folium.FeatureGroup(name="Population" )

def colorPicker(population):
    if population < 10000000:
        return 'green'
    elif population >= 10000000 and population < 500000000:
        return 'orange'
    else:
        return 'red'

#layer 2 - polygones
fgp.add_child(folium.GeoJson(data=open('population.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x: {'fillColor': colorPicker(x['properties']['POP2005'])}))

#layer control

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())


map.save("index.html")
#===================================================================================================

