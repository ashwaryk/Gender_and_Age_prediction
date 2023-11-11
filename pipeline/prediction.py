import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
from constant.application import gender_dict
import numpy as np



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model('artifacts/model/')

        imagename = self.filename
        test_image = image.load_img(imagename, color_mode="grayscale", target_size=(128,128))
        img_array = np.array(test_image)
        img_array = img_array/255.0
        pred = model.predict(img_array.reshape(1, 128, 128, 1))

        pred_gender = gender_dict[round(pred[0][0][0])]
        print("Pred: ", pred_gender)
        pred_age = round(pred[1][0][0])
        print(pred_age)
        print("Predicted Gender:", pred_gender, "Predicted Age:", pred_age)
        return [{"Gender": pred_gender, "Age": pred_age}]
    
    
'''
def load_model():
    model = tf.keras.models.load_model('artifacts/model/')
    return model

def predict_image(image, model):
    # predict from model
    pred = model.predict((image).reshape(1, 128, 128, 1))
    pred_gender = gender_dict[round(pred[0][0][0])]
    pred_age = round(pred[1][0][0])
    print("Predicted Gender:", pred_gender, "Predicted Age:", pred_age)
    return [{"Gender": pred_gender, "Age": pred_age}]

'''       
