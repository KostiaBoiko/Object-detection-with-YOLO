from ultralytics import YOLO
import cv2
import cvzone
import math
import torch
print(torch.backends.mps.is_available())

# cap = cv2.VideoCapture(0) # for webcam
# cap.set(4, 720)
# cap.set(3, 1280)
cap = cv2.VideoCapture("../Videos/cars.mp4") # for video


model = YOLO("../Yolo_weights/yolov8l.pt")

classNames = ["person", "bird", "wolf", "cat", "parrot", "crow", "eagle", "truck", "car", "motorcycle", "bus", "cell phone", "pen", "box", "paper", "towel", "napkin",
              "hand watch", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign",
              "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra",
              "giraffe", "backpack", "umbrella", "handbag" "tie", "suitcase", "frisbee", "skis", "snowboard",
              "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
              "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich",
              "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa",
              "bed", "dining table", "toilet", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"]

while True:
    success, img= cap.read()
    results = model(img, stream=True, device="mps")
    for r in results:
        boxes = r.boxes
        for box in boxes:

            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            w, h = x2-x1, y2-y1
            cvzone.cornerRect(img, (x1, y1, w, h))

            # Confidence
            conf = math.ceil((box.conf[0]*100))/100

            # Class name
            cls = int(box.cls[0])

            cvzone.putTextRect(img, f'{classNames[cls]}  {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

    cv2.imshow("My_camera", img)
    cv2.waitKey(1)

