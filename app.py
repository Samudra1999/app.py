import streamlit as st
import time

# Page config
st.set_page_config(page_title="Happy Teachers' Day", page_icon="🌸", layout="centered")

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(120deg, #faf8f5, #fffdf8);
        font-family: 'Segoe UI', sans-serif;
        color: #2c3e50;
    }
    .hero {
        text-align: center;
        margin-bottom: 25px;
    }
    .title {
        font-size: 56px;
        font-weight: bold;
        color: #2c3e50;
        text-shadow: 1px 1px 6px rgba(0,0,0,0.15);
        animation: fadeIn 2s ease-in-out;
    }
    .subtitle {
        font-size: 22px;
        margin-top: -10px;
        color: #555;
        animation: fadeIn 3s ease-in-out;
    }
    .quote-box {
        font-size: 18px;
        font-style: italic;
        color: #b8860b;
        text-align: center;
        margin: 25px auto;
        width: 70%;
        animation: fadeIn 2.5s ease-in-out;
    }
    .teacher-card {
        border: 2px solid #d4af37;
        border-radius: 12px;
        padding: 18px;
        margin: 15px auto;
        width: 65%;
        background: #fff;
        font-size: 26px;
        text-align: center;
        font-weight: bold;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
        opacity: 0;
        animation: fadeInCard 1.5s forwards;
    }
    .thanks {
        font-size: 20px;
        text-align: center;
        color: #2c3e50;
        margin-top: 35px;
        font-weight: bold;
        animation: fadeIn 2.5s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    @keyframes fadeInCard {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Hero Image
st.markdown('<div class="hero"><img src="https://img.freepik.com/free-vector/flat-teachers-day-illustration_23-2149693083.jpg" width="600"></div>', unsafe_allow_html=True)

# Title + subtitle
st.markdown('<p class="title">🌸 Happy Teachers\' Day 🌸</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">With gratitude and respect to our mentors at <b>Ivy Professional School</b></p>', unsafe_allow_html=True)

# Dynamic quotes rotation
quotes = [
    "“A teacher takes a hand, opens a mind, and touches a heart.”",
    "“Teaching is the profession that creates all other professions.”",
    "“The influence of a good teacher can never be erased.”"
]

quote_placeholder = st.empty()
for q in quotes:
    quote_placeholder.markdown(f'<div class="quote-box">{q}</div>', unsafe_allow_html=True)
    time.sleep(2.5)

st.divider()

# Teacher spotlight slideshow
teachers = [
    "🌟 Eeshani Ma’am",
    "🌟 Prateek Sir",
    "🌟 Nawid Sir",
    "🌟 Sonali Ma’am",
    "🌟 Drishti Ma’am",
    "🌟 and all the wonderful teachers of Ivy Professional School"
]

placeholder = st.empty()
for teacher in teachers:
    placeholder.markdown(f'<div class="teacher-card">{teacher}</div>', unsafe_allow_html=True)
    time.sleep(2)

st.divider()

# Thank-you note
st.markdown('<p class="thanks">💐 Thank you for your wisdom, patience, and kindness.<br>We are forever grateful to you, dear teachers. 💖</p>', unsafe_allow_html=True)

# Celebration
time.sleep(1.5)
st.balloons()
time.sleep(1)
st.snow()
