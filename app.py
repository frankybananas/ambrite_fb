from flask import Flask, request, render_template, url_for
import json
from json import JSONDecodeError
from fun.func import is_json, run_task3, run_task4

app = Flask(__name__) # Define the app using Flask
# app.config["DEBUG"] = True



@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
