import os
from time import time
from flask import Flask, flash, redirect, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2 as cv


directory = os.getcwd()
print(f'Run code at {directory}.\n\n')

class_names_41classes = ['1WayConnectorforFoley', '2WayConnectorforFoley', '2WayFoleyCatheter', '3WayConnectorforFoley', '3Waystopcock', 'AlcoholBottle', 'AlcoholPad', 'BootCover', 'CottonBall', 'CottonSwap', 'Dilator', 'DisposableInfusionSet', 'ExtensionTube', 'FaceShield', 'FrontLoadSyringe', 'GauzePad', 'Glove', 'GuideWire', 'LiquidBottle', 'Mask', 'NGTube', 'NasalCannula', 'Needle', 'OxygenMask', 'PPESuit', 'PharmaceuticalProduct', 'Pill', 'PillBottle', 'PrefilledHumidifier', 'PressureConnectingTube', 'ReusableHumidifier', 'SodiumChlorideBag', 'SterileHumidifierAdapter', 'SurgicalBlade', 'SurgicalCap', 'SurgicalSuit', 'Syringe', 'TrachealTube', 'UrineBag', 'Vaccinebottle', 'WingedInfusionSet']
class_names_4group = ['1-InfectionWaste', '2-BloodSecretionWaste', '3-LabWardWaste', '4-VaccineOtherWaste']

# -------------- Tensor-flow load model ------------

# 41 Classes Classification Model
model_41classes_path = './model/41CLASSES-EfficientNetB5-epoch2000.pb'
model_41classes = tf.keras.models.load_model(model_41classes_path)

# 4 Main Groups Classification Model
model_4group_path = './model/4G-EfficientNetB5-epoch2000.pb'
model_4group = tf.keras.models.load_model(model_4group_path)
'''
# model_41classes YoloV4 Object Detection Model
net_yolov4 = cv.dnn.readNet('./model/yolo_v4_41CLASSES/yolov4-obj_best.weights','./model/yolo_v4_41CLASSES/yolov4-obj.cfg') #, "./model/yolo_v4_41CLASSES/yolov4-obj.cfg"
net_yolov4.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
net_yolov4.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)
model_yolov4 = cv.dnn_DetectionModel(net_yolov4)
model_yolov4.setInputParams(size=(416, 416), scale=1/255, swapRB=True, crop=False)
CONFIDENCE_THRESHOLD = 0.1
NMS_THRESHOLD = 0.4
# generate different colors for different classes 
COLORS = np.random.uniform(0, 255, size=(len(class_names_41classes), 3))
'''
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

@app.route('/')
def show_index():
    str =  """<!DOCTYPE html>
<html>
<head>
<title>MedWaste-Prediction-BACKEND-API</title>
</head>
<body>

<h1>Welcome to MedWaste-Prediction-BACKEND-API</h1>
<p>This is MedWaste-Prediction-BACKEND-API</p>

</body>
</html>"""
    return str

ALLOWED_EXTENSIONS = set(['bmp', 'png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app.config['im_cache_path'] = './im_cache/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def predictClassify_41classes(im_path):
    img = image.load_img(im_path, target_size=(456, 456)) # B5 -> img_height_width=456
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_batch)
    prediction = model_41classes.predict(img_preprocessed)
    predict_probs = {class_names_41classes[i]: prediction[0][i]*100.0 for i in range(len(class_names_41classes))}
    sorted_predict_probs = dict(sorted(predict_probs.items(), key=lambda item: item[1], reverse=True))
    #print(sorted_predict_probs)
    return sorted_predict_probs


@app.route('/class41', methods=['POST'])
def classify41():
    im_path = ''
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    #str_date = request.form['date']
    success = False
    predict_message = ""
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No selected file'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        im_path = os.path.join(app.config['im_cache_path'], filename)
        file.save(im_path)
        #predict_message = predictClassify_41classes(im_path) # for debug
        try:
            predict_message = predictClassify_41classes(im_path)
            success = True
        except:
            success = False
    else:
        resp = jsonify({'message': im_path + ' -> File type is not allowed'})
        resp.status_code = 400
        return resp
    if success:
        resp = jsonify(predict_message)
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message': "Internal AI ERROR"})
        resp.status_code = 500
        return resp

def predictClassify_4G(im_path):
    img = image.load_img(im_path, target_size=(456, 456)) # B5 -> img_height_width=456
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_batch)
    prediction = model_4group.predict(img_preprocessed)
    predict_probs = {class_names_4group[i]: prediction[0][i]*100.0 for i in range(len(class_names_4group))}
    sorted_predict_probs = dict(sorted(predict_probs.items(), key=lambda item: item[1], reverse=True))
    #print(sorted_predict_probs)
    return sorted_predict_probs


@app.route('/class4G', methods=['POST'])
def classify4G():
    im_path = ''
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    #str_date = request.form['date']
    success = False
    predict_message = ""
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No selected file'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        im_path = os.path.join(app.config['im_cache_path'], filename)
        file.save(im_path)
        #predict_message = predictClassify_41classes(im_path) # for debug
        try:
            predict_message = predictClassify_4G(im_path)
            success = True
        except:
            success = False
    else:
        resp = jsonify({'message': im_path + ' -> File type is not allowed'})
        resp.status_code = 400
        return resp
    if success:
        resp = jsonify(predict_message)
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message': "Internal AI ERROR"})
        resp.status_code = 500
        return resp


if __name__ == "__main__":
    app.run(port=80,debug=False)