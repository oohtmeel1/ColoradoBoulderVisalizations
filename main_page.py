import branca
import folium
import folium.plugins
import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import re
import numpy as np
import numpy as np
from datetime import datetime 
import altair as alt
import json
import requests
import pandas as pd
import numpy as np
from folium.plugins import MarkerCluster
from folium.plugins import TimeSliderChoropleth
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

st.header('Visualization of California water testing Data over the last 100 years')

st.image('number_of_testing_stations_over_100_years.png')

st.header('Visualization of California water testing Data over the last 100 years')

st.image('Number of types of tests over the last 100 years.png')



map1903 = pd.read_csv(r"map1903")

st.subheader('Raw data')
st.write(map1903)


us_counties = (
    "C:/Users/amcfa/Downloads/California_County_Boundaries.geojson"
)

us_counties

style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}

m = folium.Map(location=(38.5816,-121.4944),width=800, zoom_start=6,zoom_control= True ,dragging = True, scrollWheelZoom=True)
folium.GeoJson(us_counties).add_to(m)


NIL = folium.features.GeoJson(
    us_counties,
    style_function=style_function, 
    control=False,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['COUNTY_NAME'],  # use fields from the json file
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
    )
)
marker_cluster = MarkerCluster(
    name="county_name",
).add_to(m)

for row in map1903.itertuples():
    #print(row)
    folium.Marker(location=[row.latitude,row.longitude],popup=row.county_name).add_to(marker_cluster)

folium.LayerControl().add_to(m)


dicts = {"1903":m}
years = st.sidebar.selectbox("Please pick a year range",
                             ("1903-1913","1914-1923"))

st_data = st_folium(m, width=725)


