import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Happy Teachers' Day", page_icon="🌸", layout="centered")

# Title
st.title("🌸 Happy Teachers' Day 🌸")
st.markdown("### With love and respect to our amazing teachers at **Ivy Professional School**")

# Main message
st.markdown(
    """
    Today we celebrate the guiding lights who inspire us every day.  
    A very warm **Happy Teachers' Day** to:
    
    - 🌟 **Eeshani Ma’am**  
    - 🌟 **Prateek Sir**  
    - 🌟 **Nawid Sir**  
    - 🌟 **Sonali Ma’am**  
    - 🌟 **Drishti Ma’am**  
    - 🌟 *and all the other wonderful teachers of Ivy Professional School*  
    
    ---
    **Thank you for your guidance, patience, and wisdom!** 💐
    """
)

# Optional: Add an image (you can replace with your own image)
st.image(
    "https://img.freepik.com/free-vector/happy-teacher-s-day-background_23-2149057072.jpg",
    caption="Happy Teachers' Day",
    use_container_width=True
)

# Closing note
st.success("We are forever grateful to you, dear teachers! 💖")
