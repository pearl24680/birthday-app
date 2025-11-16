from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    if request.method == "POST":
        name = request.form.get("username")

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Happy Birthday</title>

<style>
    body {{
        margin: 0;
        padding: 0;
        overflow: hidden;
        background: linear-gradient(135deg,#ff9a9e,#fad0c4,#fbc2eb,#a18cd1);
        background-size: 500% 500%;
        animation: bgAnimation 12s ease infinite;
        font-family: "Poppins", sans-serif;
        text-align: center;
        color: white;
    }}

    @keyframes bgAnimation {{
        0% {{background-position: 0% 50%;}}
        50% {{background-position: 100% 50%;}}
        100% {{background-position: 0% 50%;}}
    }}

    h1 {{
        font-size: 60px;
        margin-top: 100px;
        text-shadow: 3px 3px 20px black;
        animation: fadeIn 2s ease-in-out;
    }}

    @keyframes fadeIn {{
        from {{opacity: 0; transform: scale(0.8);}}
        to {{opacity: 1; transform: scale(1);}}
    }}

    .name {{
        font-size: 50px;
        color: #fff;
        font-weight: bold;
        animation: pop 1s infinite alternate;
    }}

    @keyframes pop {{
        from {{transform: scale(1);}}
        to {{transform: scale(1.15);}}
    }}

    /* Input Card */
    .card {{
        margin-top: 120px;
        background: rgba(255,255,255,0.15);
        padding: 25px;
        width: 50%;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 5px 20px rgba(0,0,0,0.3);
        margin-left: auto;
        margin-right: auto;
    }}

    input {{
        padding: 15px;
        font-size: 20px;
        width: 70%;
        border-radius: 10px;
        border: none;
        outline: none;
    }}

    button {{
        padding: 15px 25px;
        font-size: 20px;
        border: none;
        background: #ff4b5c;
        color: white;
        border-radius: 10px;
        cursor: pointer;
        margin-top: 10px;
        transition: 0.3s;
    }}

    button:hover {{
        background: #ff2e44;
        transform: scale(1.05);
    }}

    /* Balloons */
    .balloon {{
        position: absolute;
        bottom: -150px;
        width: 70px;
        height: 100px;
        border-radius: 50%;
        animation: floatUp 7s infinite ease-in;
        opacity: 0.8;
    }}

    @keyframes floatUp {{
        0% {{transform: translateY(0) rotate(0deg);}}
        100% {{transform: translateY(-900px) rotate(20deg);}}
    }}

    /* Fireworks */
    .firework {{
        position: absolute;
        width: 8px;
        height: 8px;
        background: white;
        border-radius: 50%;
        animation: explode 1s ease-out forwards;
    }}

    @keyframes explode {{
        from {{transform: scale(0); opacity: 1;}}
        to {{transform: scale(6); opacity: 0;}}
    }}

    footer {{
        position: absolute;
        bottom: 15px;
        width: 100%;
        font-size: 20px;
    }}
</style>
</head>
<body>

{"<!-- NAME INPUT FORM -->" if not name else ""}

{f'''
<div class="card">
    <h2>Enter Your Name:</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Your Name" required>
        <br><br>
        <button type="submit">Show Birthday Wish 🎉</button>
    </form>
</div>
''' if not name else ""}

{f'''
<h1>🎉 Happy Birthday <span class="name">{name}</span> 🎂</h1>

<!-- Background Music -->
<audio autoplay loop>
    <source src="https://www.dropbox.com/scl/fi/8s4dq6pr2jke5ihj9tqpt/happy.mp3?rlkey=xyz&raw=1" type="audio/mp3">
</audio>

<script>

// BALLOONS
function createBalloon() {{
    const balloon = document.createElement("div");
    balloon.classList.add("balloon");

    const colors = ["#ff4b5c", "#ffcd3c", "#4cd3c2", "#7efff5", "#ff6ec7"];
    balloon.style.background = colors[Math.floor(Math.random() * colors.length)];

    balloon.style.left = Math.random() * 100 + "vw";
    balloon.style.animationDuration = (5 + Math.random() * 5) + "s";

    document.body.appendChild(balloon);

    setTimeout(() => balloon.remove(), 7000);
}}

setInterval(createBalloon, 400);


// FIREWORKS
function firework() {{
    const fw = document.createElement("div");
    fw.classList.add("firework");

    fw.style.left = Math.random() * 100 + "vw";
    fw.style.top = Math.random() * 80 + "vh";

    document.body.appendChild(fw);

    setTimeout(() => fw.remove(), 1000);
}}

setInterval(firework, 500);

</script>
''' if name else ""}

<footer>Made by <b>Pearl</b></footer>

</body>
</html>
"""
    return html


if __name__ == "__main__":
    app.run(debug=True)
