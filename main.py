import cv2
import face_recognition
import os

import serial
import time

ser = serial.Serial('COM6',9600,timeout=1)
time.sleep(2)


# image = cv2.imread('images/Temurbek.jpg')
# face_loc = face_recognition.face_locations(image)[0]
#
# face_image_encoding = face_recognition.face_encodings(image, known_face_locations=[face_loc])[0]

# cap = cv2.VideoCapture('http://192.168.29.149:8080/video')
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# bput5927

data_path = "D:\PYTHON\OCV\l3\images"
image_files = os.listdir(data_path)
data_names = []
for i in image_files:
    data_names.append(f'images/{i}')
while True:
    ret, frame = cap.read()
    if ret == False: break
    frame = cv2.flip(frame, 1)

    face_locations = face_recognition.face_locations(frame)
    if face_locations != []:
        if len(face_locations) > 1:
            text = "1 tadan ortiq odam mumkin emas"
            color = (255, 0, 0)
            cv2.putText(frame, text, (100, 200), 3, 1.0, (50, 50, 255), 3)
            ser.write(b'F')
        else:
            face_location = face_locations[0]
            # for face_location in face_locations:
            face_frame_encodings = face_recognition.face_encodings(frame, known_face_locations=[face_location])[0]
            res = False
            name = ''
            for i in data_names:
                image = cv2.imread(i)
                face_loc = face_recognition.face_locations(image)[0]
                face_image_encoding = face_recognition.face_encodings(image, known_face_locations=[face_loc])[0]
                result = face_recognition.compare_faces([face_frame_encodings], face_image_encoding)
                if result[0] == True:
                    res = True
                    name = i.split('/')[1].split('.')[0]
            # result = face_recognition.compare_faces([face_frame_encodings], face_image_encoding)
            if res == True:
                text = name
                color = (0, 255, 0)
                ser.write(b'T')
            else:
                text = "Notanish"
                color = (50, 50, 255)
                ser.write(b'F')
            cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2] + 30),
                          color,
                          -1)
            cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), color,
                          2)
            cv2.putText(frame, text, (face_location[3], face_location[2] + 20), 2, 0.7, (255, 255, 255), 1)
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == 27 & 0xFF:
        break

cap.release()
cv2.destroyAllWindows()
