from pyexpat import model
from PIL import Image
from io import BytesIO
import numpy as np
from numpy.lib.type_check import imag
import tensorflow as tf
from keras.applications import imagenet_utils


input_shape = (224,224,3)

def load_model():
    model = tf.keras.applications.MobileNetV2(input_shape=input_shape)
    print("Model Loaded")
    return model

model = load_model()

def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

# def read_image(image_encoded):
    # pil_image = Image.open(BytesIO(image_encoded))
    # return pil_image

def preprocess(image: Image.Image):
    image = image.resize((224,224))
    image = np.asfarray(image)
    image = image / 127.5 - 1.0
    image = np.expand_dims(image,0)

    return image

# def predict(image: np.ndarray):
    # prediction = model.predict(image)
    # return prediction

def predict(image: np.ndarray):
    prediction = model.predict(image)
    prediction = imagenet_utils.decode_predictions(prediction)
    prediction = [item[1] for item in prediction[0]]
    return prediction
