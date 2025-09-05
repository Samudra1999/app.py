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
    .header {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        margin-bottom: 20px;
        animation: fadeIn 2s ease-in-out;
    }
    .header img {
        border-radius: 12px;   /* square with rounded corners */
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        width: 120px;
        height: auto;
        object-fit: contain;   /* show full image */
    }
    .title {
        font-size: 48px;
        text-align: center;
        color: #e75480;
        font-weight: bold;
        margin: 0;
        animation: fadeInDown 2s ease-in-out;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #444;
        animation: fadeIn 3s ease-in-out;
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
        color: #2c3e50;
        font-weight: bold;
        animation: fadeIn 1s ease-in-out;
    }
    .thanks {
        font-size: 22px;
        text-align: center;
        color: #b8860b;
        margin-top: 30px;
        font-weight: bold;
        animation: fadeInUp 3s ease-in-out;
    }
    /* Central image styling */
    .center-image img {
        border-radius: 20px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        margin-top: 20px;
        margin-bottom: 20px;
        width: 100%;
        max-width: 700px;   /* keep it neat */
        height: auto;
        object-fit: contain;  /* no cropping */
        display: block;
        margin-left: auto;
        margin-right: auto;
        animation: fadeIn 2s ease-in-out;
    }
    /* Animations */
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    @keyframes fadeInUp {
        from {opacity: 0; transform: translateY(30px);}
        to {opacity: 1; transform: translateY(0);}
    }
    @keyframes fadeInDown {
        from {opacity: 0; transform: translateY(-30px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header (logo + title)
st.markdown(
    """
    <div class="header">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgL3d58H6NKqxPg06OCN9k_RgI6pCwlQ43tg&s" />
        <p class="title">🌸 Happy Teachers' Day 🌸</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Subtitle
st.markdown('<p class="subtitle">With love and respect to our amazing teachers at <b>Ivy Professional School</b></p>', unsafe_allow_html=True)

# Quote
st.markdown('<p class="quote">"A good teacher is like a candle — it consumes itself to light the way for others." ✨</p>', unsafe_allow_html=True)

st.divider()

# Teacher slideshow (continuous loop)
teachers = [
    "🌟 Eeshani Ma’am",
    "🌟 Prateek Sir",
    "🌟 Nawid Sir",
    "🌟 Sonali Ma’am",
    "🌟 Drishti Ma’am",
    "🌟 and all other wonderful teachers at Ivy Professional School"
]

placeholder = st.empty()

# Looping names
for _ in range(3):   # change to while True for infinite loop
    for teacher in teachers:
        placeholder.markdown(f'<p class="teacher-name">{teacher}</p>', unsafe_allow_html=True)
        time.sleep(1.5)

st.divider()

# Central image with frame and animation
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
