import random

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Show index page."""
    return render_template("index.html")



@app.route('/profile', methods=['POST'])
def profile():
    """Return results from profile form."""

    fullname = request.form['name']
    age = request.form['age'] #added
    occupation = request.form['occupation'] #added
    
    return jsonify({'fullname': fullname,
                    'age': age, #added
                    'occupation': occupation}) #added





if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")