"""-----------------------------------------------------------------------------
well come, this is amiriiw, this is a simple project about Image classification.
       this file is the file which we classify the images.
-------------------------------------------------------"""
import os  # https://python.readthedocs.io/en/stable/library/os.html
import shutil  # https://docs.python.org/3/library/shutil.html
import argparse  # https://docs.python.org/3/library/argparse.html
import tensorflow as tf  # https://www.tensorflow.org/
from tensorflow.keras.models import load_model  # https://www.tensorflow.org/guide/keras
"""----------------------------------------------------------------------------------"""


class ImageClassifier:
    def __init__(self, model_name, image_path, category):
        self.model = load_model(model_name)
        self.image_path = image_path
        self.category = category.lower()
        self.result_dir = 'result'
        self.folders = {
            'cars': os.path.join(self.result_dir, 'car'),
            'houses': os.path.join(self.result_dir, 'house'),
            'ships': os.path.join(self.result_dir, 'ship')
        }
        self._prepare_directories()

    def _prepare_directories(self):
        os.makedirs(self.result_dir, exist_ok=True)
        if self.category in self.folders:
            os.makedirs(self.folders[self.category], exist_ok=True)

    def classify_images(self):
        for filename in os.listdir(self.image_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(self.image_path, filename)
                image = self._load_image(img_path)
                prediction = self.model.predict(image)[0]
                if self._is_target_class(prediction):
                    self._move_image(img_path, filename)
        print("Image classification process is complete.")

    def _load_image(self, img_path):
        image = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
        image = tf.keras.preprocessing.image.img_to_array(image)
        return tf.expand_dims(image, 0) / 255.0

    def _is_target_class(self, prediction):
        target_index = {'cars': 0, 'houses': 1, 'ships': 2}
        return prediction[target_index[self.category]] == max(prediction)

    def _move_image(self, img_path, filename):
        dest_folder = self.folders[self.category]
        shutil.move(img_path, os.path.join(dest_folder, filename))
        print(f"{filename} moved to {self.category} folder")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Image Classification CLI")
    parser.add_argument("category", choices=["cars", "houses", "ships"], help="Category to classify")
    parser.add_argument("--model", default="image_classificationer_model.h5", help="Path to the model file")
    parser.add_argument("--path", default="./", help="Path to the images")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    classifier = ImageClassifier(model_name=args.model, image_path=args.path, category=args.category)
    classifier.classify_images()
"""--------------------------"""
