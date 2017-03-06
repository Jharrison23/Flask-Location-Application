# import the class and function render template
from flask import Flask, render_template

# Create and store a useable instance of the flask class
app = Flask(__name__)

# Map the URL "/" to the python function index
@app.route("/")

# The python function index uses the flask function render template to render index.html
# So when a user types in the url / the function index() will run and return the page index.html
def index():
    return render_template("index.html")

# app.run, runs the app on a local server
# debug true flag allows us to see any error messages
if __name__ == "__main__":
    app.run(debug=True)
