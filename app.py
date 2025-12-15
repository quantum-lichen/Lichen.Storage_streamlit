import streamlit as st

st.set_page_config(page_title="🟢 LICHEN STORAGE", layout="wide')

st.markdown("""
<style>
.main {background-color: black;}
.stApp {background-color: black;}
[data-testid="stAppViewContainer"] {background-color: black;}
</style>
""", unsafe_allow_html=True)

html = '''
<div style="
    background: linear-gradient(135deg, #000000 0%, #0a0a0a 100%); 
    padding: 2rem; 
    border-radius: 16px; 
    border: 1px solid rgba(16,185,129,0.2);
    min-height: 90vh;
    color: white;
    font-family: monospace;
">
    <h1 style="
        text-align: center; 
        font-size: 3rem; 
        background: linear-gradient(45deg, white, #10B981); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        margin-bottom: 1rem;
    ">LICHEN<span style="color: #10B981;">.STORAGE</span></h1>
    
    <p style="text-align: center; color: #10B981; font-size: 1rem; margin-bottom: 2rem;">
        FC-496 / CRAID / BIOLOGICAL
    </p>

    <div style="display: flex; gap: 2rem; max-width: 1400px; margin: 0 auto;">
        
        <!-- VISUALIZER -->
        <div style="flex: 2; background: rgba(31,41,55,0.4); border-radius: 16px; padding: 2rem; position: relative;">
            <div id="integrity" style="
                position: absolute; 
                top: 2rem; 
                right: 2rem; 
                font-size: 2rem; 
                font-weight: bold; 
                color: #10B981;
            ">INTEGRITY: 100%</div>
            
            <canvas id="cluster" width="600" height="400" style="
                width: 100%; 
                height: 400px; 
                border-radius: 12px; 
                background: radial-gradient(circle, rgba(16,185,129,0.1) 0%, black 70%);
                border: 1px solid rgba(16,185,129,0.3);
                display: block;
                margin: 0 auto;
            "></canvas>
        </div>

        <!-- CONTROLS -->
        <div style="flex: 1; display: flex; flex-direction: column; gap: 1.5rem;">
            
            <button id="apocalypse" style="
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
            ">💥 SIMULATE APOCALYPSE<br><span style="
