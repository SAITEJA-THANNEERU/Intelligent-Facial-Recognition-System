# this file works on genetarating data set (collects samples of 200)
import cv2

def generate_dataset():
    face_classifier = cv2.CascadeClassifier("haarcascade_frontface_default.xml")
    def face_cropped(img):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray,1.3,5)
        # 1.3 means scaling factor
        # 5 means minimum neighbor 

        if faces is ():
            return None
        for (x,y,w,h) in faces:
            cropped_face = img[y:y+h,x:x+w]
        return cropped_face
    
    cap = cv2.VideoCapture(0) #0 means video capture from laptop
    id = 2 # id of first autorized person
    img_id=0

    while True:
        ret,frame = cap.read()
        if face_cropped(frame) is not None:
            img_id+=1
            face = cv2.resize(face_cropped(frame),(200,200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
            cv2.imwrite(file_name_path,face)
            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255),2)
            #(50,50) Is the origin point from where text is to be written 
            # 1 = font scale 
            # 2 = thickness

            cv2.imshow("cropped face",face)
        if cv2.waitKey(1)== 13 or int(img_id)==200:   # 200 are images colleceted
                break
    cap.release()
    cv2.destroyAllWindows()
    print("Collecting samples is completed...")
generate_dataset()