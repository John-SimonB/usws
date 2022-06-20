from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "7aw8ezfhdisuzhf"

@app.route("/")
def index():
    flash("whats your nameee?")
    return render_template("index.html")

@app.route("/recipe")
def recipe():
    return "Rezept"

@app.route("/beschreibung")
def beschreibung():
    return "beschreibung"

if __name__ == "__main__":
            app.run()