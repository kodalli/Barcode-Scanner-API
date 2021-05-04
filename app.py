from flask import Flask, render_template, request, redirect
import os
from src.Barcode_Data_Extractor import BCR as bcr

app = Flask(__name__)

# app.config['IMAGE_UPLOADS'] = r'static\img\uploads'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload-image', methods=["GET", "POST"])
def upload_image():
    print(request.method)
    print(request.data)
    res = ""
    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            print(image)

            try:
                res = bcr.decode_file(image)
                print(res)
            except:
                print("Could not read barcode")

            return res
            # image.save(os.path.join(
            #     app.config['IMAGE_UPLOADS'], image.filename))

            # return request.url

    return render_template('upload_image.html', barcodeOutput=res)


if __name__ == "__main__":
    app.run(debug=True)

# $env:FLASK_APP = "app.py"
# $env:FLASK_ENV="development"
