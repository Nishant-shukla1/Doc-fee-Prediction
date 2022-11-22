from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("doc_fee.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    features=[x for x in request.form.values()]
    final=[np.array(features)]
    print(features)
    print(final)
    prediction=model.predict(final)
    p=int(prediction)
    output='{}'.format(p)

   
    return render_template('doc_fee.html',pred='The approximate fee of doctor is Rs.{}'.format(output))
    

if __name__ == '__main__':
    app.run(debug=True)
