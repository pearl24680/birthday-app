import streamlit as st

st.set_page_config(page_title="Birthday Card", layout="centered")

st.title("💙 Birthday Card Generator")

# Name input
name = st.text_input("Enter the birthday person's name:")

if name:
    st.markdown(
        f"""
        <div style="
            width: 210mm;
            min-height: 297mm;
            padding: 50px;
            margin-top: 20px;
            background: white;
            border-radius: 25px;
            border: 3px solid #82bfff;
            box-shadow: 0 0 25px #bddbff;
            text-align: center;
            font-family: 'Georgia', serif;
        ">

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

                May your heart always find reasons to smile,<br>
                may your dreams unfold beautifully,<br>
                and may God bless you with peace, love, and warmth<br>
                in every step of your journey. ✨<br><br>

                You deserve all the happiness in the universe.<br>
                I hope this birthday brings you tears of joy<br>
                and a heart full of soft, glowing feelings. 💫💙
            </p>

            <p style="margin-top:120px; font-size:20px; color:#555;">
                — Made with love by <b>Pearl</b> —
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )
