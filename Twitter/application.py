from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
    return render_template('layout.html')


def predict(sentence):
    return "positive"