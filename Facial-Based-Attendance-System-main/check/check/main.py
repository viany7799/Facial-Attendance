import numpy as np
import face_recognition


import cv2
import os

def findEncodings(images):
  encodeList = []
  for img in images:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    encodeList.append(encode)
  return encodeList

def markAttendance(name):
  with open('Attendance.csv','r+') as f:
    myDataList = f.readlines()
    nameList = []
    for line in myDataList:
      entry = line.split(',')
      nameList.append(entry[0])
    if name not in nameList:
      now = datetime.now()
      #dtString = now.strftime('%H:%M:%S')
      f.writelines(f'n{name},{dtString}')

import xlsxwriter as xl
name = "attendance4c"
outsheet = xl.Workbook(name + ".xlsx")
sheet = outsheet.add_worksheet()
names = {"Vinay": [2, "5B7"], "Mahesh": [3, "5B7"],"badri": [4, "5C9"],"sujith": [5, "5B8"],"sandeep": [6, "513"],"Nomitha": [7, "088"]}

sheet.write("A1", "ROLLNUMBER")
sheet.write("B1", "NAME")
sheet.write("C1", "9.40AM to 10.40AM")
for a in names:
    abc=names[a]
    sheet.write("A" + str(abc[0]), abc[1])
    sheet.write("B" + str(abc[0]), a)
    sheet.write("C" + str(abc[0]), "absent")


from datetime import datetime
path = 'Student_image'

images = []
classNames = []
myList = os.listdir(path)
print(myList)
#myList=myList[1:]
print(myList)

for cl in myList:
  curImg = cv2.imread(f'{path}/{cl}')
  images.append(curImg)
  classNames.append(os.path.splitext(cl)[0])
print(classNames)

encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)
# print(encodeListKnown)


ccc = 0
while ccc <50:
  success, img = cap.read()
  #img = cv2.captureScreen()
  # print("img is",type(img),img)
 # img = cv2.imread("ctest.jpg")

  imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
  imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

  facesCurFrame = face_recognition.face_locations(imgS)
  #print(facesCurFrame, "len is ")
  if(len(facesCurFrame)>0):
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
      matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
      faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

      matchIndex = np.argmin(faceDis)

      if faceDis[matchIndex]<0.5 and matches[matchIndex]:
        name = classNames[matchIndex]
        print(name,faceDis,matchIndex)

        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        # markAttendance(name)

        out = names[name]
        # print("out is ",out)
        abc = out[0]
        sheet.write("C" + str(abc), "present")



  cv2.imshow("img is", img)
  cv2.waitKey(1)


  ccc += 1
outsheet.close()

