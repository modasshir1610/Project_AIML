import tensorflow as tf
import numpy as np

def predict(image_path):
    model = tf.keras.models.load_model('/home/gulshan/Desktop/MyVityarthi/Project/Mango leave diseases Pridiction/trained_model.keras')

    image = tf.keras.preprocessing.image.load_img(image_path,target_size=(128,128))
    input_array = tf.keras.preprocessing.image.img_to_array(image)
    input_array = np.array([input_array])

    prediction = model.predict(input_array)
    result_index = np.argmax(prediction)

    return result_index

