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
  
<img width="1912" height="842" alt="image" src="https://github.com/user-attachments/assets/9092ce87-4c4e-42a2-b830-0b600cd7ca53" />

<img width="1132" height="1420" alt="image" src="https://github.com/user-attachments/assets/b66102f1-84e7-4bbc-b158-e75af03c6843" />


## Technologies Used

1. TensorFlow / Keras (model training)
2. PIL / NumPy (image processing)
3. Seaborn / Matplotlib (evaluation)
4. Sklearn (confusion matrix, metrics)
5. Streamlit (app deployment)

## Video proof of App working:-

https://drive.google.com/file/d/1Ag25o0TGo-YBv6ekAW67h0i93jpe2z2T/view?usp=sharing

## Deployment Note:-

Due to version conflicts between streamlit and tensorflow in dependency resolution (specifically protobuf), deployment to Streamlit Cloud was not successful.

1. The application runs successfully on local system

2. Screenshots or video demo can be submitted as proof of functionality

3. Alternative deployment via Docker or local Flask app is possible


 ## Author Info:-

 Shobheet Sharma
 B.Tech (CSE), Lovely Professional University
 Intern, Advanced AI Program | Edunet Foundation

 ##  License:-

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project with proper credit.
