import streamlit as st
import time

# Page config
st.set_page_config(page_title="Happy Teachers' Day", page_icon="🌸", layout="centered")

# CSS Styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #fffaf0, #e6f7ff);
        font-family: 'Trebuchet MS', sans-serif;
    }
    .title {
        font-size: 54px;
        text-align: center;
        color: #d6336c;
        font-weight: bold;
        text-shadow: 2px 2px 8px #aaa;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #333;
        margin-bottom: 25px;
    }
    .quote {
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin: 25px 0;
        color: #b8860b;
    }
    .teacher-box {
        border: 2px solid #d4af37;
        border-radius: 12px;
        padding: 12px;
        margin: 15px auto;
        width: 60%;
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        color: #2c3e50;
        background: #fff;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
        opacity: 0;
        animation: fadeIn 1.5s forwards;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
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

# Teacher names with fade-in effect
teachers = [
    "🌟 Eeshani Ma’am",
    "🌟 Prateek Sir",
    "🌟 Nawid Sir",
    "🌟 Sonali Ma’am",
    "🌟 Drishti Ma’am",
    "🌟 and all other wonderful teachers at Ivy Professional School"
]

for teacher in teachers:
    st.markdown(f'<div class="teacher-box">{teacher}</div>', unsafe_allow_html=True)
    time.sleep(1.2)

st.divider()

# Central Image
st.image("https://img.freepik.com/free-photo/top-view-roses-flowers-arrangement_23-2148931045.jpg", use_container_width=True)

# Thank you note
st.markdown('<p class="thanks">💐 Thank you for your guidance, patience, and wisdom! <br> We are forever grateful to you, dear teachers! 💖🎊</p>', unsafe_allow_html=True)

# Celebration
st.balloons()
