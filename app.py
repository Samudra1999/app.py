import streamlit as st
import time

# Page config
st.set_page_config(page_title="Happy Teachers' Day", page_icon="🌸", layout="centered")

# CSS
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #fff0f5, #e6f7ff);
        font-family: 'Trebuchet MS', sans-serif;
    }
    .title {
        font-size: 52px;
        text-align: center;
        color: #e75480;
        font-weight: bold;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #444;
    }
    .quote {
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin: 25px 0;
        color: #b8860b;
    }
    .teacher-name {
        font-size: 28px;
        text-align: center;
        margin: 20px 0;
        color: #2c3e50;
        font-weight: bold;
    }
    .thanks {
        font-size: 22px;
        text-align: center;
        color: #b8860b;
        margin-top: 30px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<p class="title">🌸 Happy Teachers\' Day 🌸</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">With love and respect to our amazing teachers at <b>Ivy Professional School</b></p>', unsafe_allow_html=True)

# Quote
st.markdown('<p class="quote">"A good teacher is like a candle — it consumes itself to light the way for others." ✨</p>', unsafe_allow_html=True)

st.divider()

# Teacher slideshow (one by one)
teachers = [
    "🌟 Eeshani Ma’am",
    "🌟 Prateek Sir",
    "🌟 Nawid Sir",
    "🌟 Sonali Ma’am",
    "🌟 Drishti Ma’am",
    "🌟 and all other wonderful teachers at Ivy Professional School"
]

placeholder = st.empty()
for teacher in teachers:
    placeholder.markdown(f'<p class="teacher-name">{teacher}</p>', unsafe_allow_html=True)
    time.sleep(1.5)

st.divider()

# Central image
st.image("https://img.freepik.com/free-vector/happy-teacher-s-day-background_23-2149057072.jpg", use_container_width=True)

# Thank you note
st.markdown('<p class="thanks">💐 Thank you for your guidance, patience, and wisdom! We are forever grateful to you, dear teachers! 💖</p>', unsafe_allow_html=True)

# Celebration
st.balloons()
