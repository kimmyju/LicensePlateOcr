# Korean License Plate Recognition with YOLOv8 & EasyOCR

This project performs Korean license plate detection and recognition using **YOLOv8** for object detection and **EasyOCR** for text recognition.

> ★ If you found this repository useful, please support it by giving a ⭐!

---

## 📦 Requirements

Make sure the following environments and packages are installed:

- Python 3.9  
- **PyTorch 1.12.0** (with CUDA 11.3)  
- Follow the dependency requirements of [YOLOv8](https://github.com/ultralytics/ultralytics) and [EasyOCR](https://github.com/JaidedAI/EasyOCR)

> ✅ Ensure your environment satisfies the requirements of both YOLOv8 and EasyOCR for proper functionality.

---

## 🧪 Demo

To run the demo, simply execute:

```bash
python main.py
```

**Note**: You may need to manually modify the test image directory path (e.g., `'your/test/image/directory'`) inside `main.py` to match your own test image folder.

---

### 📁 (1) Project Directory Structure

Ensure your project directory follows this structure:

![Project Structure](https://github.com/kimmyju/LicensePlateOcr/assets/104639605/2f242188-302a-43b2-a65e-b94d75847dc2)

---

### 🔍 (2) Overall Process

The overall process of the program is illustrated in the example image below:

![Overall Process](https://github.com/user-attachments/assets/77a0be15-c24d-4b9b-894d-42d086f71c3f)

---

## 🏋️ Train on Custom Data

This project is based on:

- **YOLOv8** for license plate detection  
- **EasyOCR** for optical character recognition (OCR)

---

### 🗂 (1) Custom Dataset Used 

To recognize Korean license plates, we first fine-tuned the YOLOv8 model using a public dataset that contains non-Korean license plates.  
The dataset used for fine-tuning was obtained from Roboflow and can be found at the link below:

🔗 [License Plates Detection Dataset](https://universe.roboflow.com/bright-line-solutions/license-plates-detection-anpr)

---

### 🔧 (2) License Plate Detection Model

> YOLOv8 repository: [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)

Ensure your dataset directory structure is as follows:

![Dataset Structure](https://github.com/kimmyju/LicensePlateOcr/assets/104639605/a1d1b0c1-74cd-4194-859c-410fc0d12c18)

Below is an example of the detection result after fine-tuning YOLOv8 on the dataset:

![Detection Result](https://github.com/kimmyju/LicensePlateOcr/assets/104639605/02b6fb87-7826-4aee-97b2-b6ed7cfb0cc9)

---

### 🧠 (3) OCR Model

> EasyOCR repository: [JaidedAI/EasyOCR](https://github.com/JaidedAI/EasyOCR)

The final result below shows the extracted and recognized text from the detected license plates using EasyOCR:

![OCR Result](https://github.com/kimmyju/LicensePlateOcr/assets/104639605/3c2809dd-f646-491d-a34e-fb3383195a23)

**Note**: The detection model was fine-tuned on a custom dataset in this project.  
The OCR model uses **pretrained weights** provided by EasyOCR without additional training.
