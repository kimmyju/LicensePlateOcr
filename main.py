import cv2
import easyocr
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from LicensePlateDetection_YOLOv8.YOLOv8_predict import yolo

reader = easyocr.Reader(['ko'], gpu=True,model_storage_directory='../korean_g2.pth')
def easy_ocr(img, coordinates):
    x1, y1, x2, y2 = int(coordinates[0]),int(coordinates[1]),int(coordinates[2]),int(coordinates[3])
    img = img[y1:y2, x1:x2]
    #convert to BGR
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    # resize image
    (h, w) = gray.shape[:2]
    new_width = 400 
    new_height = int(h * (new_width / w))
    resized_image = cv2.resize(gray, (new_width, new_height))
   
    result = reader.readtext(resized_image)
    text = []
    for res in result:
        if len(result) == 1:
            text.append(res[1])
        elif len(result) > 1 and len(res[1]) > 3 and res[2] > 0.2:
            text.append(res[1])
       
    return text

if __name__ == '__main__':
    # license detection with yolov8 & returns id, image, bbox coord(x,y,w,h)
    img_and_coord = yolo('your/test/image/directory')
    
    text_ocr = []
    # ocr
    for instance in img_and_coord:
        if instance[0] == 'NumberPlate':
            text_ocr.append(easy_ocr(instance[1], instance[2])) #image, coord
    # print ocr results
    print('#INFO [차량 번호]: ')
    for txt in text_ocr:
        if len(txt) == 1:
            print(txt[0])
        else:
            text=''
            for i in range(len(txt)):
                text +=txt[i]
            print(text)
            
    

