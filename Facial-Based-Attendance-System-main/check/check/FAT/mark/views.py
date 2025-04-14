from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
import numpy as np
import face_recognition
from datetime import datetime

import cv2
import os
import xlsxwriter as xl
import base64
import cv2
import time

import numpy as np
from django.http import StreamingHttpResponse

from django.http import JsonResponse
from django.shortcuts import render
# from django.utils.baseconv import base64
import base64
from django.http import JsonResponse

from .models import Attendance



def process_frames(request):
      frame_data = request.POST.get('frame_data')
      encoded_data=frame_data.split(",")[1]
      img_bytes=base64.b64decode(encoded_data)
      img_array=np.frombuffer(img_bytes,dtype=np.uint8)
      img=cv2.imdecode(img_array,flags=cv2.IMREAD_COLOR)
      #print(img)
      name=capture(img)
      #cv2.imshow("img",img)
      #cv2.waitKey(1)

      # if name[1]=='19R11A05B5':
      #     s='R'+name[1]
      #     obj=obj(s='present')
      #     obj.save()
      s='R'+name[1]
      table_row[s]='present'


      return JsonResponse({'result': name[1]})


def index(request):
    return render(request,'index.html')


# def findEncodings(images):
#     encodeList = []
#     for img in images:
#         if img is None:
#             print("Skipped an unreadable image.")
#             continue
#         rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encodings = face_recognition.face_encodings(rgb_img)
#         if encodings:  # only if a face is detected
#             encode = encodings[0]
#             encodeList.append(encode)
#         else:
#             print("No face found in an image, skipping.")
#     return encodeList

def findEncodings(images):
  encodeList = []
  for img in images:
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    encodeList.append(encode)
    print("encode")
  return encodeList
#
# def markAttendance(name):
#   with open('Attendance.csv','r+') as f:
#     myDataList = f.readlines()
#     nameList = []
#     for line in myDataList:
#       entry = line.split(',')
#       nameList.append(entry[0])
#     if name not in nameList:
#       now = datetime.now()
#       #dtString = now.strftime('%H:%M:%S')
#       f.writelines(f'n{name},{dtString}')


def home(request):
    global table_row
    table_row={}
    if request.method=='POST':
        year = request.POST.get('year')
        branch = request.POST.get('branch')
        section = request.POST.get('section')
        date = request.POST.get('date')
        period = int(request.POST.get('period'))
        table_row['year']=year
        table_row['branch']=branch
        table_row['section']=section
        table_row['date']=date
        table_row['period']=period

        # request.session['year']=year
        # request.session['branch'] = branch
        # request.session['section'] = section
        # request.session['date'] = date
        # request.session['period'] = period


    name = "attendance41c"
    global outsheet
    outsheet = xl.Workbook(name + ".xlsx")
    global sheet
    sheet = outsheet.add_worksheet()

    global names
    names = {"Vinay": [2, "19R11A05B5"], "Mahesh": [3, "19R11A05B7"], "badri": [4, "19R11A05C9"], "Nithin": [5, "19R11A0516"],
             "sandeep": [6, "20R15A0513"], "Nomitha": [7, "088"] ,"Aditya":[8,"19R11A04C2"],"teja":[9,"160220735077"],"charan":[10,"160220735070"],"nomitha":[11,"160220735088"],"vikram":[12,"160220735120"],"pranathi":[13,"160220735090"]}

    sheet.write("A1", "ROLLNUMBER")
    sheet.write("B1", "NAME")
    sheet.write("C1", "9.40AM to 10.40AM")
    for a in names:
        abc = names[a]
        sheet.write("A" + str(abc[0]), abc[1])
        sheet.write("B" + str(abc[0]), a)
        sheet.write("C" + str(abc[0]), "absent")
    path = 'C:/Users/Dell/Downloads/Facial-Based-Attendance-System-main/Facial-Based-Attendance-System-main/check/check/Student_image'
    # path = 'C:/Users/Dell/Downloads/Images'
    images = []
    global classNames
    classNames = []
    myList = os.listdir(path)
    print(myList)
    # myList=myList[1:]
    print(myList)

    for cl in myList:
        img = cv2.imread(f'{path}/{cl}')
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow("Image Window", img)
        cv2.waitKey(0)        # Wait until any key is pressed
        cv2.destroyAllWindows()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        images.append(img)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    global encodeListKnown
    print(images)
    encodeListKnown = findEncodings(images)
    # for cl in myList:
    #     img_path = f'{path}/{cl}'
    #     img = cv2.imread(img_path)
    #     if img is None:
    #         print(f"Warning: Could not load image {img_path}")
    #         continue
			
    #     if len(img.shape) != 3 or img.shape[2] != 3:
    #         print(f"Warning: Image {img_path} is not a 3-channel color image")
    #         continue
    #     # No need to convert to RGB here, your findEncodings function does that
		
    #     images.append(img)
    #     classNames.append(os.path.splitext(cl)[0])

    # print(f"Loaded {len(images)} images successfully")
    # print(classNames)
    # global encodeListKnown
    # print(images)
    # encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    return render(request,'home.html')

def main(request):
    return  render(request,"main.html")

def filter(request):
    return render(request,"filter.html")

def table(request):
    if request.method=='POST':
        year = request.POST.get('year')
        branch = request.POST.get('branch')
        section = request.POST.get('section')
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')

        #print(year,branch,section,fromdate,todate)
        columns= Attendance._meta.get_fields()
        table_columns=[]
        for c in columns:
            table_columns.append(c.name)

        obj = Attendance.objects.filter(date__range=[fromdate,todate]).values()
        student_mat=[]
        for row in obj:
            l=[]
            for c in table_columns:
                l.append(row[c])
            student_mat.append(l)

        #print(student_mat)
        context={'records':student_mat,'columns':table_columns}



    return  render(request,"table.html",context)

def download(request):
    #outsheet.close()
    #print("sheet is closed")
    print(table_row)
    try:
        object1=Attendance.objects.get(year=table_row['year'],branch=table_row['branch'],section=table_row['section'],date=table_row['date'],period=table_row['period'])
        if object1 is not None:
            object1.delete()
            obj = Attendance(**table_row)
            obj.save()
    except:


        obj=Attendance(**table_row)
        obj.save()
    return HttpResponse("Success")

def capture(img):
    out=None

    if(img.any()!=None):

        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        # print(facesCurFrame, "len is ")
        if (len(facesCurFrame) > 0):
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

                matchIndex = np.argmin(faceDis)

                if faceDis[matchIndex] < 0.5 and matches[matchIndex]:
                    name = classNames[matchIndex]
                    print(name, faceDis, matchIndex)


                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    # markAttendance(name)

                    out = names[name]
                    print("out is ",out)
                    abc = out[0]
                    sheet.write("C" + str(abc), "present")

    print("closed")
    return out




#def manual_attendance(request):
