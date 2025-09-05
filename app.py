import io
from datetime import date
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# ---------- Page config ----------
st.set_page_config(page_title="Happy Teachers' Day 🎓", page_icon="🎉", layout="centered")

# ---------- Helper: load font ----------
def load_font(size=48, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except Exception:
            continue
    return ImageFont.load_default()

# ---------- Helper: text wrapping ----------
def draw_centered_multiline(draw, text, xy_center, max_width_px, font, fill):
    words = text.split()
    lines, line = [], ""
    for w in words:
        test = (line + " " + w).strip()
        if draw.textlength(test, font=font) <= max_width_px:
            line = test
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)

    line_height = font.getbbox("Ay")[3] - font.getbbox("Ay")[1] + 6
    total_h = len(lines) * line_height
    x_center, y_center = xy_center
    start_y = int(y_center - total_h / 2)

    for i, ln in enumerate(lines):
        w = draw.textlength(ln, font=font)
        x = int(x_center - w / 2)
        y = start_y + i * line_height
        draw.text((x, y), ln, font=font, fill=fill)

# ---------- Helper: create card image ----------
def make_card(teacher_name, message, from_name, base_color="#6C63FF"):
    W, H = 1200, 675
    img = Image.new("RGB", (W, H), color="white")
    draw = ImageDraw.Draw(img)

    # Gradient background
    top = Image.new("RGB", (1, 1), base_color)
    top_rgb = top.getpixel((0, 0))
    for y in range(H):
        t = y / H
        r = int(top_rgb[0] * (1 - t) + 255 * t)
        g = int(top_rgb[1] * (1 - t) + 255 * t)
        b = int(top_rgb[2] * (1 - t) + 255 * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    margin = 64
    card_bbox = (margin, margin, W - margin, H - margin)
    draw.rounded_rectangle(card_bbox, radius=40, fill=(255, 255, 255))

    # Fonts
    title_font = load_font(72, bold=True)
    sub_font = load_font(44)
    body_font = load_font(40)
    footer_font = load_font(36)

    # Title
    title = "Happy Teachers' Day"
    title_w = draw.textlength(title, font=title_font)
    draw.text(((W - title_w) / 2, margin + 40), title, font=title_font, fill=base_color)

    # Subtitle
    subtitle = "5 September • With gratitude and respect"
    sub_w = draw.textlength(subtitle, font=sub_font)
    draw.text(((W - sub_w) / 2, margin + 130), subtitle, font=sub_font, fill="#444")

    # To line
    to_line = f"Dear {teacher_name}," if teacher_name.strip() else "Dear Teacher,"
    to_w = draw.textlength(to_line, font=body_font)
    draw.text(((W - to_w) / 2, margin + 210), to_line, font=body_font, fill="#222")

    # Message
    msg = message.strip() or "Thank you for your wisdom, patience, and kindness. You inspire us every day."
    draw_centered_multiline(draw, msg, (W // 2, H // 2 + 10), int(W * 0.75), body_font, "#222")

    # Footer
    footer = f"— {from_name}" if from_name.strip() else "— Your Student"
    footer_w = draw.textlength(footer, font=footer_font)
    draw.text(((W - footer_w) / 2, H - margin - 90), footer, font=footer_font, fill="#666")

    return img

# ---------- UI ----------
st.markdown(
    """
    <div style="text-align:center; font-size: 1.75rem; line-height:1.4;">
        🎓 <b>Happy Teachers' Day</b> — celebrating the mentors who light our way.<br/>
        <span style="font-size:1rem; color:#666;">India celebrates it on 5 September in honor of Dr. Sarvepalli Radhakrishnan.</span>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("🎨 Personalize")
    teacher_name = st.text_input("Teacher's name", placeholder="e.g., Mrs. Sharma")
    message = st.text_area("Your message", height=150, placeholder="Write a heartfelt note…")
    from_name = st.text_input("Your name", placeholder="e.g., Samudra")
    base_color = st.color_picker("Accent color", value="#6C63FF")

    if st.button("Generate Card 🎁", use_container_width=True):
        st.session_state["card"] = make_card(teacher_name, message, from_name, base_color)
        st.balloons()
        st.toast("Card ready! Scroll down to preview and download.", icon="🎉")

if "card" not in st.session_state:
    st.session_state["card"] = make_card("", "", "", "#6C63FF")

st.divider()
st.subheader("Preview")
st.image(st.session_state["card"], use_column_width=True)

buf = io.BytesIO()
st.session_state["card"].save(buf, format="PNG")
png_bytes = buf.getvalue()

st.download_button(
    "Download PNG",
    data=png_bytes,
    file_name=f"teachers_day_{date.today().isoformat()}.png",
    mime="image/png",
    use_container_width=True,
)

st.caption("Tip: Share it on WhatsApp/Instagram or print it as a postcard 🌟")
