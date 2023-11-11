import sys, os
from utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from constant.application import APP_HOST, APP_PORT
from pipeline.prediction import PredictionPipeline



app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

clApp = ClientApp() 

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST", "GET"])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.classifier.predict()
        return jsonify(result)

        #os.system("yolo task=segment mode=predict model=artifacts/model_trainer/best.pt conf=0.25 source=data/inputImage.jpg save=true")

        #opencodedbase64 = encodeImageIntoBase64("runs/segment/predict/inputImage.jpg")
        #result = {"image": opencodedbase64.decode('utf-8')}

    except ValueError as val:
        print(val)
        return Response("Value not found inside json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)


if __name__ == "__main__":
    #clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT, debug=True)
