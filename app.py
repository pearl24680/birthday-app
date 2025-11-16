import streamlit as st

# ------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------
st.set_page_config(page_title="Birthday Wish", layout="centered")

# ------------------------------------------------------
# LIGHT BLUE BACKGROUND
# ------------------------------------------------------
page_bg = """
<style>
body {
    background-color: #dff3ff !important;
}

/* STAR ANIMATION */
.star {
  position: fixed;
  width: 6px;
  height: 6px;
  background: white;
  border-radius: 50%;
  animation: twinkle 1.6s infinite ease-in-out;
}

@keyframes twinkle {
  0% { opacity: 0.2; transform: scale(0.8); }
  50% { opacity: 1; transform: scale(1.3); }
  100% { opacity: 0.2; transform: scale(0.8); }
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Create floating stars
for i in range(20):
    st.markdown(
        f"""
        <div class="star" style="
            top:{5*i+10}px;
            left:{15*i+20}px;
            animation-delay:{i*0.2}s;">
        </div>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------
# HEADING
# ------------------------------------------------------
st.markdown(
    """
    <h1 style="text-align:center; color:#0077cc; font-size:45px;">
        🎉 Beautiful Birthday Wish Generator 🎉
    </h1>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------
# ASK NAME
# ------------------------------------------------------
name = st.text_input("Enter the name for birthday wish:")

# ------------------------------------------------------
# CARD ONLY BIRTHDAY WISHES
# ------------------------------------------------------
if name:
    st.markdown(
        f"""
        <div style="
            background:white;
            padding:30px;
            border-radius:25px;
            text-align:center;
            margin-top:30px;
            box-shadow:0 6px 20px rgba(0,0,0,0.3);
            border:4px solid #6ec6ff;
        ">

            <h1 style="color:#008cff; font-size:42px;">
                🎈 Happy Birthday {name}! 🎈
            </h1>

            <p style="font-size:24px; color:#444; margin-top:15px;">
                Wishing you a day filled with joy, love, laughter, and endless happiness.<br>
                May all your dreams shine as bright as the stars above! ⭐💙
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # Balloons animation
    if st.button("🎈 Release Balloons!"):
        st.balloons()

# ------------------------------------------------------
# FOOTER
# ------------------------------------------------------
st.markdown(
    """
    <br><br>
    <p style="text-align:center; color:#005fa3; font-weight:600;">
        💙 Made  by Pearl for u dost💙
    </p>
    """,
    unsafe_allow_html=True
)
