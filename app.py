import streamlit as st

st.set_page_config(page_title="Birthday Card", layout="centered")

st.title("💙 Birthday Card Generator")

name = st.text_input("Enter the birthday person's name:")

if name:
    st.markdown(
        f"""
        <h1 style="color:#008cff; font-size:46px; margin-bottom:10px;">
            🎉 Happy Birthday, {name}! 🌸
        </h1>

        <p style="
            font-size:24px;
            color:#34495e;
            line-height:1.8;
            margin-top:35px;
            padding: 10px 20px;
        ">
            Today is not just another day…<br>
            It is the day the world received a gentle, kind, beautiful soul. 💙<br><br>

            May your heart always find reasons to smile,
            may your dreams unfold beautifully,
            and may God bless you with peace, love, and warmth
            in every step of your journey. ✨

            You deserve all the happiness in the universe.
            I hope this birthday brings you tears of joy
            and a heart full of soft, glowing feelings. 💫💙
        </p>

        <p style="margin-top:120px; font-size:20px; color:#555;">
            — Made with love by <b>Pearl</b> —
        </p>
        """,
        unsafe_allow_html=True
    )

