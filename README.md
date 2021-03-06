# Webmap-with-Python
This python application creates a Webmap that displays a world map with the population of each country that was extracted from population.json file. The application saves a "Map1.html" file on the working directory. 

## Getting Started
This application was created through Visual Studio Code using folium library. The library is used to create several types of Leaflet maps 

To run the program, download Webmap.py, population.json, and volcanos.txt.

## Installation
Install any python environment. I recommend Visual Studio Code 

Install folium: ```pip3 install folium```

You should be able to run the program on your environment

## Webmap
This map displays the population of each country by color. Color 'red' means population greater than or equal to 500000000, color 'orange' means population greater than or equal to 10000000 and less than  500000000, and color 'green' means population less than 10000000.

The map starts on the equator and you can zoom in and out using (+/-) on top left corner of the map<br>
![](images/Initial.png)

Here's a view of entire map<br>
![](images/full.png)

On USA, the dots represent mountains on the west coast.<br>
![](images/usa.png)

Click on each dot to know the mountain's name, height, and location.

You can toggle on and off mountains and population map by clicking layers icon on the top right of the map.<br>

![](images/layer.png)
![](images/layer2.png)
