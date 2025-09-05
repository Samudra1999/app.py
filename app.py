import streamlit as st
import time

# Page config
st.set_page_config(page_title="Happy Teachers' Day", page_icon="🌸", layout="centered")

# CSS with animations
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
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        width: 120px;
        height: auto;
        object-fit: contain;
        animation: float 3s ease-in-out infinite;
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
        animation: glow 1.5s ease-in-out infinite alternate;
    }
    .thanks {
        font-size: 22px;
        text-align: center;
        color: #b8860b;
        margin-top: 30px;
        font-weight: bold;
        animation: pulse 2s infinite;
    }
    .center-image img {
        border-radius: 20px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        margin-top: 20px;
        margin-bottom: 20px;
        width: 100%;
        max-width: 700px;
        height: auto;
        object-fit: contain;
        display: block;
        margin-left: auto;
        margin-right: auto;
        animation: zoomIn 2s ease-in-out;
    }
    /* Animations */
    @keyframes fadeIn { from {opacity: 0;} to {opacity: 1;} }
    @keyframes fadeInUp { from {opacity: 0; transform: translateY(30px);} to {opacity: 1; transform: translateY(0);} }
    @keyframes fadeInDown { from {opacity: 0; transform: translateY(-30px);} to {opacity: 1; transform: translateY(0);} }
    @keyframes float { 0% { transform: translateY(0px);} 50% { transform: translateY(-10px);} 100% { transform: translateY(0px);} }
    @keyframes glow {
        from { text-shadow: 0 0 5px #e75480, 0 0 10px #ffb6c1; }
        to { text-shadow: 0 0 15px #ff69b4, 0 0 30px #ff1493; }
    }
    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }
    @keyframes zoomIn { from { transform: scale(0.8); opacity: 0; } to { transform: scale(1); opacity: 1; } }
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

# Teacher slideshow (fade-in names)
teachers = [
    "🌟 Eeshani Ma’am",
    "🌟 Prateek Sir",
    "🌟 Nawid Sir",
    "🌟 Sonali Ma’am",
    "🌟 Drishti Ma’am",
    "🌟 And all other wonderful teachers at Ivy Professional School"
]

placeholder = st.empty()

for _ in range(3):  # loop cycles
    for teacher in teachers:
        placeholder.markdown(
            f"""
            <p class="teacher-name" style="animation: fadeInUp 1s ease-in-out;">
                {teacher}
            </p>
            """,
            unsafe_allow_html=True
        )
        time.sleep(2)  # each name stays for 2 seconds

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
