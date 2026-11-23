from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ACV geotérmica SNSM",
    page_icon="🌋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      header, footer {visibility: hidden;}
      .block-container {padding: 0.5rem 0.5rem 0 0.5rem; max-width: 100%;}
    </style>
    """,
    unsafe_allow_html=True,
)

base = Path(__file__).resolve().parent

# Busca index.html (o cualquier .html) en la carpeta del app o en todo el repo
candidates = [base / "index.html"]
candidates += sorted(base.glob("*.html"))
candidates += sorted(base.rglob("*.html"))
html_path = next((p for p in candidates if p.is_file()), None)

if html_path is None:
    st.error(
        "No encontré ningún archivo .html en el repositorio. "
        "Sube `index.html` a la misma carpeta que `streamlit_app.py`."
    )
    st.write("Archivos que veo en el repositorio:", [p.name for p in base.iterdir()])
else:
    html = html_path.read_text(encoding="utf-8")
    components.html(html, height=820, scrolling=False)
    st.caption("Haz clic dentro de la presentación y usa las flechas del teclado para avanzar.")
