import streamlit as st

# Page config
st.set_page_config(page_title="Happy Teachers' Day", page_icon="🎓", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #6a11cb, #2575fc);
        font-family: 'Arial', sans-serif;
    }
    .card {
        background: white;
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        max-width: 700px;
        margin: auto;
    }
    h1 {
        color: #6a11cb;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    h3 {
        color: #444;
        font-weight: normal;
        margin-bottom: 2rem;
    }
    .message {
        font-size: 1.2rem;
        line-height: 1.6;
        margin-top: 1rem;
        margin-bottom: 1rem;
        color: #333;
    }
    .signature {
        margin-top: 2rem;
        font-style: italic;
        font-size: 1.1rem;
        color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main card (✅ no st.code, no st.write)
st.markdown(
    """
    <div class="card">
        <h1>🎓 Happy Teachers' Day 💐</h1>
        <h3>5 September • With deep gratitude & respect</h3>
        
        <p class="message">
        Dear <b>Eeshani Ma’am</b>, <b>Prateek Sir</b>, <b>Nawid Sir</b>, 
        <b>Sonali Ma’am</b>, <b>Drishti Ma’am</b>, and all the amazing 
        teachers at <b>Ivy Professional School</b> —
        </p>
        
        <p class="message">
        Thank you for your wisdom, patience, and unwavering guidance.  
        You inspire us every single day to learn, grow, and achieve more 
        than we thought possible.  
        </p>
        
        <p class="message">
        Your dedication shapes our future, and for that, we are forever grateful.  
        </p>
        
        <p class="signature">— Your Students at Ivy</p>
    </div>
    """,
    unsafe_allow_html=True
)
