from flask import Flask, render_template, request, send_from_directory
import tensorflow as tf
import numpy as np
import cv2
import os
from datetime import datetime
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# MongoDB
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi


app = Flask(__name__)


# =====================================
# Environment Variables
# =====================================

load_dotenv()


# =====================================
# MongoDB
# =====================================

MONGO_ENABLED = False

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")


MONGO_AVAILABLE = False
predictions_collection = None


if MONGO_ENABLED:

    try:

        client = MongoClient(
            MONGO_URI,
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=10000
        )

        client.admin.command("ping")

        db = client[DB_NAME]

        predictions_collection = db[COLLECTION_NAME]

        MONGO_AVAILABLE = True

        print("MongoDB Connected")

    except Exception as e:

        print("MongoDB Error:", e)


# =====================================
# Paths
# =====================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR,"model")

UPLOAD_FOLDER = os.path.join(BASE_DIR,"uploads")


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER



# =====================================
# Load All Models
# =====================================


print("Loading Models...")


skin_model = tf.keras.models.load_model(
    os.path.join(
        MODEL_DIR,
        "skin_disease.keras"
    )
)


brain_model = tf.keras.models.load_model(
    os.path.join(
        MODEL_DIR,
        "brain_mri_model.keras"
    )
)


xray_model = tf.keras.models.load_model(
    os.path.join(
        MODEL_DIR,
        "medical_model.keras"
    )
)


print("All Models Loaded Successfully!")



# =====================================
# Load Classes
# =====================================


with open(
    os.path.join(MODEL_DIR,"class_names.txt")
) as f:

    skin_classes = [
        line.strip()
        for line in f.readlines()
    ]



with open(
    os.path.join(MODEL_DIR,"brain_classes.txt")
) as f:

    brain_classes = [
        line.strip()
        for line in f.readlines()
    ]



# X-ray classes
# Change if your file name is different

xray_classes = [
    "Normal",
    "Pneumonia"
]



# =====================================
# Image Preparation
# =====================================


def prepare_image(path,size):

    img = cv2.imread(path)

    img = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2RGB
    )

    img = cv2.resize(
        img,
        size
    )

    img = img.astype(
        np.float32
    )


    img = preprocess_input(img)


    img = np.expand_dims(
        img,
        axis=0
    )

    return img



# =====================================
# Display Uploaded Images
# =====================================


@app.route("/uploads/<filename>")
def uploaded_file(filename):

    return send_from_directory(
        UPLOAD_FOLDER,
        filename
    )



# =====================================
# Home Page
# =====================================


@app.route("/")
def home():
    return render_template("home.html")


# =====================================
# Prediction Pages
# =====================================


@app.route("/xray")
def xray():
    return render_template("xray.html")


@app.route("/mri")
def mri():
    return render_template("mri.html")


@app.route("/skin")
def skin():
    return render_template("skin.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")



# =====================================
# Prediction
# =====================================


@app.route(
    "/predict",
    methods=["POST"]
)

def predict():


    disease_type = request.form.get("disease", "xray")
    template_map = {"xray": "xray.html", "brain": "mri.html", "skin": "skin.html"}
    template = template_map.get(disease_type, "xray.html")

    if "image" not in request.files:
        return render_template(template, error="Please upload an image.")


    file = request.files["image"]



    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )


    file.save(filepath)



    # ==========================
    # Skin Disease
    # ==========================


    if disease_type=="skin":


        img = prepare_image(
            filepath,
            (224,224)
        )


        pred = skin_model.predict(img)[0][0]


        if pred >=0.5:

            result = skin_classes[1]

            confidence = pred*100


        else:

            result = skin_classes[0]

            confidence = (1-pred)*100



    # ==========================
    # Brain MRI
    # ==========================


    elif disease_type=="brain":


        img = prepare_image(
            filepath,
            (128,128)
        )


        pred = brain_model.predict(img)[0][0]


        if pred>=0.5:

            result = brain_classes[1]

            confidence = pred*100


        else:

            result = brain_classes[0]

            confidence = (1-pred)*100




    # ==========================
    # X-Ray
    # ==========================


    else:


        img = prepare_image(
            filepath,
            (128,128)
        )


        pred = xray_model.predict(img)[0][0]


        if pred>=0.5:

            result="Pneumonia"

            confidence=pred*100


        else:

            result="Normal"

            confidence=(1-pred)*100




    # =================================
    # Save MongoDB
    # =================================


    data={

        "date":datetime.now(),

        "filename":file.filename,

        "type":disease_type,

        "prediction":result,

        "confidence":round(float(confidence),2)

    }



    if MONGO_AVAILABLE:

        predictions_collection.insert_one(data)



    return render_template(
        template,
        prediction=result,
        confidence=round(float(confidence), 2),
        image=file.filename
    )




# =====================================
# Run
# =====================================


if __name__=="__main__":

    app.run(
        debug=True,
        port=8000,
        use_reloader=False
    )