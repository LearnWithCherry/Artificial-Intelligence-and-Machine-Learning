from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def Hello_world():
    data = {
        "Message" : "Welcome to the platform!!"
    }
    return jsonify(data), 200



if __name__ == "__main__":
    app.run(debug=True)