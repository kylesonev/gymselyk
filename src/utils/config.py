from pathlib import Path
from PIL import Image
import streamlit as st


def set_page_config(title: str):
    icon = Image.open(Path(__file__).parent.parent.parent / "images" / "gymselyk.ico")
    st.set_page_config(page_title=title, page_icon=icon)
