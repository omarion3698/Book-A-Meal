from flask import Flask, render_template, url_for

app = Flask(__name__)



@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/menue")
def menue():
    return render_template("menue.html")


@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

if __name__ =='__main__':
    app.run(debug=True)