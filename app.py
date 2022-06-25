from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "7aw8ezfhdisuzhf"



# auf dieser seite bitte den abgleich der rezepte mit flink daten einbinden 
# wenn möglich ausgabe auf internetseite bitte so:

#rezeptname1:
# zutat1
# zutat2
# zutat3
# ....
# preis

#rezeptname2:
# zutat1
# zutat2
# zutat3
# ....
# preis

@app.route("/recipe")
def recipe():
    return "Rezept"

@app.route("/")
def index():
    flash("whats your nameee?")
    return render_template("index.html")

@app.route("/beschreibung")
def beschreibung():
    return "beschreibung"

if __name__ == "__main__":
            app.run()