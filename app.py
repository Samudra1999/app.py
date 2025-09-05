import streamlit as st
import time

# Page config
st.set_page_config(page_title="Happy Teachers' Day", page_icon="🌸", layout="centered")

# CSS with advanced animations
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #fff0f5, #e6f7ff);
        font-family: 'Trebuchet MS', sans-serif;
    }
    .header {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        margin-bottom: 20px;
        animation: fadeDown 1.5s ease-in-out;
    }
    .header img {
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        width: 120px;
        height: auto;
        object-fit: contain;
        animation: smoothFloat 6s ease-in-out infinite;
    }
    .title {
        font-size: 50px;
        text-align: center;
        font-weight: bold;
        margin: 0;
        background: linear-gradient(90deg, #ff0080, #ff8c00, #40e0d0, #8a2be2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 300% 300%;
        animation: rainbow 8s linear infinite, bounceIn 2s ease-in-out;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #444;
        animation: fadeIn 2.5s ease-in-out;
    }
    .quote {
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin: 25px 0;
        color: #b8860b;
        animation: fadeInUp 3s ease-in-out;
    }
    .teacher-name {
        font-size: 28px;
        text-align: center;
        margin: 20px 0;
        font-weight: bold;
        color: #2c3e50;
        opacity: 0;
        animation: fadeInOut 4s ease-in-out;
    }
    .thanks {
        font-size: 24px;
        text-align: center;
        color: #b8860b;
        margin-top: 30px;
        font-weight: bold;
        animation: softGlow 3s ease-in-out infinite, pulse 2s infinite;
    }
    .center-image img {
        border-radius: 20px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.4);
        margin-top: 20px;
        margin-bottom: 20px;
        width: 100%;
        max-width: 700px;
        height: auto;
        object-fit: contain;
        display: block;
        margin-left: auto;
        margin-right: auto;
        animation: zoomIn 2s ease-in-out, smoothFloat 10s ease-in-out infinite, glowCycle 6s ease-in-out infinite;
    }

    /* Animations */
    @keyframes fadeIn { from {opacity: 0;} to {opacity: 1;} }
    @keyframes fadeInUp { from {opacity: 0; transform: translateY(30px);} to {opacity: 1; transform: translateY(0);} }
    @keyframes fadeDown { from {opacity: 0; transform: translateY(-20px);} to {opacity: 1; transform: translateY(0);} }
    @keyframes smoothFloat { 0% { transform: translateY(0);} 50% { transform: translateY(-15px);} 100% { transform: translateY(0);} }
    @keyframes rainbow { 0%{background-position:0% 50%} 100%{background-position:100% 50%} }
    @keyframes fadeInOut {
        0% {opacity: 0;}
        10% {opacity: 1;}
        90% {opacity: 1;}
        100% {opacity: 0;}
    }
    @keyframes softGlow {
        0%, 100% { text-shadow: 0 0 8px #ffd700; }
        50% { text-shadow: 0 0 20px #ff8c00; }
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1);}
        50% { transform: scale(1.05);}
    }
    @keyframes glowCycle {
        0% { box-shadow: 0 0 15px #ffb6c1, 0 0 30px #ff69b4; }
        50% { box-shadow: 0 0 25px #8a2be2, 0 0 50px #ff1493; }
        100% { box-shadow: 0 0 15px #ffb6c1, 0 0 30px #ff69b4; }
    }
    @keyframes bounceIn {
        0% { transform: scale(0.8); opacity: 0; }
        50% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); opacity: 1; }
    }
    @keyframes zoomIn { from { transform: scale(0.9); opacity: 0;} to { transform: scale(1); opacity: 1;} }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown(
    """
    <div class="header">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgL3d58H6NKqxPg06OCN9k_RgI6pCwlQ43tg&s" />
        <p class="title">🌸 Happy Teachers' Day 🌸</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Subtitle & Quote
st.markdown('<p class="subtitle">With love and respect to our amazing teachers at <b>Ivy Professional School</b></p>', unsafe_allow_html=True)
st.markdown('<p class="quote">"A good teacher is like a candle — it consumes itself to light the way for others." ✨</p>', unsafe_allow_html=True)

st.divider()

# Teacher slideshow (smooth fade in/out carousel)
teachers = [
    "🌟 Eeshani Ma’am",
    "🌟 Prateek Sir",
    "🌟 Nawid Sir",
    "🌟 Sonali Ma’am",
    "🌟 Drishti Ma’am",
    "🌟 and all other wonderful teachers at Ivy Professional School"
]

placeholder = st.empty()

for _ in range(3):  # loop cycles
    for teacher in teachers:
        placeholder.markdown(
            f"<p class='teacher-name'>{teacher}</p>",
            unsafe_allow_html=True
        )
        time.sleep(4)  # sync with fadeInOut animation

st.divider()

# Central Image
st.markdown(
    """
    <div class="center-image">
        <img src="https://img.freepik.com/free-vector/happy-teachers-day_52683-44814.jpg?semt=ais_incoming&w=740&q=80" />
    </div>
    """,
    unsafe_allow_html=True
)

# Thank you note
st.markdown('<p class="thanks">💐 Thank you for your guidance, patience, and wisdom! We are forever grateful to you, dear teachers! 💖</p>', unsafe_allow_html=True)

# Celebration
st.balloons()
st.snow()
