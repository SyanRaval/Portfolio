import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium

st.title("Wanderly GeoMatcher: Geospatial Job Matching Demo")

# Load mock jobs
jobs = pd.read_csv("sample jobs.csv")

# Initialize map (US-centered)
m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# Add job markers
for _, job in jobs.iterrows():
    folium.Marker(
        [job['Latitude'], job['Longitude']],
        popup=f"<b>{job['Profession']}</b><br>Specialty: {job['Specialty']}<br>Pay: {job['Pay']}",
        icon=folium.Icon(color='red')
    ).add_to(m)

# Display map
st_folium(m, width=700, height=500)
