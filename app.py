import streamlit as st
import streamlit.components.v1 as components
import os

# Config black theme
st.markdown("""
<style>
    .main {background-color: black;}
    .stApp {background-color: black;}
    [data-testid="stAppViewContainer"] {background-color: black;}
    .css-1d391kg {background-color: black;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="text-align: center; color: white; font-family: monospace; font-size: 3rem;">LICHEN<span style="color: #10B981;">.STORAGE</span></h1>', unsafe_allow_html=True)

# Serve ton React app depuis dist/ (build Vite)
try:
    # Cherche le build React dans dist/
    if os.path.exists("dist/index.html"):
        with open("dist/index.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Injecte CSS/JS depuis dist/
        components.html(html_content, height=1200, scrolling=True)
    else:
        st.warning("🚧 **Build React manquant** → `npm run build` requis")
        st.info("""
        **1-CLI BUILD :**
        ```
        npm install
        npm run build
        ```
        Puis refresh !
        """)
        
except Exception as e:
    st.error(f"❌ Erreur React: {e}")
    st.info("Fallback Streamlit mode...")
    
    # Fallback spirale si React down
    import numpy as np
    import plotly.graph_objects as go
    
    fig = go.Figure(go.Scatterpolar(r=[0,1], theta=[0,72,144,216,288], mode='markers'))
    st.plotly_chart(fig)
