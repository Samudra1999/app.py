import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image, ImageDraw, ImageFont
import io
import base64
import textwrap
import random
import datetime
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Teachers' Day 🎉", page_icon="🎓", layout="wide")

# ---------- Helper functions ----------
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None

def make_ecard(title, message, teacher_name, bg_color=(255, 255, 255), size=(1200, 675)):
    """Return a PNG bytes buffer for an e-card"""
    img = Image.new("RGB", size, bg_color)
    draw = ImageDraw.Draw(img)

    # Fonts - fallback to default if unavailable
    try:
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 60)
        subtitle_font = ImageFont.truetype("DejaVuSans.ttf", 32)
        small_font = ImageFont.truetype("DejaVuSans.ttf", 20)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    w, h = size
    padding = 60

    # Title
    draw.text((padding, padding), title, font=title_font, fill=(20, 20, 60))

    # Message (wrapped)
    wrapped = textwrap.fill(message, width=40)
    draw.text((padding, padding + 90), wrapped, font=subtitle_font, fill=(40, 40, 80))

    # Teacher name
    draw.text((padding, h - 140), f"To: {teacher_name}", font=subtitle_font, fill=(20, 20, 60))
    draw.text((padding, h - 90), f"From: Your student(s) — {datetime.date.today().isoformat()}", font=small_font, fill=(80, 80, 120))

    # small decorative shapes
    for i in range(8):
        x0 = random.randint(w - 300, w - 20)
        y0 = random.randint(20, h - 20)
        draw.ellipse((x0-10, y0-10, x0+10, y0+10), fill=(random.randint(100,255), random.randint(100,255), random.randint(100,255)), outline=None)

    # Save to buffer
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf

def to_download_link(buf, filename="ecard.png", label="Download e-card"):
    b64 = base64.b64encode(buf.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{b64}" download="{filename}">{label}</a>'
    return href

# ---------- Top section ----------
col1, col2 = st.columns([2, 1])

with col1:
    st.title("🎉 Happy Teachers' Day! 🎓")
    st.markdown(
        """
        Today we celebrate the mentors who shape minds, spark curiosity, and inspire the future.
        Use this page to send warm wishes, create a personalized e-card, and shower your teachers with confetti!
        """
    )
    st.write("---")

with col2:
    # Lottie animation (celebration)
    lottie_url = "https://assets10.lottiefiles.com/packages/lf20_jbrw3hcz.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=180, key="celebrate")
    else:
        st.image("https://i.imgur.com/2yaf2wb.png", width=200)  # fallback

# ---------- Confetti JS ----------
confetti_js = """
<button id="confettiBtn" style="font-size:16px;padding:10px 18px;border-radius:8px;cursor:pointer;">
🎊 Throw Confetti
</button>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
<script>
  const btn = document.getElementById("confettiBtn");
  btn.addEventListener("click", () => {
    var myConfetti = confetti.create(document.body, { resize: true, useWorker: true });
    myConfetti({ particleCount: 200, spread: 160 });
  });
</script>
"""
st.markdown(confetti_js, unsafe_allow_html=True)

st.write("---")

# ---------- Teacher list (editable) ----------
st.subheader("Teachers (edit names or add photos)")
default_teachers = [
    {"name": "Eeshani Ma'am", "note": "Thank you for your guidance!"},
    {"name": "Prateek Sir", "note": "Your lessons make learning fun!"},
    {"name": "Nawid Sir", "note": "We appreciate your support."},
    {"name": "Sonali Ma'am", "note": "You inspire us everyday."},
    {"name": "Drishti Ma'am", "note": "Thank you for believing in us."},
]

teacher_text = st.text_area("Enter teacher names and optional note (one per line, format: Name||Note). Edit to personalize.",
                            value="\n".join([f"{t['name']}||{t['note']}" for t in default_teachers]),
                            height=140)

teachers = []
for line in teacher_text.splitlines():
    if "||" in line:
        name, note = line.split("||", 1)
    else:
        name, note = line.strip(), ""
    if name:
        teachers.append({"name": name.strip(), "note": note.strip()})

# Display teacher cards
cols = st.columns(3)
for i, t in enumerate(teachers):
    with cols[i % 3]:
        st.header(t["name"])
        st.write(t["note"] or "Thanks for everything!")
        # optional photo uploader per teacher
        img_file = st.file_uploader(f"Upload photo for {t['name']} (optional)", type=["png", "jpg", "jpeg"], key=f"uploader_{i}")
        if img_file:
            img = Image.open(img_file)
            st.image(img, use_column_width=True)
        else:
            st.image("https://i.imgur.com/4AiXzf8.png", width=150)

st.write("---")

# ---------- E-card generator ----------
st.subheader("Create & download a personalized e-card")
ecard_teacher = st.selectbox("Choose a teacher", [t["name"] for t in teachers])
ecard_title = st.text_input("Card title", value="Happy Teachers' Day!")
ecard_message = st.text_area("Write your message", value="Thank you for your patience, guidance and kindness. You make a difference every day.", height=120)
bg_color_hex = st.color_picker("Pick a background color (optional)", "#FFF9E6")

if st.button("Generate e-card"):
    # convert hex to rgb tuple
    hexc = bg_color_hex.lstrip("#")
    bg_rgb = tuple(int(hexc[i:i+2], 16) for i in (0, 2, 4))
    buf = make_ecard(ecard_title, ecard_message, ecard_teacher, bg_color=bg_rgb)
    st.image(buf)
    st.markdown(to_download_link(buf, filename=f"ecard_{ecard_teacher.replace(' ','_')}.png"), unsafe_allow_html=True)

st.write("---")

# ---------- Footer + share ----------
st.markdown("Made with ❤️ — wish your teachers a wonderful day! Share this page with classmates to create more cards.")
share_url = st.experimental_get_query_params() 
# small tip
st.info("Tip: Click 'Throw Confetti' multiple times for more party!")

# Optional extra: embed a small "thank you" music (user can paste own YouTube link)
st.markdown("""
<div style="margin-top:18px">
<small>Optional: embed a short music or message video below by pasting a YouTube URL in the code if you'd like.</small>
</div>
""", unsafe_allow_html=True)
