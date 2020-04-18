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
    if request.method == "POST":
        string1 = None
        string2 = None
        string1 = str(request.form['string1'])
        string2 = str(request.form['string2'])
        if string1 is not None and string2 is not None:
            result = run_task3(string1, string2)
            html_item = json.dumps(result, indent=4, seperators(', ', ': '))
            return render_template("task3_out.html", result=result)
    return render_template("task3_in.html")      

if __name__ == '__main__':
    app.run(debug=True, port=8080)
