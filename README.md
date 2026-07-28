# Medical Image Diagnosis using Deep Learning

A web-based deep learning application that detects multiple medical conditions from medical images using trained deep learning models and Flask. The application supports chest X-ray analysis, brain MRI tumor detection, and skin disease classification through a clean and responsive web interface.

---

## Supported Disease Categories

| # | Category | Classes | Model |
|---|---|---|---|
| 1 | Chest X-ray Disease Detection | NORMAL, PNEUMONIA | MobileNetV2 |
| 2 | Brain MRI Tumor Detection | Tumor, No Tumor | CNN |
| 3 | Skin Disease Classification | Benign, Malignant | CNN |

---

## Features

- Upload medical images through a responsive web interface
- Select disease detection category before prediction
- AI-based prediction using trained deep learning models
- Display prediction result with confidence score
- Display clinical recommendation based on the result
- Temporarily store uploaded images for preview
- Clean and responsive HTML/CSS interface

---

## Model Details

| Model File | Task | Architecture | Input Size |
|---|---|---|---|
| `medical_model.keras` | Chest X-ray (Normal vs Pneumonia) | MobileNetV2 | 128x128 |
| `brain_mri_model.keras` | Brain MRI (Tumor vs No Tumor) | CNN | 128x128 |
| `skin_disease.keras` | Skin Disease (Benign vs Malignant) | CNN | 128x128 |

All models are trained using TensorFlow/Keras and saved in the `.keras` format.

---

## Technologies

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Deep Learning | TensorFlow, Keras, MobileNetV2, CNN |
| Image Processing | OpenCV, NumPy, Pillow |
| Frontend | HTML, CSS |
| Environment | python-dotenv |

---

## Project Structure

```
Medical_Image_Diagnosis/
│
├── app.py                        # Flask application (routes + prediction logic)
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── .gitignore                    # Git ignore rules
│
├── model/
│   ├── medical_model.keras       # Chest X-ray model (MobileNetV2)
│   ├── brain_mri_model.keras     # Brain MRI tumor detection model
│   └── skin_disease.keras         # Skin disease classification model
│
├── static/
│   └── style.css                 # Application styles
│
├── templates/
│   └── index.html                # Web UI template
│
└── uploads/                      # Temporarily stores uploaded images
    └── .gitkeep
```

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/deshpandeprajakta03-tech/Medical_Image_Diagnosis.git
cd Medical_Image_Diagnosis
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## How to Run

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:8000
```

1. Select the disease detection category
2. Click **Choose File** and upload a medical image
3. Click **Predict Disease**
4. View the prediction result, confidence score, and recommendation

---

## Screenshots

> Screenshots will be added after final UI completion.

| Home Page | Prediction Result |
|---|---|
| _Coming soon_ | _Coming soon_ |

---

## Dataset Summary

| Dataset | Classes |
|---|---|
| Chest X-ray Dataset | Normal, Pneumonia |
| Brain MRI Dataset | Tumor, No Tumor |
| Skin Disease Dataset | Benign, Malignant |

---

## Future Enhancements

- Add support for additional disease categories (COVID-19, Tuberculosis, Retinal diseases)
- Add Grad-CAM heatmap visualization for model explainability
- Build a prediction history dashboard
- Implement user authentication and session management
- Deploy to cloud platforms (Azure, AWS, GCP, Render)
- Implement REST API endpoints for third-party integration
- Add multi-language support for broader accessibility

---

## Author

**Prajakta Deshpande**

- GitHub: [deshpandeprajakta03-tech](https://github.com/deshpandeprajakta03-tech)
