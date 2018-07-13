from flask import Flask, jsonify, render_template, request
import requests
app=Flask(__name__)

##microsoft subscription key for sentiment
subscription_key =  'adb0a29a82be49908776b915bc6a5d86'
assert subscription_key

##region sepecified
##this one is for free usage
text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"


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
            result = predict_the_text(data['value'])
            return jsonify({'name':result})
    return jsonify({'error','error occured'})

def predict_the_text(text):
    sentiment_api_url = text_analytics_base_url + "sentiment"
    print(sentiment_api_url)
    ##lets define the document to detect the sentiment
    
    documents = {'documents' : [
        {'id': '1', 'language': 'en', 'text': text},
        ]}

    ##lets do the sentiment detection
    headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
    response  = requests.post(sentiment_api_url, headers=headers, json=documents)
    sentiments = response.json()
    doc = sentiments['documents']
    sen=doc[0]
    ##this is the actual score
    score = sen['score']
    if score >0.5:
        return 'positive'
    else:
        return 'negative'



if __name__ == "__main__":
    app.run(debug=True)
    