import streamlit as st
import folium
import pandas as pd
from streamlit_folium import st_folium

st.title("Wanderly GeoMatcher: Geospatial Job Matching Demo")

# Load mock jobs
jobs = pd.read_csv("jobs.csv")

# Initialize map (US-centered)
m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# Add job markers
for _, job in jobs.iterrows():
    folium.Marker(
        [job['latitude'], job['longitude']],
        popup=f"<b>{job['title']}</b><br>Specialty: {job['specialty']}<br>Pay: {job['pay']}",
        icon=folium.Icon(color='red')
    ).add_to(m)

# Display map
st_folium(m, width=700, height=500)
