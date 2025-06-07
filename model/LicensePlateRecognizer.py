import yolov5
import easyocr
import cv2
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

class LicensePlateRecognizer:
    def __init__(self, img_path):
        self.__model =  yolov5.load('keremberke/yolov5n-license-plate')
        self.__model.conf = 0.5
        self.__model.iou = 0.45
        self.__model.agnostic = False
        self.__model.multi_label = False
        self.__model.max_det = 1000
        self.__reader = easyocr.Reader(['en', 'fr'], gpu=False)
        self.__img = cv2.imread(img_path)

    def predction(self):
        self.__result = self.__model(self.__img, size=640)
        self.__predictions = self.__result.pred[0]
        self.__boxes = self.__predictions[:, :4]
        print(f"Nombre de plaques détectées : {len(self.__result.pred[0])}")
        return self.__boxes
    
    def text_extraction(self):
        self.__boxes = self.predction()
        self.__output = []
        for i, box in enumerate(self.__boxes):
            self.__x1, self.__y1, self.__x2, self.__y2 = box.int()
            self.__cropped_plate = self.__img[self.__y1:self.__y2, self.__x1:self.__x2]
            self.__text_extracted = self.__reader.readtext(self.__cropped_plate)
            for detection in self.__text_extracted:
                self.__output.append({
                    "text": detection[1],
                    "confidence": float(detection[2]),
                    "bbox": [self.__x1, self.__y1, self.__x2, self.__y2]
                })
                return {
                    "count": len(self.__boxes),
                    "results": self.__output
                }
            

lpr = LicensePlateRecognizer("images/img3.png")
extracted_text = lpr.text_extraction()
print(extracted_text['results'])