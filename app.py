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
<div style='background:black;padding:2rem;color:white;font-family:monospace;border-radius:16px;border:1px solid #10B98120;min-height:90vh'>
<h1 style='text-align:center;font-size:3rem;color:#10B981'>LICHEN.STORAGE</h1>
<p style='text-align:center;color:#10B98180'>FC-496 / CRAID / BIOLOGICAL</p>
<div style='display:flex;gap:2rem;max-width:1400px;margin:0 auto;flex-wrap:wrap'>
""", unsafe_allow_html=True)

st.markdown("""
<div style='flex:2;min-width:400px;background:rgba(31,41,55,0.4);border-radius:16px;padding:2rem;position:relative'>
<div id='integrity' style='position:absolute;top:2rem;right:2rem;font-size:2rem;color:#10B981;font-weight:bold'>INTEGRITY: 100%</div>
<canvas id='cluster' width='600' height='400' style='width:100%;height:400px;border-radius:12px;background:rgba(16,185,129,0.1);border:1px solid #10B98130;display:block'></canvas>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='flex:1;min-width:300px;display:flex;flex-direction:column;gap:1.5rem'>
<button id='apocalypse' style='width:100%;padding:1.5rem;background:linear-gradient(45deg,#ef4444,#dc2626);color:white;border:none;border-radius:12px;font-weight:bold;cursor:pointer'>💥 APOCALYPSE 60%</button>
<div id='console' style='background:black;padding:1rem;border-radius:12px;height:200px;overflow-y:auto;font-size:0.8rem;border:1px solid #333'>
> LichenCluster(10) deployed<br>> φ-topology OK
</div>
<div style='font-size:0.8rem;color:#9ca3af'>
RAID-6: 2 Drives | Lichen: 60% OK<br>Rebuild: Hours vs INSTANT
</div>
</div></div>
<div style='text-align:center;margin-top:2rem;color:#666;font-size:0.8rem'>Lichen Labs v0.9.2</div></div>
<script>
let i=100,c=document.getElementById('console'),v=document.getElementById('integrity'),a=document.getElementById('cluster'),x=a.getContext('2d'),b=document.getElementById('apocalypse');
function l(m){c.innerHTML+='> '+m+'<br>';c.scrollTop=c.scrollHeight}
b.onclick=function(){b.disabled=true;b.innerHTML='🔄 RECOVERING...';b.style.background='linear-gradient(45deg,#10B981,#059669)';l('⚠️ 60% NODES KILLED');i=40;v.textContent='INTEGRITY: '+i+'%';v.style.color='#f59e0b';let d=0,k=setInterval(()=>{x.fillStyle='rgba(239,68,68,'+(0.5-d/30)+')';x.beginPath();x.arc(Math.random()*600,Math.random()*400,25,0,Math.PI*2);x.fill();
