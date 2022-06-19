import os
from time import time
from flask import Flask, jsonify, request
from flask_cors import CORS

import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2 as cv

class_names_41classes = ['1WayConnectorforFoley', '2WayConnectorforFoley', '2WayFoleyCatheter', '3WayConnectorforFoley', '3Waystopcock', 'AlcoholBottle', 'AlcoholPad', 'BootCover', 'CottonBall', 'CottonSwap', 'Dilator', 'DisposableInfusionSet', 'ExtensionTube', 'FaceShield', 'FrontLoadSyringe', 'GauzePad', 'Glove', 'GuideWire', 'LiquidBottle', 'Mask', 'NGTube', 'NasalCannula', 'Needle', 'OxygenMask', 'PPESuit', 'PharmaceuticalProduct', 'Pill', 'PillBottle', 'PrefilledHumidifier', 'PressureConnectingTube', 'ReusableHumidifier', 'SodiumChlorideBag', 'SterileHumidifierAdapter', 'SurgicalBlade', 'SurgicalCap', 'SurgicalSuit', 'Syringe', 'TrachealTube', 'UrineBag', 'Vaccinebottle', 'WingedInfusionSet']
class_names_4group = ['1-InfectionWaste', '2-BloodSecretionWaste', '3-LabWardWaste', '4-VaccineOtherWaste']

# -------------- Tensor-flow load model ------------

# 41 Classes Classification Model
model_41classes_path = './model/41CLASSES-EfficientNetB5-epoch2000.pb'
model_41classes = tf.keras.models.load_model(model_41classes_path)

# 4 Main Groups Classification Model
model_4group_path = './model/4G-EfficientNetB5-epoch2000.pb'
model_4group = tf.keras.models.load_model(model_4group_path)

# model_41classes YoloV4 Object Detection Model
net_yolov4 = cv.dnn.readNet("./yolo-obj_50000.weights", "./yolo-obj.cfg")
net_yolov4.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
net_yolov4.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)
model_yolov4 = cv.dnn_DetectionModel(net_yolov4)
model_yolov4.setInputParams(size=(416, 416), scale=1/255, swapRB=True, crop=False)
CONFIDENCE_THRESHOLD = 0.1
NMS_THRESHOLD = 0.4



# generate different colors for different classes 
COLORS = np.random.uniform(0, 255, size=(len(class_names_41classes), 3))

app = Flask(__name__)
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