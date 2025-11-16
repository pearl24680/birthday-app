import streamlit as st
import random
import time

st.set_page_config(page_title="Happy Birthday", layout="wide")

# --- CSS + Animations ---
st.markdown("""
<style>

body {
    background: linear-gradient(135deg,#ff9a9e,#fad0c4,#fbc2eb,#a18cd1);
    background-size: 500% 500%;
    animation: bgAnimation 12s ease infinite;
}

@keyframes bgAnimation {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.title {
    font-size: 60px;
    text-align: center;
    color: white;
    text-shadow: 3px 3px 20px black;
    animation: pop 2s infinite alternate;
}

@keyframes pop {
    from {transform: scale(1);}
    to {transform: scale(1.18);}
}

.name {
    color: yellow;
    font-size: 65px;
}

.balloon {
    position: absolute;
    animation: floatUp 7s infinite ease-in;
}

@keyframes floatUp {
    0% {transform: translateY(300px);}
    100% {transform: translateY(-500px);}
}

.footer {
    position: fixed;
    bottom: 10px;
    width: 100%;
    text-align: center;
    color: white;
    font-size: 22px;
}

</style>
""", unsafe_allow_html=True)


# --- UI Input ---
st.markdown("## 🎂 Enter Your Name For Birthday Wish")
name = st.text_input("Your Name:")
btn = st.button("Show Birthday Wish 🎉")

if btn and name.strip() != "":
    st.markdown(f"""
    <h1 class="title">🎉 Happy Birthday <span class="name">{name}</span> 🎂</h1>
    """, unsafe_allow_html=True)

    # Background music
    st.audio("https://www.dropbox.com/scl/fi/8s4dq6pr2jke5ihj9tqpt/happy.mp3?rlkey=xyz&raw=1")

    # Balloons animation
    for i in range(20):
        x = random.randint(10, 90)
        color = random.choice(["red", "yellow", "cyan", "pink", "violet"])
        st.markdown(
            f"""
            <div class="balloon" style="left:{x}%; bottom:0px; width:60px; height:90px; background:{color}; border-radius:50%;"></div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(0.2)

# Footer
st.markdown("""
<div class="footer">Made by <b>Pearl</b></div>
""", unsafe_allow_html=True)
