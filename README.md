# Plant Disease Detection and treatment Recommendation  using AI

This is an AI- powered web app built using **Tensorflow** and **Streamlit** that allows users (especially farmers, agriculturists , and researchers) to detect plant diseases from leaf images and get **instant treatment recommendations**.


## Project Overview

Plant diseases can severely impact crop yield and food security. Manual disease detection is time-consuming and requires expert knowledge. This project automates the process using **deep learning**, allowing quick, accurate identification of plant diseases and how to treat them.


## Features:-

1. Upload a plant leaf image (JPG/PNG)
2. Detects disease using a **Convolutional Neural Network (CNN)** model trained on the PlantVillage dataset
3. Displays **confidence score** of prediction
4. Provides **treatment advice** for each disease
5. Deployed as a web app using **Streamlit**


## Model Details:-

1. Framework: **TensorFlow Keras**
2. Architecture: CNN (can be upgraded to MobileNetV2 for optimization)
3. Dataset: [PlantVillage](https://www.kaggle.com/datasets/emmarex/plantdisease)  
4. Image size: 128x128  
5. Classes: 15 plant diseases + healthy categories  
6. Final accuracy: **~87% on validation data**


## Sample Predictions:-

When a user uploads an image of a diseased leaf, the model processes the image and returns a prediction with high accuracy, along with a treatment recommendation.

Example Output:-
1. Uploaded Image: Grape leaf showing signs of black rot with dark spots and decaying edges

2. Predicted Disease : Grape__Black_rot

3. Confidence Score :  95.83%

4. Recommended Treatment: Apply Bordeaux mixture; prune infected parts


## Technologies Used

1. TensorFlow / Keras (model training)
2. PIL / NumPy (image processing)
3. Seaborn / Matplotlib (evaluation)
4. Sklearn (confusion matrix, metrics)
5. Streamlit (app deployment)

