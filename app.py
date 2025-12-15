import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="🟢 LICHEN STORAGE", layout="wide")

# BLACK THEME
st.markdown("""
<style>
.main {background-color: black;}
.stApp {background-color: black;}
[data-testid="stAppViewContainer"] {background-color: black;}
</style>
""", unsafe_allow_html=True)

st.title("🟢 **LICHEN.STORAGE**")
st.markdown("**FC-496 / CRAID / BIOLOGICAL** | *60% Apocalypse OK*")

# CONTROLS
col1, col2 = st.columns([3,1])

with col1:
    if 'apocalypse' not in st.session_state:
        st.session_state.apocalypse = False
        st.session_state.integrity = 100
    
    st.metric("INTEGRITY", f"{st.session_state.integrity}%", delta=None)
    
    if st.button("💥 **SIMULATE APOCALYPSE 60%**", use_container_width=True):
        st.session_state.apocalypse = True
        st.session_state.integrity = 40
        st.balloons()
        st.rerun()

with col2:
    st.markdown("**RAID-6 vs LICHEN**")
    st.markdown("- **RAID**: 2 Drives")
    st.markdown("- **Lichen**: *60% NODES*")
    st.markdown("- **Rebuild**: Hours vs **INSTANT**")

# SPIRALE φ
if st.session_state.apocalypse:
    st.error("⚠️ 60% NODES KILLED → CRAID-496 ACTIVE")
    st.success("✅ **DATA RECOVERED 100%**")
else:
    angles = np.linspace(0, 4*np.pi, 12)
    r = np.logspace(0, 1, 12)
    
    fig = go.Figure()
    for i, angle in enumerate(angles):
        fig.add_trace(go.Scatterpolar(
            r=[0, r[i]], theta=[angle*180/np.pi],
            mode='markers+text',
            marker=dict(size=40, color='lime'),
            text=[f"N{i+1}🟢"],
            showlegend=False
        ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        title="**φ-SPIRALE** | Survivants: 100%",
        template="plotly_dark"
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("***Lichen Labs | v0.9.2***")
