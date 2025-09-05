import streamlit as st
import time

# Page config
st.set_page_config(page_title="Happy Teachers' Day", page_icon="🌸", layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(120deg, #fdfcfb, #f7f7f7);
        font-family: 'Segoe UI', sans-serif;
        color: #2c3e50;
    }
    .hero {
        position: relative;
        text-align: center;
        margin-bottom: 30px;
    }
    .hero img {
        width: 100%;
        border-radius: 12px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
    }
    .hero-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-size: 56px;
        font-weight: bold;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
        animation: fadeIn 2.5s ease-in-out;
        background: linear-gradient(90deg, #ffd700, #ff69b4, #00c3ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #444;
        margin: 20px 0;
        animation: fadeIn 3s ease-in-out;
    }
    .quote-box {
        font-size: 20px;
        font-style: italic;
        color: #b8860b;
        text-align: center;
        margin: 25px auto;
        width: 70%;
        animation: fadeIn 2s ease-in-out;
    }
    .teacher-grid {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
        margin-top: 25px;
    }
    .teacher-card {
        flex: 1 1 250px;
        max-width: 280px;
        border: 2px solid #d4af37;
        border-radius: 12px;
        padding: 20px;
        background: #fff;
        font-size: 22px;
        text-align: center;
        font-weight: bold;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
        opacity: 0;
        animation: fadeInCard 1.5s forwards;
    }
    .thanks {
        font-size: 22px;
        text-align: center;
        color: #2c3e50;
        margin-top: 40px;
        font-weight: bold;
        animation: fadeIn 2.5s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    @keyframes fadeInCard {
        from {opacity: 0; transform: translateY(30px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown(
    """
    <div class="hero">
        <img src="https://img.freepik.com/free-vector/flat-teachers-day-background_23-2149694130.jpg" alt="Teachers Day Banner">
        <div class="hero-text">Happy Teachers' Day 🌸</div>
    </div>
    """,
    unsafe_allow_html=True
)

# Subtitle
st.markdown('<p class="subtitle">With love and gratitude to our mentors at <b>Ivy Professional School</b></p>', unsafe_allow_html=True)

# Rotating quotes
quotes = [
    "“A teacher takes a hand, opens a mind, and touches a heart.”",
    "“Teaching is the profession that creates all other professions.”",
    "“The influence of a good teacher can never be erased.”"
]
quote_placeholder = st.empty()
for q in quotes:
    quote_placeholder.markdown(f'<div class="quote-box">{q}</div>', unsafe_allow_html=True)
    time.sleep(2.8)

st.divider()

# Teachers (show in grid)
teachers = [
    "🌟 Eeshani Ma’am",
    "🌟 Prateek Sir",
    "🌟 Nawid Sir",
    "🌟 Sonali Ma’am",
    "🌟 Drishti Ma’am",
    "🌟 and all the wonderful teachers of Ivy Professional School"
]

st.markdown('<div class="teacher-grid">', unsafe_allow_html=True)
for teacher in teachers:
    st.markdown(f'<div class="teacher-card">{teacher}</div>', unsafe_allow_html=True)
    time.sleep(0.7)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# Thank-you
st.markdown('<p class="thanks">💐 Thank you for your wisdom, patience, and kindness.<br>We are forever grateful to you, dear teachers. 💖</p>', unsafe_allow_html=True)

# Grand celebration
time.sleep(1.2)
st.balloons()
time.sleep(1.2)
st.snow()
