import streamlit as st

st.set_page_config(page_title="Emotional Birthday Card", layout="centered")

# Soft animated background
st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #d7edff, #f0f6ff);
    animation: fadeIn 2s ease-in-out;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

/* Falling stars */
.star {
    position: fixed;
    top: -10px;
    width: 8px;
    height: 8px;
    background: #a1c7ff;
    border-radius: 50%;
    animation: fall linear infinite;
    opacity: 0.8;
}
@keyframes fall {
    0% {transform: translateY(0) scale(1);}
    100% {transform: translateY(120vh) scale(0.3);}
}
</style>
""", unsafe_allow_html=True)

# Create falling stars
for i in range(15):
    st.markdown(
        f"<div class='star' style='left:{i*6}%; animation-duration:{3+i%5}s; animation-delay:{i*0.3}s;'></div>",
        unsafe_allow_html=True
    )

# A4 Card Content
card = """
<div style="
    width: 210mm;
    min-height: 297mm;
    padding: 50px;
    margin-top: 30px;
    background: white;
    border-radius: 25px;
    border: 3px solid #82bfff;
    box-shadow: 0 0 25px #bddbff;
    text-align: center;
    font-family: 'Georgia', serif;
">

    <h1 style="color:#008cff; font-size:46px; margin-bottom:10px;">
        🎉 Happy Birthday 🌸
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
"""

st.markdown(card, unsafe_allow_html=True)
