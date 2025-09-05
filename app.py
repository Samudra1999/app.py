import streamlit as st
import time

# Page config
st.set_page_config(page_title="Happy Teachers' Day", page_icon="🌸", layout="centered")

# CSS Styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ffffff, #f7f9fc);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 50px;
        text-align: center;
        color: #2c3e50;
        font-weight: bold;
        opacity: 0;
        animation: fadeIn 2s forwards;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #444;
        margin-bottom: 25px;
        opacity: 0;
        animation: fadeIn 3s forwards;
    }
    .quote {
        font-size: 18px;
        text-align: center;
        font-style: italic;
        margin: 25px 0;
        color: #b8860b;
    }
    .teacher-card {
        border: 2px solid #d4af37;
        border-radius: 12px;
        padding: 18px;
        margin: 20px auto;
        width: 60%;
        background: #fff;
        font-size: 26px;
        text-align: center;
        color: #2c3e50;
        font-weight: bold;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        opacity: 0;
        animation: fadeInCard 1.5s forwards;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    @keyframes fadeInCard {
        from {opacity: 0; transform: translateY(15px);}
        to {opacity: 1; transform: translateY(0);}
    }
    .thanks {
        font-size: 20px;
        text-align: center;
        color: #2c3e50;
        margin-top: 30px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title + subtitle
st.markdown('<p class="title">🌸 Happy Teachers\' Day 🌸</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">With gratitude and respect to our mentors at <b>Ivy Professional School</b></p>', unsafe_allow_html=True)

# Quote
st.markdown('<p class="quote">"Teaching is the profession that creates all other professions." ✨</p>', unsafe_allow_html=True)

st.divider()

# Teacher slideshow (spotlight one by one)
teachers = [
    "🌟 Eeshani Ma’am",
    "🌟 Prateek Sir",
    "🌟 Nawid Sir",
    "🌟 Sonali Ma’am",
    "🌟 Drishti Ma’am",
    "🌟 and all the other wonderful teachers of Ivy Professional School"
]

placeholder = st.empty()
for teacher in teachers:
    placeholder.markdown(f'<div class="teacher-card">{teacher}</div>', unsafe_allow_html=True)
    time.sleep(1.8)

st.divider()

# Tribute Image
st.image(
    "https://img.freepik.com/free-vector/flat-design-teachers-day-background_23-2149694130.jpg",
    use_container_width=True
)

# Thank-you note
st.markdown('<p class="thanks">💐 Thank you for your wisdom, patience, and kindness.<br>We are forever grateful to you, dear teachers. 💖</p>', unsafe_allow_html=True)

# Subtle balloons celebration
st.balloons()
