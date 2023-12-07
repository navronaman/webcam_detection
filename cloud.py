import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime

today_date = datetime.now()

cred = credentials.Certificate("key/serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
   "databaseURL": "https://webcam-detection-default-rtdb.firebaseio.com/",
    "storageBucket": "webcam-detection.appspot.com"
})

def format_time():
    # Get the current time
    current_time = datetime.now().strftime("%I:%M:%S %p")
    return current_time


def upload_image(image_path):
    print("Uploading image to Firebase Storage...")

    bucket = storage.bucket()
    blob = bucket.blob(today_date.strftime("%B %d, %Y") + "/" + image_path.split("/")[-1])

    # Upload the image to Firebase Storage
    blob.upload_from_filename(image_path)

    # Get the download URL of the uploaded image
    download_url = blob.public_url

    return download_url


def inti_cloud(image_path):
    print("Cloud integration started")

    ref = db.reference("Images")
    date_ref = ref.child(today_date.strftime("%B %d, %Y"))

    download_url = upload_image(image_path)

    date_ref.set({
        "Object entered the room": {
            "image_path": download_url,
            "exact_time": format_time()}
    })

    handle = db.reference("Images")

    print(ref.get())


if __name__ == "__main__":
    inti_cloud(image_path="images/trial.png")





