from flask import Flask, render_template, request, flash
import os
import chatbot

app = Flask(__name__)
app.secret_key = "manPigHAHAblalabla"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chatbot", methods=["POST", "GET"])
def process_chat_messsage():
    question = request.form["question"]
    response = chatbot.reply_user(question)
    flash(response) 
    return render_template("index.html")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

