from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

@app.route("/")
def show_hi():
    return render_template("index.html")
    
@app.route("/searchpost", methods=['POST'])
def do_search():
    make = request.form['make']
    model = request.form['model']
    year = request.form['year']
    return "Hey you searched for {0} {1} {2}".format(year, make, model)

@app.route("/searchget")
def do_search_get():
    make = request.args['make']
    model = request.args['model']
    year = request.args['year']
    return "Hey you searched for {0} {1} {2}".format(year, make, model)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)