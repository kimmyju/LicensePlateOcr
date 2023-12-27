from ultralytics import YOLO

model = YOLO('yolov8x.pt')
print(model.info())
model.train(data='ultralytics/datasets/CarPlate/data.yaml',epochs=100,imgsz=640,device=[0,1],project='runs/checkpoints')

