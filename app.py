from flask import Flask, render_template, request, redirect, url_for
from habit import Habit

app = Flask(__name__)

habits = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    goal = int(request.form['goal'])
    habits.append(Habit(name, goal))
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', habits=habits)

@app.route('/update/<int:index>')
def update(index):
    habits[index].complete()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
