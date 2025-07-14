# Plant Disease Detection and treatment Recommendation  using AI

This project is developed as part of the **Advanced AI Internship by Edunet Foundation**.  
It is an AI-powered image classification tool that allows users — especially **farmers, agriculturists, and researchers** — to detect plant diseases from leaf images and receive **instant treatment recommendations**.


## Project Overview

Plant diseases pose a major threat to global agriculture, affecting both **yield** and **food security**. Traditional diagnosis methods are slow, labor-intensive, and require domain expertise.

This project automates the detection process using **Deep Learning** — specifically a **Convolutional Neural Network (CNN)** — trained on the **PlantVillage dataset**. The tool provides:
1. Accurate disease classification from leaf images
2. Treatment advice based on the prediction
3. A user-friendly local interface (Streamlit-based)


## Features:-

1. Upload plant leaf image (JPG or PNG)
2. Predict disease class using CNN
3. Show confidence score
4. Recommend treatment for the detected disease
5. Runs as a **local web app** using Streamlit (`streamlit run app.py`)

> ❗ Note: Streamlit Cloud deployment is **not active** due to package compatibility issues. However, the project works **perfectly when run locally**.


## Model Details:-

1. Framework: **TensorFlow Keras**
2. Architecture: CNN (can be upgraded to MobileNetV2 for optimization)
3. Dataset: [PlantVillage](https://www.kaggle.com/datasets/emmarex/plantdisease)  
4. Image size: 128x128  
5. Classes: 15 plant diseases + healthy categories  
6. Final accuracy: **~87% on validation data**

- Potential for upgrade: **MobileNetV2** or **EfficientNet** for real-time mobile support.
  

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


