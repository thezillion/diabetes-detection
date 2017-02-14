from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("fr2.html")

@app.route('/', methods=['GET','POST'])
def my_form_post():
	name=request.form['name']
	age=request.form['age']

	return render_template("fr.html", name=name, age=age)


if __name__ == '__main__':
    app.run()