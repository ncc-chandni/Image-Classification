# Stop Sign Classification Using ResNet18

![19aa347d-d2f6-4ccd-8844-470a5d3195d0](https://github.com/user-attachments/assets/03f9ef07-59b9-4d83-b632-78217d60a29d)
  

## Project Overview

This project aims to classify stop signs and non-stop signs using a deep learning model based on the ResNet18 architecture. By leveraging transfer learning, this application efficiently identifies stop signs in real-time, making it a vital tool for enhancing road safety and compliance.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Web Application](#web-application)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Technologies Used

- Python
- Flask
- PyTorch
- torchvision
- PIL (Pillow)
- HTML/CSS (for web interface)

## Model Training
This project utilizes the ResNet18 architecture for image classification. The model was trained on a dataset consisting of various images of stop signs and non-stop signs. The training process involved the following steps:

## Data Preprocessing: Images were resized and normalized to fit the model input requirements.
Transfer Learning: The ResNet18 model was fine-tuned with a custom final layer to classify the two classes.

Training & Evaluation: The model was trained using PyTorch, and the performance was evaluated based on accuracy metrics.


## Web Application
The web application is built using Flask. It allows users to upload images for classification and provides feedback based on the model's predictions. The web interface is designed to be user-friendly, enabling easy interaction with the model.

## Key Features:

User-friendly image upload form.

Real-time classification results displayed on the same page.

Responsive design for accessibility on various devices.
