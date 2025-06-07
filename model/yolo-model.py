import yolov5
import cv2
import numpy as np
# Chargement de modéle
model = yolov5.load('keremberke/yolov5n-license-plate')

# les parametres du modéle
model.conf = 0.50 
model.iou = 0.45  
model.agnostic = False  
model.multi_label = False 
model.max_det = 1000

img = cv2.imread('images/img2.jpg')
results = model(img, size=640)

# Predictions
predictions = results.pred[0]
boxes = predictions[:, :4]


print("boxes: ", boxes.tolist()[0])

for i, box in enumerate(boxes):
    x1, y1, x2, y2 = box.int()
    cropped_plate = img[y1:y2, x1:x2] 
    cv2.imwrite(f"result/cropped_plate.jpg", cropped_plate)

