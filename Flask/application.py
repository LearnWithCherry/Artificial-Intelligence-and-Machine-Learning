from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #! - http://127.0.0.1:5000/
def hello_world():
    return "<h1>Hello Engineer</h1>"

@app.route("/") #! - http://127.0.0.1:5000/login 
def file():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)



# ! TO run the flask file -  flask --app application run --debug