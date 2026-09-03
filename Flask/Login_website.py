from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #! - http://127.0.0.1:5000/
def login():
    return render_template("login.html")


@app.route("/form") #! - http://127.0.0.1:5000/form
def form():
    return render_template("form.html")


@app.route("/thankyou", methods=["GET","POST"]) #! - http://127.0.0.1:5000/thankyou
def thank():
    return render_template("thankyou.html")


@app.route("/resubmit") #! - http://127.0.0.1:5000/resubmit
def resubmit():
    return render_template("resubmit.html")

if __name__ == "__main__":
    app.run(debug=True)



# ! TO run the flask file -  flask --app application run --debug