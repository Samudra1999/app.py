import streamlit as st
from PIL import Image
import time

# Page config
st.set_page_config(page_title="Happy Teachers' Day", page_icon="🌸", layout="wide")

# Custom CSS for background & text styling
st.markdown(
    """
    <style>
    body {
        background-color: #fffaf0;
    }
    .title {
        font-size: 50px;
        text-align: center;
        color: #e75480;
        font-weight: bold;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #444;
    }
    .teacher-list {
        font-size: 20px;
        line-height: 1.8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<p class="title">🌸 Happy Teachers\' Day 🌸</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">With love and respect to our amazing teachers at <b>Ivy Professional School</b></p>', unsafe_allow_html=True)

st.divider()

# Inspirational quote
st.markdown(
    """
    > "A good teacher is like a candle — it consumes itself to light the way for others." ✨  
    """
)

# Teachers list
st.markdown("### A very warm **Happy Teachers' Day** to:")
st.markdown(
    """
    <div class="teacher-list">
    🌟 <b>Eeshani Ma’am</b><br>
    🌟 <b>Prateek Sir</b><br>
    🌟 <b>Nawid Sir</b><br>
    🌟 <b>Sonali Ma’am</b><br>
    🌟 <b>Drishti Ma’am</b><br>
    🌟 <i>and all the other wonderful teachers of Ivy Professional School</i><br>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# Two column layout
col1, col2 = st.columns(2)

with col1:
    st.image("https://img.freepik.com/free-vector/happy-teacher-s-day-background_23-2149057072.jpg", use_container_width=True)
with col2:
    st.image("https://img.freepik.com/free-photo/top-view-roses-flowers-arrangement_23-2148931045.jpg", use_container_width=True)

st.success("💐 Thank you for your guidance, patience, and wisdom! We are forever grateful to you, dear teachers! 💖")

# Celebration animation
st.balloons()
time.sleep(1.5)
st.snow()
