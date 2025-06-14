import os
import json
from PIL import Image

import numpy as numpy
import tensorflow as tf

# Function to load and preprocess the image using Pillow
def load_and_preprocess_image(image_path, target_size=(256,256)):
  # Load the image
  img = Image.open(image_path)
  #Resize the image
  img = img.resize(target_size)
  # Convert the image to a numpy array
  img_array = np.array(img)
  # Add batch dimension
  img_array = np.expand_dims(img_array, axis=0)
  # Scale the image values to [0, 1]
  img_array = img_array.astype('float32')/ 255.
  return img_array

# Function to predict the class of an image
def predict_image_class(model, image_path, class_indices):
  preprocessed_image = load_and_preprocess_image(image_path)
  predictions = model.predict(preprocessed_image)
  predicted_class_index = np.argmax(predictions, axis=1)[0]  
  predicted_class_name = class_indices[predicted_class_index]
  return predicted_class_name


# Streamlit App

import streamlit as st

st.title("🫁 Lung Colon Disease Classifier")

uploaded_image = st.file_uploader("Upload an image:", type=['jpg', 'jpeg', 'png'])

if uploaded_image is not None:
	image = Image.open(uploaded_image)
	col1, col2 = st.columns(2)

	with col1:
		resized_image = image.resize(150,150)
		st.image(resized_image)

	with col2:
		if st.button('Classify'):
			prediction = predict_image_class(model, uploaded_image, class_indices)
			st.success(f'Prediction: {str(prediction)}')