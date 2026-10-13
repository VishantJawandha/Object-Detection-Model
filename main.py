import cv2
from ultralytics import YOLO
import pandas as pd

model = YOLO('yolov8s.pt')

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

def scaleDown(f, scl=0.2):
    f = cv2.resize(f, (int(f.shape[1]*scl), int(f.shape[0]*scl)))
    return f



import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")







def findObject(fframe):
    # Find Cars from
    orgFrame = fframe.copy()
    frame_copy = orgFrame.copy()

    # PREDICTION
    results = model(orgFrame)

    a = results[0].boxes.data
    px = pd.DataFrame(a).astype('float')

    for index, row in px.iterrows():

        x1, y1 = int(row[0]), int(row[1])
        x2, y2 = int(row[2]), int(row[3])
        d = int(row[5])
        c = class_list[d]

        if c:
            cx = int(x1 + x2) // 2
            cy = int(y1 + y2) // 2
            # Rectangle all the cars
            cv2.rectangle(frame_copy, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.circle(frame_copy, (cx, cy), 3, (0, 0, 255), -1)
            # Put Car Number
            cv2.putText(frame_copy, c , (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 4)
            cv2.putText(frame_copy, c , (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

           
    return frame_copy

# ------------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------

runForVideo = True #Change this to true for running in video

if runForVideo:

    video_src = 0
   # video_src = "video2.mp4"
    cap = cv2.VideoCapture(video_src, cv2.CAP_MSMF)                            # cv2.CAP_MSMF is for windows only
    frames_to_skip = 0 

 
    while True:
        
        for _ in range(frames_to_skip):
            ret, _ = cap.read()

            
            if not ret:
                print("Error: Failed to read frame from stream.")
                break
        _, frame = cap.read()
        if not _:
            break

        output = findObject(frame)
        cv2.imshow("Output",output)
        # cv2.imshow("BestCar", scaleDown(bestCar, .7))

        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

# runForImage = True

# if(runForImage):
#     myimg = cv2.imread('./img/image.jpg')
#     output = findObject(myimg)
#     cv2.imshow("Out", output)
#     # cv2.imshow("BestCar", bestCar)
#     # input()
#     cv2.destroyAllWindows()
    

