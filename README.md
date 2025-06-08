# License Plate Recognition (LPR)

Ce projet implémente un système de reconnaissance de plaques d'immatriculation à partir d'images, en utilisant YOLOv5 pour la détection et EasyOCR pour l'extraction du texte.

## 📌 Fonctionnalités

- Détection de plaques d'immatriculation dans une image
- Extraction du texte contenu sur la plaque détectée
- Support multilingue (Français et Anglais)
- Basé sur les modèles open-source : `keremberke/yolov5n-license-plate` et EasyOCR

## 🖼️ Exemples d'utilisation

```python
from license_plate_recognizer import LicensePlateRecognizer

lpr = LicensePlateRecognizer()
lpr.load_image("images/image.png")
result = lpr.text_extraction(confidence_threshold=0.3)
print(result)
