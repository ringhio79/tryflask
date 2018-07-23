from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

todolist1 = []

@app.route("/")
def show_hi():
    return render_template("contacts.html", todolist=todolist1)

@app.route("/add", methods=['POST'])
def add_item():
    item = request.form['item']
    todolist1.append(item)
    return redirect("/")

@app.route("/edit", methods=['POST', 'GET'])
def edit_item():
    if request.method=="POST":
        newitem = request.form['item']
        olditem = request.form['olditem']
        
        todolist1.remove(olditem)
        todolist1.append(newitem)
        
        return redirect("/")
    else:
        item = request.args['item']
    return render_template("edititem.html", item=item)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)