import requests
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80),unique=True, nullable=False)
    content =db.Column(db.Text, nullable=False)
    complete = db.Column(db.Boolean, nullable=False)

@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def addtodo():
    title = request.form.get("title")
    if not title:
        return redirect(url_for("index"))
    content = request.form.get("content")
    
    newtodo = Todo(title = title, content = content, complete=False)

    db.session.add(newtodo)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def completetodo(id):
    todo = Todo.query.filter_by(id=id).first()
    if (todo.complete == False):
        todo.complete = True
    else:
        todo.complete = False

    db.session.commit()

    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deletetodo(id):
    todo = Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("index"))










if __name__ == "__main__":
    app.run(debug=True)