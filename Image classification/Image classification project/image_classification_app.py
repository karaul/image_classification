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

    @staticmethod
    def image_classificationer(model_name="image_classificationer_model.h5", image_path="./"):

        model = load_model(model_name)

        new_images_dir = 'result'
        car_folder = 'result/car'
        house_folder = 'result/house'
        ship_folder = 'result/ship'
        trash_folder = 'result/trash'

        if not os.path.exists(new_images_dir):
            os.makedirs(new_images_dir)
        if not os.path.exists(car_folder):
            os.makedirs(car_folder)
        if not os.path.exists(house_folder):
            os.makedirs(house_folder)
        if not os.path.exists(ship_folder):
            os.makedirs(ship_folder)
        if not os.path.exists(trash_folder):
            os.makedirs(trash_folder)

        img_path = image_path
        for filename in os.listdir(img_path):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(img_path, filename)
                image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
                image = tf.keras.preprocessing.image.img_to_array(image)
                image = tf.expand_dims(image, 0) / 255.0
                prediction = model.predict(image)[0]

                if prediction[0] > prediction[1] and prediction[0] > prediction[2]:
                    shutil.move(image_path, os.path.join(car_folder, filename))
                    print(f"{filename} moved to car folder")
                elif prediction[1] > prediction[0] and prediction[1] > prediction[2]:
                    shutil.move(image_path, os.path.join(house_folder, filename))
                    print(f"{filename} moved to house folder")
                elif prediction[2] > prediction[0] and prediction[2] > prediction[1]:
                    shutil.move(image_path, os.path.join(ship_folder, filename))
                    print(f"{filename} moved to ship folder")
                else:
                    shutil.move(image_path, os.path.join(trash_folder, filename))
                    print(f"{filename} moved to trash folder")
        print("Process is done!")
# -----------------------------------
