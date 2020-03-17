from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():  # fucntions that are called in the url_for('')
    return render_template("home.html")


@app.route("/blackwidow")
def blackwidow():
    return render_template('blackwidow.html')


@app.route("/dr-strange")
def dr_strange():
    return render_template('dr_strange.html')


@app.route("/ironman")
def ironman():
    return render_template('ironman.html')


@app.route("/thor")
def thor():
    return render_template('thor.html')


@app.route("/hawkeye")
def hawkeye():
    return render_template('hawkeye.html')


@app.route('/captain-america')
def captain_america():
    return render_template('captain_america.html')


@app.route('/hulk')
def hulk():
    return render_template('hulk.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
