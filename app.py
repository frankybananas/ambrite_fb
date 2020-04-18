from flask import Flask, request, render_template, url_for
import json
from json import JSONDecodeError
from fun.func import is_json, run_task3, run_task4

app = Flask(__name__) # Define the app using Flask
# app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/task2', methods=['GET', 'POST'])
def task2():
    result = ""
    if request.method == "POST":
        string1 = None
        string1 = str(request.form['string1'])
        if string1 is not None:
            result = is_json(string1)
            return render_template("task2_out.html", result=result)
    return render_template("task2_in.html")

@app.route('/task3', methods=["GET", "POST"])
def task3():
    result = ""
    

if __name__ == '__main__':
    app.run(debug=True, port=8080)
