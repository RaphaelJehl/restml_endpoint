import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from classes import class_label

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


# home and input page
@app.route('/')
def home():
    return render_template('index.html')


# predict route
@app.route('/classify',methods=['POST'])
def predict():
    # retrieve 784 pixels from input form
    int_features = [eval(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    # get highest probability
    probability = np.max(prediction)
    # get class that has the highest probability
    id_class_pred = np.argmax(prediction)
    id_class_pred = int(id_class_pred)
    label_class_pred = class_label[id_class_pred]

    return render_template('results.html', prediction=label_class_pred, proba=probability)


if __name__ == "__main__":
    app.run(debug=True)