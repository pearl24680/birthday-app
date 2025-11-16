import streamlit as st
import base64

# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(
    page_title="Cute Birthday Wish",
    layout="centered"
)

# --------------------------
# GLOBAL PINK BACKGROUND
# --------------------------
page_bg = """
<style>
body {
    background-color: #ffdef2 !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --------------------------
# NAVBAR
# --------------------------
navbar = """
<style>
.navbar {
    background: white;
    padding: 12px;
    border-radius: 20px;
    display: flex;
    justify-content: center;
    gap: 40px;
    font-size: 20px;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    margin-bottom: 25px;
}
.navbar a {
    text-decoration: none;
    color: #ff4fa2;
}
.navbar a:hover {
    color: #d60073;
}
</style>

<div class="navbar">
    <a href="?page=home">Home</a>
    <a href="?page=wish">Make a Wish</a>
    <a href="?page=upload">Upload Photo</a>
</div>
"""
st.markdown(navbar, unsafe_allow_html=True)

# READ PAGE PARAM
page = st.query_params.get("page", "home")

# --------------------------
# BALLOON ANIMATION BUTTON
# --------------------------
def balloon_button():
    if st.button("🎈 Release Balloons! 🎈"):
        st.balloons()

# --------------------------
# HOME PAGE
# --------------------------
if page == "home":
    st.markdown(
        """
        <div style="
            background:white;
            padding:30px;
            border-radius:25px;
            text-align:center;
            box-shadow:0 5px 20px rgba(0,0,0,0.2);
        ">
            <h1 style="color:#ff2e93;">🎀 Welcome to the Birthday Wishes 🎀</h1>
            <p style="font-size:20px;color:#444;">
                Create cute animated birthday wishes for your friends!
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    balloon_button()

# --------------------------
# WISH PAGE
# --------------------------
elif page == "wish":

    st.markdown(
        """
        <h2 style="text-align:center;color:#ff2e93;">💗 Create Cute Birthday Wish 💗</h2>
        """,
        unsafe_allow_html=True
    )

    name = st.text_input("Enter Name:")

    if name:
        st.markdown(
            f"""
            <div style="
                background:white;
                padding:30px;
                border-radius:25px;
                text-align:center;
                margin-top:20px;
                box-shadow:0 4px 15px rgba(0,0,0,0.2);
                ">
                
                <h1 style="color:#ff2e93; font-size:40px;">🎉 Happy Birthday {name}! 🎉</h1>
                
                <p style="font-size:22px; color:#444;">
                    Wishing you lots of joy, smiles, surprises & love 💕<br>
                    Have a magical and unforgettable day!
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        balloon_button()

# --------------------------
# UPLOAD PHOTO PAGE
# --------------------------
elif page == "upload":

    st.markdown(
        """
        <h2 style="text-align:center;color:#ff2e93;">📸 Upload a Cute Photo</h2>
        """,
        unsafe_allow_html=True
    )

    img = st.file_uploader("Upload Photo", type=["png", "jpg", "jpeg"])

    if img:
        st.image(img, caption="Your Uploaded Photo", use_container_width=True)

# --------------------------
# FOOTER
# --------------------------
st.markdown(
    """
    <br><br>
    <p style="text-align:center; color:#ff0d6a; font-weight:600;">
        🌸 Made with love by Pearl 🌸
    </p>
    """,
    unsafe_allow_html=True
)
