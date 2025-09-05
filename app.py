import streamlit as st
import time

# Page config
st.set_page_config(page_title="Happy Teachers' Day", page_icon="🌸", layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ffe6f0, #e6f7ff);
        color: #333333;
    }
    .title {
        font-size: 60px;
        text-align: center;
        color: #ff4c61;
        font-weight: bold;
        text-shadow: 2px 2px 5px #aaa;
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
        margin: 20px 0;
        color: #555;
    }
    .teacher-card {
        background: white;
        padding: 15px;
        margin: 10px;
        border-radius: 12px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
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

# Teachers list slideshow
teachers = ["🌟 Eeshani Ma’am", "🌟 Prateek Sir", "🌟 Nawid Sir", "🌟 Sonali Ma’am", "🌟 Drishti Ma’am", "🌟 and all other wonderful teachers at Ivy Professional School"]

placeholder = st.empty()
for teacher in teachers:
    placeholder.markdown(f'<div class="teacher-card">{teacher}</div>', unsafe_allow_html=True)
    time.sleep(1.5)

st.divider()

# Celebration
st.success("💐 Thank you for your guidance, patience, and wisdom! We are forever grateful to you, dear teachers! 💖")
st.balloons()
time.sleep(1.5)
st.snow()
