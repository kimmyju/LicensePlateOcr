from ultralytics import YOLO
import torch
def yolo(data_path, save=True, imgz=640, conf=0.5):
    data_path = './'+data_path
    img_and_coord = []
    # Load a pretrained YOLOv8n model
    model = YOLO('./runs/checkpoints/train/weights/best.pt')
    
    # Run inference on images with arguments
    results = model.predict(data_path, save=save, imgsz=imgz, conf=conf)
    for r in results:
        #names[0]: 'NumberPlate' , orig_img: original image, boxes.xywh: w,y,w,h of the bounding box
        img_and_coord.append([r.names[0], r.orig_img, (r.boxes.xyxy).to('cpu').numpy().flatten()])

    return img_and_coord
    
    # #used to check cropped images
    # for result in results:
    #     result.save_crop('../results/detection_cropped_img')


    

