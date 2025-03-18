import cv2
print(cv2.__version__)
print(hasattr(cv2, 'face'))

import numpy as np
from PIL import Image
import os
import cv2

def train_classifier(data_dir):
    # Ensure the directory exists
    if not os.path.isdir(data_dir):
        print(f"Error: The directory {data_dir} does not exist.")
        return
    
    # Generate a list of image paths from the data directory
    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
    
    faces = []
    ids = []

    for image_path in path:
        try:
            # Open the image and convert it to grayscale
            img = Image.open(image_path).convert('L')
            image_np = np.array(img, 'uint8')
            
            # Extract the ID from the filename, assuming a format like "subject.ID.jpg"
            filename = os.path.basename(image_path)
            id_str = filename.split(".")[1]
            
            # Validate ID
            id = int(id_str)
            
            faces.append(image_np)
            ids.append(id)
        
        except Exception as e:
            print(f"Error processing image {image_path}: {e}")

    if len(faces) == 0:
        print("No faces found, or there was an error processing images.")
        return

    ids = np.array(ids)

    # Initialize the face recognizer and train it
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    
    # Save the trained classifier to a file
    clf.write("classifier.xml")
    print("Training complete and classifier saved as classifier.xml")

train_classifier("data")
