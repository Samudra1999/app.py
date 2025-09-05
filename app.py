# Teacher slideshow (fade-in names)
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
            f"""
            <p class="teacher-name" style="animation: fadeInUp 1s ease-in-out;">
                {teacher}
            </p>
            """,
            unsafe_allow_html=True
        )
        time.sleep(2)  # show each name clearly
