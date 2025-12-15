import streamlit as st

st.set_page_config(page_title="🟢 LICHEN STORAGE", layout="wide")

st.markdown("""
<style>
.main {background-color: black;}
.stApp {background-color: black;}
[data-testid="stAppViewContainer"] {background-color: black;}
</style>
""", unsafe_allow_html=True)

# TON DESIGN SUBLIME INLINE (AUCUN npm !)
st.markdown("""
<div style='
    background: linear-gradient(135deg, #000000 0%, #0a0a0a 100%); 
    padding: 2rem; 
    border-radius: 16px; 
    border: 1px solid rgba(16,185,129,0.2);
    min-height: 90vh;
    color: white;
    font-family: "Courier New", monospace;
'>
    <div style='text-align: center; margin-bottom: 2rem'>
        <h1 style='
            font-size: 3rem; 
            background: linear-gradient(45deg, white, #10B981); 
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent;
            font-weight: bold;
            margin: 0;
        '>LICHEN<span style='color: #10B981;'>.STORAGE</span></h1>
        <p style='color: #10B981; font-size: 1rem; margin: 0.5rem 0;'>FC-496 / CRAID / BIOLOGICAL</p>
    </div>

    <div style='display: flex; gap: 2rem; max-width: 1400px; margin: 0 auto;'>
        
        <!-- VISUALIZER -->
        <div style='flex: 2; background: rgba(31,41,55,0.4); border-radius: 16px; padding: 2rem;'>
            <div style='position: absolute; top: 2rem; right: 2rem; font-size: 2rem; font-weight: bold; color: #10B981'>
                INTEGRITY: 100%
            </div>
            <canvas id="cluster" width="600" height="400" style="
                width: 100%; 
                height: 400px; 
                border-radius: 12px; 
                background: radial-gradient(circle, rgba(16,185,129,0.1) 0%, black 70%);
                border: 1px solid rgba(16,185,129,0.3);
            "></canvas>
        </div>

        <!-- CONTROLS -->
        <div style='flex: 1; display: flex; flex-direction: column; gap: 1.5rem;'>
            
            <!-- APOCALYPSE BUTTON -->
            <button onclick="triggerApocalypse()" style='
                width: 100%; 
                padding: 1.5rem; 
                background: linear-gradient(45deg, #ef4444, #dc2626); 
                color: white; 
                border: none; 
                border-radius: 12px; 
                font-weight: bold; 
                font-size: 1.1rem; 
                cursor: pointer; 
                transition: all 0.3s;
            ' onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
                💥 SIMULATE APOCALYPSE<br><span style='font-size: 0.8rem; opacity: 0.8'>KILL 60% NODES</span>
            </button>

            <!-- STATS -->
            <div style='
                background: rgba(31,41,55,0.6); 
                padding: 1.5rem; 
                border-radius: 12px; 
                border: 1px solid rgba(16,185,129,0.2);
            '>
                <table style='width: 100%; font-size: 0.85rem;'>
                    <tr><td style='padding: 0.5rem; color: #9ca3af'>RAID-6 Max Fail</td><td style='padding: 0.5rem; color: #ef4444; font-weight: bold'>2 Drives</td></tr>
                    <tr><td style='padding: 0.5rem; color: #9ca3af'>Lichen Max Fail</td><td style
