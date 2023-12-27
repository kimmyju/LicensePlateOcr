# korean LicensePlateRecognition
korean LicensePlateRecognition with YOLOv8 and easyOCR
<br> If you found this repository useful, please let us know by staring this repo ★
# 1. demo
## (1) set the project directory as bellow figure
![파일경로fig](https://github.com/kimmyju/LicensePlateOcr/assets/104639605/2f242188-302a-43b2-a65e-b94d75847dc2)


## (2) detection results
the results of yolov8 trained by the datasets from Roberflow : https://universe.roboflow.com/bright-line-solutions/license-plates-detection-anpr
##
![korean_plate9](https://github.com/kimmyju/LicensePlateOcr/assets/104639605/02b6fb87-7826-4aee-97b2-b6ed7cfb0cc9)

## (3) OCR results
## 
![KakaoTalk_20231211_164835912](https://github.com/kimmyju/LicensePlateOcr/assets/104639605/3c2809dd-f646-491d-a34e-fb3383195a23)




# 2. train custom data
this repository is implemented from YOLOv8 and easy ocr.
to train your own model with custom data, go to the following repository
<br>(1) license plate detection model: https://github.com/ultralytics/ultralytics
dataset directory figure in this repos are as follows
<br>
![data경로](https://github.com/kimmyju/LicensePlateOcr/assets/104639605/a1d1b0c1-74cd-4194-859c-410fc0d12c18)


<br>(2) OCR model: https://github.com/ultralytics/ultralytics
<br>in this repos, OCR model was not trained(only detection model was trained). provided pretrained weights of easyOCR is used. 
