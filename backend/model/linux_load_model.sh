#!/bin/bash

echo 'Loading Model from https://assets.gezdev.com/model-ai/medical-waste/4G-EfficientNetB5-epoch2000.pb.zip'
wget https://assets.gezdev.com/model-ai/medical-waste/4G-EfficientNetB5-epoch2000.pb.zip
echo 'Loading Model from https://assets.gezdev.com/model-ai/medical-waste/41CLASSES-EfficientNetB5-epoch2000.pb.zip'
wget https://assets.gezdev.com/model-ai/medical-waste/41CLASSES-EfficientNetB5-epoch2000.pb.zip
echo 'Loading Model from https://assets.gezdev.com/model-ai/medical-waste/10FreqCLASSES-EfficientNetB5-epoch1000.pb.zip'
wget https://assets.gezdev.com/model-ai/medical-waste/10FreqCLASSES-EfficientNetB5-epoch1000.pb.zip
echo 'Loading Model from https://assets.gezdev.com/model-ai/medical-waste/yolo_v4_41CLASSES.zip'
wget https://assets.gezdev.com/model-ai/medical-waste/yolo_v4_41CLASSES.zip
echo 'Loading Model from https://assets.gezdev.com/model-ai/medical-waste/yolo_v5_41CLASSES.zip'
wget https://assets.gezdev.com/model-ai/medical-waste/yolo_v5_41CLASSES.zip
echo 'Model Unzipping..................'
tar -xzvf '4G-EfficientNetB5-epoch2000.pb.zip'
tar -xzvf '41CLASSES-EfficientNetB5-epoch2000.pb.zip'
tar -xzvf '10FreqCLASSES-EfficientNetB5-epoch1000.pb.zip'
tar -xzvf 'yolo_v4_41CLASSES.zip'
ls -a
Model_MedWaste_Path = $(pwd)
echo 'Model Saved at ...' + $Model_MedWaste_Path
echo '++++++++++ [Load/Extract Model] Completed ++++++++++'