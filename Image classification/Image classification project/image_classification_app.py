"""----------------------------------------------------------------------------------------------------
well come, this is amiriiw, this is a simple project about Image classification.
       this file is the file which we classify the images.
----------------------------------------------------------------------------------------------------"""
# import what we need:
import os  # https://python.readthedocs.io/en/stable/library/os.html
import shutil  # https://docs.python.org/3/library/shutil.html
import tensorflow as tf  # https://www.tensorflow.org/
from PyQt5 import QtWidgets, QtGui  # https://www.riverbankcomputing.com/static/Docs/PyQt5/
from tensorflow.keras.models import load_model  # https://www.tensorflow.org/guide/keras
# ---------------------------------------------------------------------------------------


class ImageClassificationer:

    @staticmethod
    def image_classificationer(search, model_name, image_path):
        model = load_model(model_name)

        new_images_dir = 'result'
        car_folder = 'result/car'
        house_folder = 'result/house'
        ship_folder = 'result/ship'

        if not os.path.exists(new_images_dir):
            os.makedirs(new_images_dir)
        if search == "cars" and not os.path.exists(car_folder):
            os.makedirs(car_folder)
        if search == "houses" and not os.path.exists(house_folder):
            os.makedirs(house_folder)
        if search == "ships" and not os.path.exists(ship_folder):
            os.makedirs(ship_folder)

        for filename in os.listdir(image_path):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(image_path, filename)
                image = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
                image = tf.keras.preprocessing.image.img_to_array(image)
                image = tf.expand_dims(image, 0) / 255.0
                prediction = model.predict(image)[0]

                if search == "cars" and prediction[0] > prediction[1] and prediction[0] > prediction[2]:
                    shutil.move(img_path, os.path.join(car_folder, filename))
                    print(f"{filename} moved to car folder")
                elif search == "houses" and prediction[1] > prediction[0] and prediction[1] > prediction[2]:
                    shutil.move(img_path, os.path.join(house_folder, filename))
                    print(f"{filename} moved to house folder")
                elif search == "ships" and prediction[2] > prediction[0] and prediction[2] > prediction[1]:
                    shutil.move(img_path, os.path.join(ship_folder, filename))
                    print(f"{filename} moved to ship folder")
                else:
                    pass
        print("Process is done!")


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 380)
        self.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.rect().center())
        self.setStyleSheet("background-color: #1f2727; color: #d1f9f9;")

        self.setWindowTitle("Image Classification")

        self.layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel("Welcome to amiriiw Image Classification")
        self.label.setFont(QtGui.QFont("Arial", 16))
        self.layout.addWidget(self.label)

        self.model_label = QtWidgets.QLabel("Model name:")
        self.layout.addWidget(self.model_label)

        self.model_input = QtWidgets.QLineEdit()
        self.model_input.setPlaceholderText("Default is './image_classificationer_model.h5'")
        self.layout.addWidget(self.model_input)

        self.path_label = QtWidgets.QLabel("Images path:")
        self.layout.addWidget(self.path_label)

        self.path_input = QtWidgets.QLineEdit()
        self.path_input.setPlaceholderText("Default is './'")
        self.layout.addWidget(self.path_input)

        self.class_label = QtWidgets.QLabel("Classification:")
        self.layout.addWidget(self.class_label)

        self.class_combo = QtWidgets.QComboBox()
        self.class_combo.addItems(["cars", "houses", "ships"])
        self.layout.addWidget(self.class_combo)

        self.button = QtWidgets.QPushButton("Classify Images")
        self.button.clicked.connect(self.classify_images)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def classify_images(self):
        model = self.model_input.text() if self.model_input.text() else "image_classificationer_model.h5"
        image_path = self.path_input.text() if self.path_input.text() else "./"
        classification = self.class_combo.currentText()

        if not os.path.exists(model):
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid model name.")
            return

        if not os.path.exists(image_path):
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid image path.")
            return

        ImageClassificationer.image_classificationer(classification, model_name=model, image_path=image_path)
        QtWidgets.QMessageBox.information(self, "Done", "Image classification process is complete.")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
# -------------
