# 📸 Plate Recognition System with ESP32-CAM + YOLOv5 + OCR

Un système de reconnaissance automatique de plaques d'immatriculation utilisant l'ESP32-CAM pour capturer des images, YOLOv5 pour détecter les plaques, et un modèle OCR pour extraire les caractères. Idéal pour les applications IoT embarquées telles que le contrôle d'accès, le suivi de véhicules, ou les parkings intelligents.

---

## 🚀 Fonctionnalités

- Capture d'image via **ESP32-CAM**
- Détection des plaques avec **YOLOv5 (fine-tuné)**
- Lecture des caractères avec **OCR (Tesseract)**
- Interface API simple via **Flask** pour prédiction
- Compatible avec **streaming vidéo**, fichiers images ou requêtes HTTP POST
- Facilement déployable sur **PC local**, **serveur cloud** ou **Raspberry Pi**

---

## 📁 Structure du projet

```
📦 plate-recognition-system/
├── esp32-cam/
│   └── camera_post.ino          # Code Arduino pour envoyer les images au serveur
├── model/
│   └── best.pt                  # Modèle YOLOv5 fine-tuné (Roboflow)
├── server/
│   ├── app.py                   # API Flask pour détection + OCR
│   ├── utils.py                 # Fonctions de traitement YOLO/OCR
│   └── requirements.txt
├── dataset/
│   └── (Roboflow dataset téléchargé au format YOLOv5)
├── README.md
```

---

## ⚙️ Installation (côté serveur)

### 1. Cloner le dépôt
```bash
git clone https://github.com/ton-user/plate-recognition-system.git
cd plate-recognition-system/server
```

### 2. Créer un environnement virtuel (optionnel)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Télécharger le modèle
Placer `best.pt` dans le dossier `model/` (téléchargé depuis [Roboflow](https://roboflow.com)).

---

## 📡 Utilisation

### ▶️ Lancer le serveur Flask

```bash
python app.py
```

### 🔁 Envoyer une image depuis ESP32 ou Postman :

```http
POST /predict
Content-Type: multipart/form-data
Body: image (fichier .jpg ou .png)
```

Réponse JSON :
```json
{
  "plate": "1234-AB-56",
  "confidence": 0.87
}
```

---

## 📷 ESP32-CAM

Le firmware Arduino pour ESP32-CAM (`camera_post.ino`) permet de capturer une photo et de l’envoyer à votre serveur Flask via HTTP POST. Le projet est inspiré du guide :
👉 [ESP32-CAM POST Image to Server](https://randomnerdtutorials.com/esp32-cam-post-image-photo-server/)

---

## 🔍 Exemple de prédiction

<img src="example_plate_detection.jpg" width="400"/>

---

## 🧠 Modèle YOLOv5

- Entraîné via [Roboflow](https://roboflow.com)
- Base : `yolov5s.pt`
- Fine-tuning sur un dataset personnalisé de plaques d’immatriculation
- Format YOLOv5 (`images/`, `labels/`, `data.yaml`)

---

## 🧾 Dépendances

- Python ≥ 3.8
- [YOLOv5](https://github.com/ultralytics/yolov5)
- OpenCV
- Flask
- Pytesseract
- Requests (client ESP32)

---

## 📦 À venir

- Déploiement sur Raspberry Pi
- Dashboard web de suivi des plaques détectées
- Intégration base de données SQLite ou Firebase

---

## 👨‍💻 Auteur

**Ton Nom**  
Licence : MIT  
Projet réalisé dans le cadre d’un projet IoT utilisant le Deep Learning avec TensorFlow/PyTorch.

---
