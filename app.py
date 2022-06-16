from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "7aw8ezfhdisuzhf"

@app.route("/")
def index():
    flash("whats your nameee?")
    return render_template("index.html")

if __name__ == "__main__":
            app.run()