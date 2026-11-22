from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ACV geotérmica SNSM",
    page_icon="🌋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Quita márgenes para que la presentación ocupe la pantalla
st.markdown(
    """
    <style>
      header, footer {visibility: hidden;}
      .block-container {padding: 0.5rem 0.5rem 0 0.5rem; max-width: 100%;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=820, scrolling=False)
st.caption("Haz clic dentro de la presentación y usa las flechas del teclado para avanzar.")
