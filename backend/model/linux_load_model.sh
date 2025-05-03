#!/bin/bash
sudo apt-get install zip unzip  -y
sudo apt-get install ffmpeg libsm6 libxext6  -y
echo 'Loading Model from https://asset.coecore.com/model-ai/medical-waste/4G-EfficientNetB5-epoch2000.pb.zip'
wget https://asset.coecore.com/model-ai/medical-waste/4G-EfficientNetB5-epoch2000.pb.zip
echo 'Loading Model from https://asset.coecore.com/model-ai/medical-waste/41CLASSES-EfficientNetB5-epoch2000.pb.zip'
wget https://asset.coecore.com/model-ai/medical-waste/41CLASSES-EfficientNetB5-epoch2000.pb.zip
echo 'Loading Model from https://asset.coecore.com/model-ai/medical-waste/10FreqCLASSES-EfficientNetB5-epoch1000.pb.zip'
wget https://asset.coecore.com/model-ai/medical-waste/10FreqCLASSES-EfficientNetB5-epoch1000.pb.zip
echo 'Loading Model from https://asset.coecore.com/model-ai/medical-waste/yolo_v4_41CLASSES.zip'
wget https://asset.coecore.com/model-ai/medical-waste/yolo_v4_41CLASSES.zip
echo 'Loading Model from https://asset.coecore.com/model-ai/medical-waste/yolo_v5_41CLASSES.zip'
wget https://asset.coecore.com/model-ai/medical-waste/yolo_v5_41CLASSES.zip
echo 'Model Unzipping..................'
unzip '4G-EfficientNetB5-epoch2000.pb.zip'
unzip '41CLASSES-EfficientNetB5-epoch2000.pb.zip'
unzip '10FreqCLASSES-EfficientNetB5-epoch1000.pb.zip'
unzip 'yolo_v4_41CLASSES.zip'
ls -a
Model_MedWaste_Path = $(pwd)
echo 'Model Saved at ...' + $Model_MedWaste_Path
echo '++++++++++ [Load/Extract Model] Completed ++++++++++'
