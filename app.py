import streamlit as st
import random
import time

st.set_page_config(page_title="Birthday Card", layout="wide")

# --- CSS Birthday Card Design ---
st.markdown("""
<style>

body {
    background: linear-gradient(135deg,#f6d365,#fda085,#fbc2eb,#a6c1ee);
    background-size: 500% 500%;
    animation: bgAnimation 12s ease infinite;
}

@keyframes bgAnimation {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.card {
    width: 55%;
    margin: auto;
    margin-top: 80px;
    padding: 30px;
    background: rgba(255,255,255,0.25);
    border-radius: 25px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    text-align: center;
    animation: fadeIn 1.5s ease-in-out;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(40px);}
    to {opacity: 1; transform: translateY(0);}
}

.title {
    font-size: 55px;
    font-weight: bold;
    color: #fff;
    text-shadow: 2px 2px 10px #5e5e5e;
}

.name {
    color: #ffeb3b;
    font-size: 58px;
    text-shadow: 2px 2px 15px black;
}

.message {
    font-size: 24px;
    color: white;
    margin-top: 15px;
}

.balloon {
    position: absolute;
    animation: floatUp 8s infinite ease-in;
    opacity: 0.85;
}

@keyframes floatUp {
    0% {transform: translateY(300px);}
    100% {transform: translateY(-600px);}
}

.footer {
    position: fixed;
    bottom: 15px;
    width: 100%;
    text-align: center;
    color: white;
    font-size: 20px;
}

</style>
""", unsafe_allow_html=True)

# --- UI Input ---
st.markdown("## 🎂 Enter Your Name to Generate Birthday Card")
name = st.text_input("Your Name:")
btn = st.button("Create Birthday Card")

if btn and name.strip() != "":
    
    # --- Birthday Card ---
    st.markdown(f"""
    <div class="card">
        <div class="title">🎉 Happy Birthday</div>
        <div class="name">{name}</div>
        <div class="message">Wishing you a year full of joy, success and beautiful memories! 💛</div>
    </div>
    """, unsafe_allow_html=True)

    # --- Balloons Animation ---
    for i in range(20):
        x = random.randint(5, 95)
        size = random.randint(50, 90)
        color = random.choice(["#ff4b5c", "#ffcd3c", "#4cd3c2", "#7efff5", "#ff6ec7"])

        st.markdown(
            f"""
            <div class="balloon" style="
                left:{x}%;
                width:{size}px;
                height:{int(size*1.3)}px;
                background:{color};
                border-radius:50%;
            "></div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(0.15)

# Footer
st.markdown("""
<div class="footer">Made by <b>Pearl</b></div>
""", unsafe_allow_html=True)
