from flask import Flask, request, render_template
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import os

app = Flask(__name__)

# Load the trained model
model = models.resnet18()
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 2)
model.load_state_dict(torch.load('resnet18_stop_sign_classifier.pth', weights_only=True))
model.eval()  # Set the model to evaluation mode

# Define transformations for incoming images
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return 'No file uploaded.', 400
    file = request.files['file']
    if file.filename == '':
        return 'No file selected.', 400

    # Process the image
    image = Image.open(file)
    image = transform(image).unsqueeze(0)  # Add batch dimension

    # Make prediction
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
        prediction = 'Stop' if predicted.item() == 1 else 'Not Stop'

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
