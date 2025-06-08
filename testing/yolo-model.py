import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import yolov5
import cv2
import easyocr
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Chargement de modéle
model = yolov5.load('keremberke/yolov5n-license-plate')
# Text Extraction
reader = easyocr.Reader(['en', 'fr'], gpu=False)

# les parametres du modéle
model.conf = 0.50 
model.iou = 0.45  
model.agnostic = False  
model.multi_label = False 
model.max_det = 1000

img = cv2.imread('images/image.png')
results = model(img, size=640)

# Predictions
predictions = results.pred[0]
boxes = predictions[:, :4]
print(f"Nombre de plaques détectées : {len(results.pred[0])}")
best_text = None
best_conf = 0
confidence_threshold=0.2
for i, box in enumerate(boxes):
    x1, y1, x2, y2 = box.int()
    cropped_plate = img[y1:y2, x1:x2] 
    cv2.imshow(f"cropped_plate_{i}", cropped_plate)
    cv2.waitKey(0)
    result_text = reader.readtext(cropped_plate)
    for detection in result_text:
        text = detection[1]
        confidence = detection[2]
        if confidence > confidence_threshold and 5 <= len(text) <= 10:
            if confidence > best_conf:
                best_text = text
                best_conf = confidence
print(f"Texte : {best_text}, Confiance : {best_conf}")        