import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


model=tf.keras.models.load_model("plant_disease_model.h5")


class_names= ['Apple___Black_rot', 'Apple___healthy', 'Corn___Common_rust', 'Grape___Black_rot', 
               'Potato___Early_blight', 'Potato___Late_blight', 'Strawberry___Leaf_scorch',
               'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___healthy',
               'Grape___healthy', 'Peach___Bacterial_spot', 'Cherry___Powdery_mildew',
               'Pepper___bell___Bacterial_spot', 'Tomato___Yellow_Leaf_Curl_Virus']



treatments=  {
    'Apple___Black_rot': 'Use fungicide sprays; remove infected fruit and leaves.',
    'Apple___healthy': 'No disease detected.',
    'Corn___Common_rust': 'Apply rust-resistant hybrids and fungicides.',
    'Grape___Black_rot': 'Apply Bordeaux mixture; prune infected parts.',
    'Potato___Early_blight': 'Use certified seed; apply fungicide early.',
    'Potato___Late_blight': 'Remove and destroy infected plants; apply metalaxyl.',
    'Strawberry___Leaf_scorch': 'Use resistant varieties; remove affected leaves.',
    'Tomato___Late_blight': 'Use copper-based fungicides; remove infected plants.',
    'Tomato___Leaf_Mold': ' Ensure air circulation; use protective fungicides.',
    'Tomato___healthy': 'No disease detected.',
    'Grape___healthy': 'No signs of disease.',
    'Peach___Bacterial_spot': 'Use bactericides and avoid overhead watering.',
    'Cherry___Powdery_mildew': 'Prune affected areas and apply sulfur spray.',
    'Pepper___bell___Bacterial_spot': 'Use resistant varieties and bactericides.',
    'Tomato___Yellow_Leaf_Curl_Virus': 'Control whiteflies and remove infected plants.'
}


st.title("Plant Disease Detection")
st.write("Upload a leaf image to identify the disease and get treatment advice.")

uploaded_file = st.file_uploader("Choose an image----> ", type=["jpg","png","jpeg"])


if uploaded_file is not None:
    img = Image.open(uploaded_file)
    
    st.image(img, caption='Uploaded Leaf Image ',use_column_width=True)

    img = img.resize((128, 128))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    
    
    predictions = model.predict(img_array)
    
    predicted_class = class_names[np.argmax(predictions)]
    
    
    confidence = np.max(predictions) * 100
    
    
    st.success(f"Predicted Disease: {predicted_class}")
    
    
    st.info(f"Confidence: {confidence:.2f}%")
    
    
    st.warning(f"Treatment: {treatments.get(predicted_class, 'No info available')}")
    
    
    
