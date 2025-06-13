# 🫁 Lung-Colon-Disease-Image-Classification

## Project Overview

This project classifies medical images of lung and colon tissues into five distinct classes using a convolutional neural network (CNN). The aim is to assist in early diagnosis of cancer by identifying whether a tissue image is normal or cancerous.

The model classifies input images into the following categories:
- `lung_n`: Lung benign (normal) tissue
- `lung_aca`: Lung adenocarcinoma
- `lung_scc`: Lung squamous cell carcinoma
- `colon_aca`: Colon adenocarcinoma
- `colon_n`: Colon benign (normal) tissue

## Dataset

The dataset was sourced from Kaggle and contains high-resolution tissue images labeled into five classes.  
**(https://www.kaggle.com/datasets/andrewmvd/lung-and-colon-cancer-histopathological-images)**

### Class Descriptions

1. **lung_n** (Lung Benign Tissue)  
   Non-cancerous lung tissue. These healthy examples help the model recognize what normal tissue looks like.

2. **lung_aca** (Lung Adenocarcinoma)  
   A type of lung cancer arising from mucus-secreting glands, typically located in the outer parts of the lungs.

3. **lung_scc** (Lung Squamous Cell Carcinoma)  
   Cancer that originates from squamous cells lining the lung airways. Strongly linked to smoking.

4. **colon_aca** (Colon Adenocarcinoma)  
   A common form of colon cancer that originates in glandular tissue lining the colon walls.

5. **colon_n** (Colon Benign Tissue)  
   Healthy colon tissue with no signs of malignancy. Helps the model identify normal scans.

## Model and Approach

This project uses **TensorFlow** to build a convolutional neural network capable of learning visual patterns in tissue samples.

- Framework: **TensorFlow (Keras)**
- Architecture: CNN
- Format: `.keras` model file
- Test Set Accuracy: **96.94%**

The trained model is available here:  
**https://drive.google.com/drive/folders/1cr4MrM9sfZbX1TzHWSBcW9K_6Rww-1d9?usp=drive_link**

## Deployment

The final model is deployed **locally** using **Streamlit**, allowing users to upload a tissue image and receive a predicted class label in real time.

## How to Run the Project Locally

### Step 1: Clone the Repository
```
git clone https://https://github.com/dishydammy/Lung-Colon-Disease-Image-Classification.git
cd Lung-Colon-Disease-Image-Classification
```

### Step 2: Create a Virtual Environment
```
python -m venv venv
```

### Step 3: Activate the Virtual Environment
```
source venv/bin/activate
```

### Step 4: Install Dependencies
```
pip install -r requirements.txt
```

### Step 5: Download the Trained Model
- Go to the model download link provided above.
- Save the .keras model file in the project root directory (where app.py is located).

### Step 6: Run the Streamlit App
```
streamlit run app.py
```
This will open the app in your default browser. Upload an image to get the prediction.


## Project Folder Structure

```
lung-colon-disease-classification/
│
├── app.py                            # Streamlit application for image prediction
├── Lung_Colon_Image Classifier.ipynb # Jupyter Notebook for training and evaluation
├── requirements.txt                  # Python dependencies
├── class_indices.json                # Mapping of class indices to class labels
└── model.keras                       # Trained model (user must download and place here manually)
```
> The original `colon_images_set/` and `lung_images_set/` folders were flattened for compatibility with `image_dataset_from_directory`.

---
