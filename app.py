import streamlit as str

# Set konfigurasi halaman streamlit
str.set_page_config(page_title="Informasi Rekening Nurmayasari Usman", page_icon="💳", layout="centered")

# Fungsi untuk membaca file eksternal
def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

try:
    # Membaca kode dari file terpisah
    html_content = load_file("index.html")
    css_content = load_file("style.css")
    js_content = load_file("script.js")

    # Menyisipkan CSS dan JS langsung ke dalam HTML untuk kebutuhan render Streamlit Component
    full_html = f"""
    <style>
    {css_content}
    </style>
    {html_content}
    <script>
    {js_content}
    </script>
    """

    # Menampilkan ke halaman web Streamlit (menggunakan tinggi 700px agar pas di mobile/desktop)
    str.components.v1.html(full_html, height=750, scrolling=True)

except FileNotFoundError as e:
    str.error(f"Gagal memuat file halaman: {e}. Pastikan file index.html, style.css, dan script.js berada di folder yang sama.")