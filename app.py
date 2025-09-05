import streamlit as st
import time
import itertools

# Page config
st.set_page_config(page_title="Happy Teachers' Day", page_icon="🌸", layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(-45deg, #ffdee9, #b5fffc, #ffe6f7, #d4fc79);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        font-family: 'Trebuchet MS', sans-serif;
    }
    @keyframes gradient {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .title {
        font-size: 55px;
        text-align: center;
        color: #ff4c61;
        font-weight: bold;
        text-shadow: 2px 2px 8px #888;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #222;
        margin-bottom: 20px;
    }
    .teacher-card {
        background: white;
        padding: 20px;
        margin: 10px;
        border-radius: 15px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .teacher-card:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 20px rgba(0,0,0,0.3);
    }
    .quote {
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin: 25px 0;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Typing effect for Title
title_text = "🌸 Happy Teachers' Day 🌸"
placeholder = st.empty()
typed_text = ""
for char in title_text:
    typed_text += char
    placeholder.markdown(f'<p class="title">{typed_text}</p>', unsafe_allow_html=True)
    time.sleep(0.05)

st.markdown('<p class="subtitle">With love and respect to our amazing teachers at <b>Ivy Professional School</b></p>', unsafe_allow_html=True)

# Quote
st.markdown('<p class="quote">"A good teacher is like a candle — it consumes itself to light the way for others." ✨</p>', unsafe_allow_html=True)

st.divider()

# Teachers list as glowing cards
teachers = ["🌟 Eeshani Ma’am", "🌟 Prateek Sir", "🌟 Nawid Sir", "🌟 Sonali Ma’am", "🌟 Drishti Ma’am", "🌟 and all other wonderful teachers at Ivy Professional School"]

cols = st.columns(3)
for idx, teacher in enumerate(teachers):
    with cols[idx % 3]:
        st.markdown(f'<div class="teacher-card">{teacher}</div>', unsafe_allow_html=True)

st.divider()

# Image carousel simulation
images = [
    "https://img.freepik.com/free-vector/happy-teacher-s-day-background_23-2149057072.jpg",
    "https://img.freepik.com/free-photo/top-view-roses-flowers-arrangement_23-2148931045.jpg",
    "https://img.freepik.com/free-vector/hand-drawn-flat-design-teachers-day-background_23-2149694125.jpg"
]

st.markdown("### 🌼 A small token of love 🌼")
img_placeholder = st.empty()
for i in itertools.cycle(images):
    img_placeholder.image(i, use_container_width=True)
    time.sleep(2)  # change image every 2 seconds

# Celebration
st.success("💐 Thank you for your guidance, patience, and wisdom! We are forever grateful to you, dear teachers! 💖")
st.balloons()
time.sleep(1.5)
st.snow()
