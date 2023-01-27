""""
ML model to predict fashion mnist classes using a simple keras NN
"""

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import pickle


# import, prepare train/test, scale

mnist_train = pd.read_csv(r"C:\Users\raphj\OneDrive\Documents\datasets\mlops\mnist\fashion-mnist-train-1.csv")
mnist_test = pd.read_csv(r"C:\Users\raphj\OneDrive\Documents\datasets\mlops\mnist\fashion-mnist_test.csv")

y_train = mnist_train['label']
X_train = mnist_train.drop(columns=['label'])

y_test = mnist_test['label']
X_test = mnist_test.drop(columns=['label'])

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

X_train = X_train / 255.0
X_test = X_test / 255.0


# create and train simple keras NN
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(X_train, y_train, batch_size = 8, epochs=10)

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(X_test)


# save model with pickle
pickle.dump(model, open('model.pkl','wb'))
model = pickle.load(open('model.pkl', 'rb'))