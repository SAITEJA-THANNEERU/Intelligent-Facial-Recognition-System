import cv2
import os

def generate_dataset():
    # Load the pre-trained face detection model
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    def face_cropped(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) == 0:
            return None
        
        # Assuming only one face per image
        for (x, y, w, h) in faces:
            cropped_face = img[y:y+h, x:x+w]
        
        return cropped_face
    
    # Open the camera
    cap = cv2.VideoCapture(0)  # Usually 0 is the default camera

    # Directory to save the dataset
    output_dir = "data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    id = 1
    img_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Crop the face from the frame
        face = face_cropped(frame)
        if face is not None:
            img_id += 1
            face = cv2.resize(face, (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            file_name_path = os.path.join(output_dir, f"user.{id}.{img_id}.jpg")
            cv2.imwrite(file_name_path, face)
            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("Cropped face", face)
        
        if cv2.waitKey(1) == 13 or img_id >= 200:  # 13 is the Enter key ASCII value
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()
    print("Collecting samples is completed....")

# Call the function
generate_dataset()
