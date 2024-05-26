"""----------------------------------------------------------------------------------------------------
well come, this is maskiiw, this is a simple project about Image classification.
       this file is the file which we classify the images.
----------------------------------------------------------------------------------------------------"""
# import what we need:
import os  # https://python.readthedocs.io/en/stable/library/os.html
import shutil  # https://docs.python.org/3/library/shutil.html
import tensorflow as tf  # https://www.tensorflow.org/
from tensorflow.keras.models import load_model  # https://www.tensorflow.org/guide/keras
# ---------------------------------------------------------------------------------------


class ImageClassificationer:

    model = load_model('image_classificationer_model.h5')

    new_images_dir = 'animals pics'
    dog_folder = 'animals pics/dog'
    cat_folder = 'animals pics/cat'
    trash_folder = 'animals pics/trash'

    for filename in os.listdir(new_images_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(new_images_dir, filename)
            image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
            image = tf.keras.preprocessing.image.img_to_array(image)
            image = tf.expand_dims(image, 0) / 255.0

            prediction = model.predict(image)[0][0]

            if prediction > 0.5:
                shutil.move(image_path, os.path.join(dog_folder, filename))
            elif prediction <= 0.5:
                shutil.move(image_path, os.path.join(cat_folder, filename))
            else:
                shutil.move(image_path, os.path.join(trash_folder, filename))
            print("prosess is done!")
# -----------------------------------
