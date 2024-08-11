"""-----------------------------------------------------------------------------
well come, this is amiriiw, this is a simple project about Image classification.
       this file is the file which we train the Image classification model.
------------------------------------------------------------------------"""
from tensorflow.keras.models import Sequential  # https://www.tensorflow.org/guide/keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # https://www.tensorflow.org/guide/keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout  # https://www.tensorflow.org/guide/keras
"""--------------------------------------------------------------------------------------------------------------------------"""


class ImageClassification:
    def __init__(self, train_dir="dataset", model_name="image_classificationer_model.h5"):
        self.train_dir = train_dir
        self.model_name = model_name
        self.train_datagen = ImageDataGenerator(rescale=1.0 / 255, validation_split=0.2)
        self.train_generator, self.validation_generator = self.create_data_generators()
        self.model = self.build_model()

    def create_data_generators(self):
        train_generator = self.train_datagen.flow_from_directory(
            self.train_dir,
            target_size=(224, 224),
            batch_size=32,
            class_mode="categorical",
            subset="training"
        )
        validation_generator = self.train_datagen.flow_from_directory(
            self.train_dir,
            target_size=(224, 224),
            batch_size=32,
            class_mode="categorical",
            subset="validation"
        )
        return train_generator, validation_generator

    def build_model(self):
        model = Sequential([
            Conv2D(32, (3, 3), activation="relu", input_shape=(224, 224, 3)),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation="relu"),
            MaxPooling2D((2, 2)),
            Conv2D(128, (3, 3), activation="relu"),
            MaxPooling2D((2, 2)),
            Flatten(),
            Dense(512, activation="relu"),
            Dropout(0.5),
            Dense(3, activation="softmax")
        ])
        model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
        return model

    def train_model(self, epochs=10):
        self.model.fit(
            self.train_generator,
            epochs=epochs,
            validation_data=self.validation_generator
        )

    def save_model(self):
        model_path = input(f"Enter the name to save your model (default: {self.model_name}): ") or self.model_name
        self.model.save(model_path)
        print(f"Model saved as {model_path}")


if __name__ == "__main__":
    classifier = ImageClassification()
    classifier.train_model()
    classifier.save_model()
"""---------------------"""
