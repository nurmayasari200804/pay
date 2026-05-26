import streamlit as st

st.set_page_config(page_title="Informasi Rekening - Nurmayasari Usman", page_icon="💳", layout="wide")

# Reset default margin Streamlit agar komponen HTML menyatu sempurna
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        padding-top: 0rem;
        background-color: #fffbf2;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 100% !important;
    }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

try:
    html_code = load_file("index.html")
    css_code = load_file("style.css")
    js_code = load_file("script.js")

    full_code = f"""
    <style>{css_code}</style>
    {html_code}
    <script>{js_code}</script>
    """

    # Mengatur tinggi wadah agar pas tanpa scroll ganda di Streamlit Cloud
    st.components.v1.html(full_code, height=1100, scrolling=True)

except Exception as e:
    st.error(f"Gagal memuat komponen: {e}")