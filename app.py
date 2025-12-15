import streamlit as st

st.set_page_config(page_title="🟢 LICHEN STORAGE", layout="wide")

st.markdown("""
<style>
.main {background-color: black;}
.stApp {background-color: black;}
[data-testid="stAppViewContainer"] {background-color: black;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style='background: linear-gradient(135deg, #000 0%, #0a0a0a 100%); padding: 2rem; border-radius: 16px; border: 1px solid rgba(16,185,129,0.2); min-height: 90vh; color: white; font-family: monospace;'>
    <h1 style='text-align: center; font-size: 3rem; color: #10B981; font-weight: bold; margin-bottom: 1rem;'>LICHEN<span style='color: white;'>.STORAGE</span></h1>
    <p style='text-align: center; color: #10B98180; font-size: 1rem; margin-bottom: 2rem;'>FC-496 / CRAID / BIOLOGICAL</p>
    
    <div style='display: flex; gap: 2rem; max-width: 1400px; margin: 0 auto;'>
        
        <div style='flex: 2; background: rgba(31,41,55,0.4); border-radius: 16px; padding: 2rem; position: relative;'>
            <div id='integrity' style='position: absolute; top: 2rem; right: 2rem; font-size: 2rem; font-weight: bold; color: #10B981;'>INTEGRITY: 100%</div>
            <canvas id='cluster' width='600' height='400' style='width: 100%; height: 400px; border-radius: 12px; background: radial-gradient(circle, rgba(16,185,129,0.1) 0%, black 70%); border: 1px solid rgba(16,185,129,0.3); display: block; margin: 0 auto;'></canvas>
        </div>

        <div style='flex: 1; display: flex; flex-direction: column; gap: 1.5rem;'>
            <button id='apocalypse' style='width: 100%; padding: 1.5rem; background: linear-gradient(45deg, #ef4444, #dc2626); color: white; border: none; border-radius: 12px; font-weight: bold; font-size: 1.1rem; cursor: pointer;'>💥 SIMULATE APOCALYPSE<br><span style="font-size: 0.8rem; opacity: 0.8">KILL 60% NODES</span></button>
            
            <div style='background: rgba(31,41,55,0.6); padding: 1.5rem; border-radius: 12px; border: 1px solid rgba(16,185,129,0.2); font-size: 0.85rem;'>
                <div style='margin-bottom: 0.5rem; color: #9ca3af;'>RAID-6 Max Fail</div>
                <div style='color: #ef4444; font-weight: bold;'>2 Drives</div>
                <div style='margin-top: 1rem; color: #9ca3af;'>Lichen Max Fail</div>
                <div style='color: #10B981; font-weight: bold;'>60% NODES</div>
                <div style='margin-top: 1rem; color: #9ca3af;'>Rebuild Time</div>
                <div style='color: #10B981; font-weight: bold;'>INSTANT</div>
            </div>

            <div id='console' style='background: rgba(0,0,0,0.8); padding: 1rem; border-radius: 12px; height: 200px; overflow-y: auto; font-size: 0.75rem; border: 1px solid #333;'>
                > LichenCluster(10) deployed<br>> φ-topology active<br>> CRAID-496 ready
            </div>
        </div>
    </div>
    
    <div style='text-align: center; margin-top: 2rem; color: #6b7280; font-size: 0.8rem'>
        Built by Lichen Labs | v0.9.2-alpha
    </div>
</div>

<script>
let integrity = 100;
const consoleEl = document.getElementById('console');
const integrityEl = document.getElementById('integrity');
const canvas = document.getElementById('cluster');
const ctx = canvas.getContext('2d');
const apocBtn = document.getElementById('apocalypse');

function addLog(msg) {
    consoleEl.innerHTML += '> ' + msg + '<br>';
    consoleEl.scrollTop = consoleEl.scrollHeight;
}

function triggerApocalypse() {
    apocBtn.disabled = true;
    apocBtn.innerHTML = '🔄 RECONSTRUCTING...';
    apocBtn.style.background = 'linear-gradient(45deg, #10B981, #059669)';
    
    addLog('⚠️ SIMULATING CATASTROPHIC FAILURE...');
    integrity = 40;
    integrityEl.textContent = 'INTEGRITY: ' + integrity + '%';
    integrityEl.style.color = '#f59e0b';
    
    let destroyed = 0;
    const interval = setInterval(() => {
        ctx.fillStyle = 'rgba(239,68,68,' + (0.5 - destroyed/30) + ')';
        ctx.beginPath();
        ctx.arc(Math.random()*canvas.width, Math.random()*canvas.height, 20 + Math.random()*20, 0, Math.PI*2);
        ctx.fill();
        destroyed++;
        if (destroyed > 25) {
            clearInterval(interval);
            setTimeout(() => {
                addLog('✅ CRAID-496: DATA RECOVERED 100%');
                integrity = 100;
                integrityEl.textContent = 'INTEGRITY: ' + integrity + '%';
                integrityEl.style
