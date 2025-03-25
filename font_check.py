import streamlit as st

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Orbitron&family=Garamond&family=Courier+Prime&family=Arial&display=swap');

    .serif { font-family: 'Garamond', serif; font-size: 24px; }
    .sans-serif { font-family: 'Arial', sans-serif; font-size: 24px; }
    .monospace { font-family: 'Courier Prime', monospace; font-size: 24px; }
    .handwriting { font-family: 'Pacifico', cursive; font-size: 24px; }
    .futuristic { font-family: 'Orbitron', sans-serif; font-size: 24px; }

    </style>

    <p class="serif">Garamond (Serif Font)</p>
    <p class="sans-serif">Arial (Sans-serif Font)</p>
    <p class="monospace">Courier Prime (Monospace Font)</p>
    <p class="handwriting">Pacifico (Handwriting Font)</p>
    <p class="futuristic">Orbitron (Futuristic Font)</p>
    """,
    unsafe_allow_html=True
)
