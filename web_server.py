from flask import Flask, request, jsonify, render_template

from router import process_request


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    message = data.get("message", "")

    answer = process_request(message)

    return jsonify(
        {
            "response": answer
        }
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=10000
    )
