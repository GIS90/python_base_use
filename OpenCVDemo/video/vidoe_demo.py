# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
视频显示，读取，保存
------------------------------------------------
"""
import cv2


cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    print frame
    # import time
    # time.sleep(0.2q)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





