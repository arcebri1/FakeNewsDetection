from flask import Flask, render_template, jsonify
import pandas as pd
import csv
import psycopg2 as psycopg2

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/")
# def scatter():
#     return render_template("")

# @app.route("/")
# def scatter():
#     return render_template("")



if __name__ == '__main__':
    app.run(debug=True)