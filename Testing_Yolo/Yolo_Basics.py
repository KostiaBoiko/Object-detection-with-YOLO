from ultralytics import  YOLO
import cv2

model = YOLO('../Yolo_weights/yolov8l.pt')
results = model('Images/Miatas.jpg', show=True)
cv2.waitKey(0)