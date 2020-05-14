from flask import Flask, request, jsonify, render_template
import numpy as np
import keras as k
from keras.models import load_model
import tensorflow as tf
from PIL import Image
import cv2
import base64

from werkzeug.utils import secure_filename

app = Flask(__name__)

def init():
   global model,graph, session
   session = k.backend.get_session()
   init = tf.global_variables_initializer()
   session.run(init)
   model = load_model('model.h5')
   graph = tf.get_default_graph()

@app.route('/', methods=['POST'])

def predict():
   file = request.files['file']
   file.save(secure_filename('templates/image.jpeg'))

   img = cv2.imread("templates_image.jpeg")
   img = cv2.resize(img, (70, 70))
   im2arr = np.array(img).reshape(-1,70,70,3)
   with session.as_default():
      with graph.as_default():
         y_pred = model.predict_classes(im2arr[[0], :])
   print(y_pred[0])
   return render_template('result.html', result= get_plant_name(y_pred[0]))

def get_plant_name(number):
   if number == 0:
      return "Black Grass"
   if number == 1:
      return "Charlock"
   if number == 2:
      return "Cleavers"
   if number == 3:
      return "Common Chickweed"
   if number == 4:
      return "Common Wheat"
   if number == 5:
      return "Fat Hen"
   if number == 6:
      return "Loose silky bent"
   if number == 7:
      return "Maize"
   if number == 8:
      return "Scentless Mayweed"
   if number == 9:
      return "Shepherds Purse"
   if number == 10:
      return "Small-flowered Cranesbill"
   if number == 11:
      return "Sugar Beet"

@app.route('/')
def upload_file():
   return render_template('index.html')

if __name__ == '__main__':
   print(("* Loading Keras model and Flask starting server..."
      "please wait until server has fully started"))
   init()
   app.run(port = 5000, debug=True, threaded=False)