from flask import Flask, render_template
import os
import pydicom
import base64

IMAGE_FOLDER = os.path.join('app/static', 'medical_images')

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER
@app.route("/")
@app.route("/display")
def hello_world():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], '0003.dcm')
    ds = pydicom.dcmread(full_filename)
    # extract pixel data
    # print(ds)
    pixel_data_64 = base64.b64encode(ds.pixel_array)
    print(pixel_data_64)
    return render_template("index.html", pixel_data = pixel_data_64)