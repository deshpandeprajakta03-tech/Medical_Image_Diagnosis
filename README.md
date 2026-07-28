# Medical Image Diagnosis using MobileNetV2

A web-based deep learning application that detects **Pneumonia** from chest X-ray images using **MobileNetV2** and **Flask**. Every prediction is automatically stored in **MongoDB Atlas** for record-keeping.

---

## Features

- Upload a chest X-ray image through a clean web interface
- Predict **NORMAL** or **PNEUMONIA** using a trained MobileNetV2 model
- Display confidence score for each prediction
- Display a clinical recommendation based on the result
- Store every prediction record in MongoDB Atlas
- Responsive UI built with HTML and CSS

---

## Technologies

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Deep Learning | TensorFlow, Keras, MobileNetV2 |
| Image Processing | OpenCV, NumPy |
| Database | MongoDB Atlas |
| Environment | python-dotenv |
| Deployment | Gunicorn |
| Frontend | HTML, CSS |

---

## Project Structure

```
Medical_Image_Diagnosis/
│
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── .env                      # Environment variables (not committed)
├── .gitignore
│
├── model/
│   ├── medical_model.keras   # Trained MobileNetV2 model
│   └── class_names.txt       # Class labels (NORMAL, PNEUMONIA)
│
├── static/
│   └── style.css             # Application styles
│
├── templates/
│   └── index.html            # Web UI template
│
└── uploads/                  # Temporarily stores uploaded images
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

## MongoDB Atlas Setup

1. Go to [https://www.mongodb.com/atlas](https://www.mongodb.com/atlas) and sign in
2. Create a free cluster (M0)
3. Under **Database Access**, create a database user with read/write permissions
4. Under **Network Access**, add your IP address (or `0.0.0.0/0` for all)
5. Click **Connect** on your cluster and copy the connection string
6. Replace `<username>` and `<password>` with your database user credentials

---

## Environment Variables

Create a `.env` file in the project root with the following keys:

```
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
DB_NAME=medical_diagnosis_db
COLLECTION_NAME=predictions
```

> The `.env` file is listed in `.gitignore` and will never be committed to GitHub.

---

## How to Run

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:8000
```

1. Click **Choose File** and select a chest X-ray image
2. Click **Predict Disease**
3. View the prediction, confidence score, and recommendation
4. The result is saved automatically to MongoDB Atlas

---

## Future Enhancements

- Add support for multi-class disease classification (e.g., COVID-19, TB)
- Add a prediction history dashboard reading from MongoDB
- Implement user authentication
- Deploy to cloud platforms (Render, AWS, GCP)
- Add Grad-CAM heatmap visualization for model explainability
- Implement REST API endpoints for integration with other services

---

## Author

**Prajakta Deshpande**

- GitHub: [deshpandeprajakta03-tech](https://github.com/deshpandeprajakta03-tech)
