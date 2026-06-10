import streamlit as st



st.set_page_config(
    page_title="Engelden Kaçan Robot",
    page_icon="🤖",
    layout="wide"
)
# Beyaz tema CSS ile zorla
st.markdown("""
<style>
    .stApp {
        background-color: #FFFFFF;
        color: #1A1A1A;
    }
    [data-testid="stHeader"] {
        background-color: #FFFFFF;
    }
    [data-testid="stSidebar"] {
        background-color: #F5F5F5;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #1A1A1A !important;
    }
    p, span, div {
        color: #1A1A1A;
    }
    [data-testid="stMetricValue"] {
        color: #B41E32;
    }
</style>
""", unsafe_allow_html=True)

# --- BAŞLIK ---
col1, col2 = st.columns([1, 4])
with col1:
    st.image("assets/hitit_logo.png", width=100)
with col2:
    st.title("Engelden Kaçan Robot")
    st.caption("Rıdvan Koçak · 244210071 · Mikrodenetleyici Proje Videosu")

st.divider()

# --- PROJE VİDEOSU ---
st.header("🎬 Proje Videosu")
st.video("https://youtu.be/1oLlbrZzcW0")

st.divider()

# --- PROJE HAKKINDA ---
st.header("📋 Proje Hakkında")
st.markdown("""
Bu projede **Arduino tabanlı**, ultrasonik sensör ile önündeki engelleri 
algılayıp otonom olarak yön değiştiren bir robot tasarlandı. 

**Kullanılan bileşenler:**
- Arduino Uno
- HC-SR04 Ultrasonik mesafe sensörü
- L298N motor sürücü
- 2x DC motor + tekerlek seti
- 9V batarya
""")

# --- DEVRE ŞEMASI ---
st.header("⚡ Devre Şeması")
st.image("assets/devre_semasi.png", caption="Robot devre bağlantı şeması")



# --- SONUÇLAR ---
st.header("✅ Sonuçlar")
col1, col2, col3 = st.columns(3)
col1.metric("Algılama mesafesi", "30 cm")
col2.metric("Tepki süresi", "~200 ms")
col3.metric("Çalışma süresi", "~45 dk")

st.divider()
st.caption("Hitit Üniversitesi · 2026")
