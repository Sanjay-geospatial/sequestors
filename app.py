import pandas as pd
import numpy as np
import geopandas as gpd
import os
import matplotlib.pyplot as plt
import pydeck as pdk
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Sequestors | NGO", layout="wide")

# Inject Calligraphy Font and Styles
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

.title {
    font-family: 'Great Vibes', cursive;
    font-size: 110px;
    text-align: center;
    margin-bottom: 0px;
    color: #2E8B57;
}

.tagline {
    text-align: center;
    font-size: 22px;
    color: #555;
    margin-top: -20px;
}
</style>
""", unsafe_allow_html=True)

# ========= TITLE =========
st.markdown('<div class="title">Sequestors</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Planting a Greener Tomorrow for Bengaluru</div>',
            unsafe_allow_html=True)

# try:
#     st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
#     st.image("plant.png", width = 150)
#     st.markdown('</div>', unsafe_allow_html=True)
# except:
#     st.error("❌ Could not load plant.png — ensure it's in the same folder or use a raw GitHub URL.")

st.markdown("---")


# Description of the NGO (Section 1)
st.header("About Us")
st.write("""
Sequestors is a non-profit organization dedicated to restoring ecosystems, 
fighting climate change, and empowering communities through large-scale tree plantation 
and sustainable land management practices. Our mission is to sequester carbon by planting 
native trees while promoting biodiversity, soil health, and climate-resilient urban environments.
""")

# What We Do Section (Section 2)
st.header("What We Do")
st.write("""
At Sequestors, we focus on a single, powerful mission:

- 🌱 **Tree Planting in Bengaluru** – We organize community-driven tree plantation drives 
  with a motivated group of volunteers dedicated to greening every neighborhood. 
  We partner with local communities to ensure the long-term survival of every plant.

Our work is rooted in the belief that collective action, even through small steps, 
can transform urban landscapes and breathe life back into our city.
""")

st.markdown("---")

# Our Impact Section with Visualization (Section 3 - Now spanning full width)
df = pd.read_excel('tree_data.xlsx')

species_counts = df['species_name'].value_counts().reset_index()
species_counts.columns = ['species_name', 'count']

st.title("Tree species planted so far...")

fig = px.bar(
    species_counts, 
    x='species_name', 
    y='count',
    color='species_name',
    text='count',
    title="Species Count",
)

fig.update_traces(marker=dict(line=dict(width=1, color="black")))
fig.update_layout(
    showlegend=False,
    xaxis_title="Species",
    yaxis_title="Count",
    title_x=0.5,
    bargap=0.3,
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.header("We often involve volunteers in our activities to create awareness")

st.markdown("### *Tree Planting Activity*")

with st.expander("📸 Show Tree Planting Activity"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/pic1.jpg", use_container_width=True)

    with col2:
        st.image("images/pic4.jpg", use_container_width=True)

    with col3:
        st.image("images/pic5.jpg", use_container_width=True)

st.markdown("### *Plastic drive*")

with st.expander("📸 Show clean drive Activity"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/pic2.jpg", use_container_width=True)

    with col2:
        st.image("images/pic3.jpg", use_container_width=True)

    with col3:
        st.image("images/pic6.jpg", use_container_width=True)



st.header("Our Impact")
st.write(f"Explore {len(df)} specific sites where we've planted trees across Bengaluru")

lat_center, lon_center = df['lat'].mean(), df['lon'].mean()

# ---- PYDECK LAYER ----
scatter_layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position='[lon, lat]',
    get_radius=7,
    radius_units="meters",
    get_color=[0, 255, 0],   # green points
    pickable=True,
)

view_state = pdk.ViewState(
    latitude=lat_center,
    longitude=lon_center,
    zoom=11,
    pitch=45,
)

tooltip = {
    "html": "<b>Species:</b> {species_name}",
    "style": {"backgroundColor": "black", "color": "white"}
}

r = pdk.Deck(
    layers=[scatter_layer],
    initial_view_state=view_state,
    tooltip=tooltip,
    map_style="https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json"
)

st.pydeck_chart(r)
st.markdown("---")

# Footer
st.markdown("<p style='text-align: center; font-size: 14px; color: #696969;'>© 2025 Sequestors NGO | Greening Bengaluru Together.</p>", unsafe_allow_html=True)
