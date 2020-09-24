from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

# creates a Flask application, named app
app = Flask(__name__)
Bootstrap(app)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def color_balance():
    message = "Color Balance"
    value = 50
    return render_template('index.html', message=message, value=value)

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)