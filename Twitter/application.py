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
        data = request.get_json()
        if(data !=None):
            ##here we have to make a call to cognitive api for the sentiment analysis
            ##thankgod it finally worked
            return jsonify({'name':"Positive"})
    return jsonify({'error','error occured'})


if __name__ == "__main__":
    app.run(debug=True)