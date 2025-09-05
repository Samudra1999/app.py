import streamlit as st

# Page config
st.set_page_config(page_title="Happy Teachers' Day", page_icon="🌸", layout="centered")

# CSS Styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ffffff, #f9f9ff);
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        font-size: 48px;
        text-align: center;
        color: #2c3e50;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #555;
        margin-bottom: 30px;
    }
    .teacher-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 12px;
        margin: 8px 0;
        background: #fff;
        font-size: 20px;
        text-align: center;
        color: #2c3e50;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.08);
    }
    .quote {
        font-size: 18px;
        text-align: center;
        font-style: italic;
        margin: 25px 0;
        color: #555;
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

# Title
st.markdown('<p class="title">🌸 Happy Teachers\' Day 🌸</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">With gratitude and respect to our mentors at <b>Ivy Professional School</b></p>', unsafe_allow_html=True)

# Quote
st.markdown('<p class="quote">"A teacher takes a hand, opens a mind, and touches a heart." ✨</p>', unsafe_allow_html=True)

st.divider()

# Teachers list in neat cards
teachers = [
    "🌟 Eeshani Ma’am",
    "🌟 Prateek Sir",
    "🌟 Nawid Sir",
    "🌟 Sonali Ma’am",
    "🌟 Drishti Ma’am",
    "🌟 and all the other wonderful teachers of Ivy Professional School"
]

for teacher in teachers:
    st.markdown(f'<div class="teacher-card">{teacher}</div>', unsafe_allow_html=True)

st.divider()

# Central Image
st.image(
    "https://img.freepik.com/free-vector/flat-design-teachers-day-background_23-2149694130.jpg",
    use_container_width=True
)

# Thank-you note
st.markdown('<p class="thanks">💐 Thank you for your guidance, patience, and wisdom. <br> We are truly grateful to you, dear teachers. 💖</p>', unsafe_allow_html=True)

# Subtle celebration
st.balloons()
