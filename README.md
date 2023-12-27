# korean LicensePlateRecognition
korean LicensePlateRecognition with YOLOv8 and easyOCR
# 1. demo
## (1) set the project directory as bellow figure
![파일경로fig](https://github.com/kimmyju/LicensePlateRecognition/assets/104639605/dec7435b-b39d-44a7-91d5-e13aa5b9436e)

## (2) detection results
the results of yolov8 trained by the datasets from Roberflow : https://universe.roboflow.com/bright-line-solutions/license-plates-detection-anpr
##
![korean_plate9](https://github.com/kimmyju/LicensePlateRecognition/assets/104639605/4d475504-1dc7-400b-b7a6-a6fdc206e6c6)

## (3) OCR results
## 
![KakaoTalk_20231211_164835912](https://github.com/kimmyju/LicensePlateRecognition/assets/104639605/bfa11d27-cea7-46c2-b6db-1d33a25ccd21)




# 2. train custom data
this repository is implemented from YOLOv8 and easy ocr.
to train your own model with custom data, go to the following repository
<br>(1) license plate detection model: https://github.com/ultralytics/ultralytics
dataset directory figure in this repos are as follows
<br>
![data경로](https://github.com/kimmyju/LicensePlateRecognition/assets/104639605/f73eae36-ff5d-4210-8338-7356879cf3bf)

<br>(2) OCR model: https://github.com/ultralytics/ultralytics
<br>in this repos, OCR model was not trained(only detection model was trained). provided pretrained weights of easyOCR is used. 
