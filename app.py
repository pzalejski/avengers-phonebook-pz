from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/blackwidow")
def blackwidow():
    return render_template('blackwidow.html')


@app.route("/dr-strange")
def dr_strange():
    return render_template('dr_strange.html')


if __name__ == "__main__":
    app.run(debug=True)
