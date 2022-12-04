import pickle
from flask import Flask,request,render_template,app,jsonify,url_for
import numpy as np
import pandas as pd

app = Flask(__name__)
regmodel  = pickle.load(open("regmodel.pkl","rb"))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)



