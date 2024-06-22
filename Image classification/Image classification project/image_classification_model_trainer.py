"""----------------------------------------------------------------------------------------------------
well come, this is maskiiw, this is a simple project about Image classification.
       this file is the file which we train the Image classification model.
----------------------------------------------------------------------------------------------------"""
# import what we need:
from tensorflow.keras.models import Sequential  # https://www.tensorflow.org/guide/keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # https://www.tensorflow.org/guide/keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout  # https://www.tensorflow.org/guide/keras
# --------------------------------------------------------------------------------------------------------------------------


class ImageClassification:

    @staticmethod
    def model_trainer(bth_size=32, img_size=(224, 224), epochs=10, train_dir="dataset", model_name="image_classificationer_model.h5"):
        batch_size = bth_size
        image_size = img_size
        epochs = epochs
        train_dir = train_dir
        train_datagen = ImageDataGenerator(rescale=1. / 255, validation_split=0.2)

        train_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=image_size,
            batch_size=batch_size,
            class_mode="categorical",
            subset="training"
        )
        validation_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=image_size,
            batch_size=batch_size,
            class_mode="categorical",
            subset="validation"
        )
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

        model.fit(
            train_generator,
            epochs=epochs,
            validation_data=validation_generator
        )
        model.save(model_name)
# ---------------------------------------------------
