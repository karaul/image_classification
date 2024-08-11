# Image Classification Project

Welcome to the **Image Classification Project**! This project is designed to train a model for classifying images into different categories and then use that model to automatically sort images based on their predicted categories.

## Overview

This project consists of two main components:

1. **image_classification_model_trainer.py**: This script is responsible for training a CNN-based model to classify images into predefined categories.
2. **image_classification_app.py**: This script uses the trained model to classify images and sort them into corresponding folders.

## Libraries Used

The following libraries are used in this project:

- **[tensorflow](https://www.tensorflow.org/)**: TensorFlow is an open-source machine learning library used for training and inference in this project.
- **[argparse](https://docs.python.org/3/library/argparse.html)**: Argparse is used for parsing command-line arguments.
- **[os](https://python.readthedocs.io/en/stable/library/os.html)**: The OS module is used for directory and file manipulation.
- **[shutil](https://docs.python.org/3/library/shutil.html)**: Shutil is used for moving files across directories.

## Detailed Explanation

### `image_classification_model_trainer.py`

This script is the backbone of the project, responsible for training the image classification model. The key components of the script are:

- **ImageClassification Class**: This class handles the entire training process, from data preparation to model saving. It uses TensorFlow’s Keras API to build, compile, and train a convolutional neural network (CNN) model.
- **create_data_generators() Function**: This function sets up the data generators for training and validation using the ImageDataGenerator class. It resizes the images and applies scaling.
- **build_model() Function**: This function constructs a CNN model with multiple convolutional and pooling layers, followed by a dense layer and a softmax output layer for classification.
- **train_model() Function**: This function trains the model on the dataset using the data generators.
- **save_model() Function**: This function prompts the user to enter a model name and saves the trained model.

### `image_classification_app.py`

This script uses the trained model to classify images and sort them into folders based on their predicted category. The key components of the script are:

- **ImageClassifier Class**: This class loads the trained model, prepares the directories, and handles the classification of images.
- **classify_images() Function**: This function processes each image, predicts its category using the model, and moves the image to the corresponding folder.
- **_load_image() Function**: This function loads and preprocesses the image before it’s passed to the model for prediction.
- **_is_target_class() Function**: This function checks if the predicted class matches the target category.
- **_move_image() Function**: This function moves the image to the correct folder based on its predicted category.

### How It Works

1. **Model Training**:
    - The `image_classification_model_trainer.py` script reads images from the specified dataset directory.
    - The images are resized, scaled, and fed into a CNN model, which is trained to classify them into one of the predefined categories (e.g., cars, houses, ships).
    - The trained model is saved for later use.

2. **Image Classification**:
    - The `image_classification_app.py` script loads the trained model and processes images from a specified directory.
    - Each image is classified into one of the categories, and the script automatically moves the image to the corresponding folder.

## Dataset

The dataset used for training the model can be accessed via this [Dataset](https://drive.google.com/drive/folders/11sZkOEBnMTO0TO6hmpBReidg3I5bcHqZ?usp=sharing).

## Installation and Setup

To use this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/amiriiw/image_classification
    cd image_classification
    ```

2. Install the required libraries:

    ```bash
    pip install tensorflow argparse
    ```

3. Download and prepare your dataset, ensuring it's structured appropriately for training.

4. Run the model training script:

    ```bash
    python image_classification_model_trainer.py
    ```

5. Use the trained model to classify images:

    ```bash
    python image_classification_app.py --category <category> --path <path_to_images> --model <model_path>
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
