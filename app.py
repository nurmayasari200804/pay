import streamlit as st
import streamlit.components.v1 as components
import os

# Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Informasi Rekening dan E-Wallet",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Menghilangkan padding & header bawaan Streamlit agar tampilan penuh (full screen)
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
        iframe {
            width: 100% !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Fungsi untuk membaca file
def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Membaca HTML, CSS, dan JS
html_content = read_file("index.html")
css_content = read_file("style.css")
js_content = read_file("script.js")

# Menggabungkan CSS & JS langsung ke dalam HTML agar dapat di-render dengan sempurna
full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        {css_content}
    </style>
</head>
<body>
    {html_content.replace('<link rel="stylesheet" href="style.css">', '').replace('<script src="script.js"></script>', '')}
    <script>
        {js_content}
    </script>
</body>
</html>
"""

# Render tampilan web di Streamlit
components.html(full_html, height=1000, scrolling=True)
