from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "Message"

@app.route('/')
def welcome():
    return redirect(url_for("login"))

@app.route('/login')
def login():
    return '<p>Login Page</p>'

@app.route('/contact')
def contact():
    flash("Support timing are from 9-5.")
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)