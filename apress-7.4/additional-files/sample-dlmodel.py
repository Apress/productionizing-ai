import numpy as np
from numpy import array
import matplotlib.pyplot as plt

import os

from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.python.keras import layers, models, Model
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator, load_img
from tensorflow.python.keras.preprocessing.image import img_to_array

class Model():

    def runInference(self,dlImage):
        model = load_model("python/best-model-traffic-ESC.h5") # load model
        doc2infer = "static/uploads/" + dlImage

        test_datagen =  ImageDataGenerator(
            rescale=1./255
        )

        img_height, img_width = 224,224

        category_names = ["Bikes","Forbidden_for_traffic", "Intersection", "No_entry", "Pedestrians", "Right_of_way", "Slippery_road", "Speed_60", "Stop", "Yield"]

        img = image.load_img(doc2infer,color_mode='rgb', target_size=(224, 224))
        image_array = image.img_to_array(img)
        # if error "TypeError: __array__() takes 1 positional argument but 2 were given", line below required and PIL/Pillow needs to be downgraded to 8.2.0 from 8.3.0
        image_array = np.expand_dims(image_array, axis=0) 

        #normalize image
        image_array = image_array / 255.0

        # infer category
        pred = model.predict_classes([image_array])[0]
        print_msg = str(category_names[pred]) + " (probability: " + str(np.max(model.predict_proba([image_array])))+ ")"

        return print_msg
        

