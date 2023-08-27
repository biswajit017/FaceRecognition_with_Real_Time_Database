import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendance-realtime-df344-default-rtdb.firebaseio.com/",
    'storageBucket':"faceattendance-realtime-df344.appspot.com"
})


#importing the student Images into  a list
folderPath = 'Images'
PathList = os.listdir(folderPath)
print(PathList)
imgList =[]
studentIds=[]
for path in PathList: 
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentIds.append(os.path.splitext(path)[0])
    #print(path)
    #print(os.path.splitext(path)[0])
# print(len(imgList))
# print(studentIds)
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

def findEncodings(imagesList):
    encodeList=[]
    for img in imagesList:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #opencv uses BGR but face_recognition uses RGB
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList
print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
# print(encodeListKnown)
encodeListKnownWithIds=[encodeListKnown,studentIds]
print("Encoding Completed..!")

file = open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("file Saved")


# encoding in face recognition, just remember that it's like creating a special 
# fingerprint for each face using numbers. This allows the computer to compare and 
# recognize faces accurately based on their unique features.