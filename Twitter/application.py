from flask import Flask, jsonify, render_template, request

app=Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
    print('rendering......')
    return render_template('layout.html')


@app.route('/predict',methods=['POST', 'GET'])
def predict():
    if request.method=='POST':
        print('inside the post method')
        a = request.request.args.get('x')
        print('got the data')
    else:
        print('the method was not called with pos')
    return jsonify(result="positive")
