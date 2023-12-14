#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:48:00 2022

@author: meryemecedal
"""
import sys
import cv2
import torch
import numpy as np
import os
from facenet_pytorch.models.mtcnn import MTCNN

class FaceDetector(object):
    """
    Face detector class
    """

    def __init__(self, mtcnn):
        self.mtcnn = mtcnn

    def _draw(self, frame, boxes, probs, landmarks):
        """
        Draw landmarks and boxes for each face detected
        """
        try:
            for box, prob, ld in zip(boxes, probs, landmarks):
                # Draw rectangle on frame
                cv2.rectangle(frame,
                              (box[0], box[1]),
                              (box[2], box[3]),
                              (0, 0, 255),
                              thickness=2)

                # Show probability
                cv2.putText(frame, str(
                    prob), (box[2], box[3]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

                # Draw landmarks
                cv2.circle(frame, tuple(ld[0]), 5, (0, 0, 255), -1)
                cv2.circle(frame, tuple(ld[1]), 5, (0, 0, 255), -1)
                cv2.circle(frame, tuple(ld[2]), 5, (0, 0, 255), -1)
                cv2.circle(frame, tuple(ld[3]), 5, (0, 0, 255), -1)
                cv2.circle(frame, tuple(ld[4]), 5, (0, 0, 255), -1)
        except:
            pass

        return frame
    def run(self):
        """
            Run the FaceDetector and draw landmarks and boxes around detected faces
        """
        person= "Semih Ufuk Guler"
        classNumber=12

        os.chdir("/Users/meryemecedal/Desktop/maskesiz")

        video=os.listdir()
        cap = cv2.VideoCapture("Semih Ufuk Guler.mp4")
        color = (0,255,0)

        personFolder = os.path.join(person)
        if not os.path.exists(personFolder):
            os.mkdir(personFolder)
        os.chdir(personFolder)
        value=0
        count=0
        isSave=0
        while cap.isOpened():

            try:
                ret, frame = cap.read()
                if value %10==0:
                    # detect face box, probability and landmarks
                    cv2.imwrite(person + "_" + str(classNumber) + "_" + str(count) + ".jpg", frame)
                    isSave=1
                    boxes, probs, landmarks = self.mtcnn.detect(frame, landmarks=True)
                    # draw on frame
                    self._draw(frame, boxes, probs, landmarks)
                    #print(boxes[0])
                    topLeftX= int(boxes[0][0])
                    topLeftY= int(boxes[0][1])
                    bottomRightX= int(boxes[0][2])
                    bottomRightY= int(boxes[0][3])

                    h, w, _ = frame.shape
                    a = (topLeftX + bottomRightX) / 2
                    b = (topLeftY + bottomRightY) / 2
                    d = abs(topLeftX - bottomRightX)
                    c = abs(topLeftY - bottomRightY)

                    txtData = str(classNumber) + " " + str(a / w) + " " + str(b / h) + " " + str(d / w) + " " + str(
                        c / h)


                    f = open(person + "_" + str(classNumber) + "_" + str(count) + ".txt", "w+")
                    f.write(txtData)
                    f.close

                    count += 1
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                value+=1
            except:
               count += 1
               value += 1
               if isSave==0:
                   sys.exit('tamamlandı')

               if cv2.waitKey(1) & 0xFF == ord('q'):
                  break

               continue

            # Show the frame
            #cv2.imshow('Face Detection', frame)


        cap.release()
        cv2.destroyAllWindows()
        
        
# Run the app
mtcnn = MTCNN()
fcd = FaceDetector(mtcnn)
fcd.run()