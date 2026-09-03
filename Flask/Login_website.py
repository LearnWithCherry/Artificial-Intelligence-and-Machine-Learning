from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder="static")


@app.route("/") #? Running on http://127.0.0.1:5000/
def login():
    return render_template("login.html")


@app.route("/form") #? Running on http://127.0.0.1:5000/form
def form():
    return render_template("form.html")


@app.route("/thankyou", methods=["GET", "POST"]) #? Running on http://127.0.0.1:5000/form
def thank():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]
        city = request.form["city"]

        return render_template("thankyou.html", name=name)

    return render_template("thankyou.html", name="<3")


@app.route("/resubmit")  #? Running on http://127.0.0.1:5000/resubmit
def resubmit():
    return render_template("resubmit.html")


if __name__ == "__main__":
    app.run(debug=True)


# ! To run:  flask --app Login_website run --debug