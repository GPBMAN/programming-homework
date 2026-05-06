
from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            return render_template("login_answer.html", response=f"{query}")
        else:
            return "No, query :("
    return render_template('login.html')
    

@app.route("/countries")
def countries():
    return render_template('countries.html')


    

app.run(debug=True)