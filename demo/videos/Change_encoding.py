import cv2

vid_capture = cv2.VideoCapture('test.mp4')
output = cv2.VideoWriter('test2.mp4', cv2.VideoWriter_fourcc(*'VP09'), 20, (1920,1080))
framenum = 0
while(vid_capture.isOpened()):
    framenum+=1
    print(framenum)
    ret, frame = vid_capture.read()
    if ret == True:
        output.write(frame)
    else: break
        
output.release()
vid_capture.release()
