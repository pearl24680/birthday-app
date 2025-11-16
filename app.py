from flask import Flask, render_template_string

app = Flask(__name__)

html_card = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Birthday Card</title>
<style>
    body {
        width: 210mm;
        height: 297mm;
        margin: 0;
        padding: 40px;
        font-family: "Arial", sans-serif;
        text-align: center;
        border: 3px solid #008cff;
        box-sizing: border-box;
    }
    h1 {
        color: #008cff;
        font-size: 40px;
        margin-top: 40px;
    }
    p {
        font-size: 22px;
        color: #333;
        margin: 25px 0;
        line-height: 1.5;
    }
    .footer {
        margin-top: 120px;
        font-size: 18px;
        color: #555;
    }
</style>
</head>

<body>
    <h1>🎉 Happy Birthday! 🎉</h1>

    <p>
        Wishing you a beautiful day filled with joy and smiles.<br>
        May God bless you always and bring happiness into your life. 💙✨
    </p>

    <div class="footer">
        — Made by Pearl —
    </div>
</body>
</html>
"""

@app.route("/")
def card():
    return render_template_string(html_card)

if __name__ == "__main__":
    app.run(debug=True)
