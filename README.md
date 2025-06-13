# 🫁 Lung-Colon-Disease Image Classification

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
- Test Set Accuracy: **96.94%**

The trained model is available here:  
**[Model download link to be added here]**

## Deployment

The final model is deployed using **Streamlit**, allowing users to upload a tissue image and receive a predicted class label in real time.

## Project Folder Structure

```
Lung-Colon-Disease-Classification/
│
├── colon_aca/ # Colon adenocarcinoma images
├── colon_n/ # Colon benign (normal) tissue images
├── lung_aca/ # Lung adenocarcinoma images
├── lung_n/ # Lung benign (normal) tissue images
├── lung_scc/ # Lung squamous cell carcinoma images
│
├── model/ # Trained TensorFlow model
├── app/ # Streamlit app code
├── Lung_Colon_Image Classifier.ipnyb/ # Training and preprocessing code
├── README.md # Project documentation
└── requirements.txt
```
> The original `colon_images_set/` and `lung_images_set/` folders were flattened for compatibility with `image_dataset_from_directory`.

---
