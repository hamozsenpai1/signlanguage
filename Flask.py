from flask import Flask , render_template ,request, jsonify ,make_response, send_from_directory

import tensorflow as tf
from tensorflow import keras
import cv2
import numpy as np
from flask_ngrok import run_with_ngrok


app=Flask(__name__)
# run_with_ngrok(app)
model=tf.keras.models.load_model('model.hdf5')

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/pred', methods=["POST"])
def pred():

    img=request.files['img']

    img.save("img.jpg")
    image=cv2.imread("img.jpg")
    image=cv2.resize(image,(64,64))
    image=np.reshape(image,(1,64,64,3))
    
 #   image=str(image)
    
    pred=model.predict(image)
    pred=np.argmax(pred)

    return render_template("pred.html",data=pred)

# @app.route('/pred', methods=["POST"])
# def pred():

#     img=request.files['img']

#     img.save("img.jpg")
#     image=cv2.imread("img.jpg")
#     image=cv2.resize(image,(64,64))
#     image=np.reshape(image,(1,64,64,3))
    
#  #   image=str(image)
    
#     pred=model.predict(image)
#     pred=np.argmax(pred)

#     return render_template("pred.html",data=pred)


@app.route('/sw.js')
def sw():
   return app.send_static_file('sw.js')
# @app.route('/sw.js')
# def service_worker():
#     response = make_response(send_from_directory('static', 'sw.js'))
#     response.headers['Cache-Control'] = 'no-cache'
#     return response

if __name__ == '__main__':
    app.run()