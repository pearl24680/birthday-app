import streamlit as st

# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(
    page_title="Birthday Wish",
    layout="centered"
)

# --------------------------
# LIGHT BLUE BACKGROUND
# --------------------------
page_bg = """
<style>
body {
    background-color: #dff3ff !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --------------------------
# HEADING
# --------------------------
st.markdown(
    """
    <h1 style="text-align:center; color:#0077cc;">
        🎉 Cute Birthday Wish Generator 🎉
    </h1>
    """,
    unsafe_allow_html=True
)

# --------------------------
# ASK NAME
# --------------------------
name = st.text_input("Enter the name for birthday wish:")

# --------------------------
# SHOW CARD
# --------------------------
if name:
    st.markdown(
        f"""
        <div style="
            background:white;
            padding:25px;
            border-radius:20px;
            text-align:center;
            margin-top:25px;
            box-shadow:0 6px 20px rgba(0,0,0,0.25);
            border:3px solid #5ab4ff;
        ">

            <h1 style="color:#008cff; font-size:40px;">
                🎈 Happy Birthday {name}! 🎈
            </h1>

            <img src="https://i.pinimg.com/originals/48/ef/05/48ef05e8f302ff628f6ba674fbec6ff3.png"
                width="220" alt="Doraemon">

            <p style="font-size:22px; color:#333; margin-top:15px;">
                May your special day be filled with<br>
                fun, excitement and smiles just like<br>
                <b>Doraemon, Cars & Hot Wheels adventures!</b> 🚗💨💙
            </p>

            <img src="https://i.pinimg.com/originals/36/e0/f1/36e0f117d1691e6c59e43db3cdbe13b1.png"
                width="250" alt="Hotwheels">

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("🎈 Release Balloons!"):
        st.balloons()

# --------------------------
# FOOTER
# --------------------------
st.markdown(
    """
    <br><br>
    <p style="text-align:center; color:#005fa3; font-weight:600;">
        💙 Made by Pearl 💙
    </p>
    """,
    unsafe_allow_html=True
)
