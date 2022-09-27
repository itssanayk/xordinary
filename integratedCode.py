import cv2                                              # to solve computer vision problems
import numpy as np                                      # numerical and logical calculations on Array
import pyautogui                                        # to automate graphics user interface by simulating mouse cursor actions
class cnt:                                              # class declaration
   cnt=4                                                # may be four clicks required
def mouse_drawing(event, x, y, flags, params):
   if event == cv2.EVENT_LBUTTONDOWN:                      # detects left mouse button pressed or not and
       cnt.cnt-=1                                          # decrements the value of cnt for a click
       print("Remanng Clcks - ",cnt.cnt)                   # prints remaining clicks
       circles.append((x, y))                              # adds single item to the existing list
cap = cv2.VideoCapture(1)                                  # capture video frame by frame by accepting device index
cv2.namedWindow("Frame")                                   # a window with Frame name is created.
cv2.setMouseCallback("Frame", mouse_drawing)               # as soon as mouse draws, frame is called
circles = []                                               # empty object declaration
x1=0
y1=0
var = 5
while len(circles)!=4:                                      # checks if the number of items in circles is not = to 4
   _, frame = cap.read()                                    # capture image frame by frame
                                                            # cap.read()returns  true if frame is read correctly.
   for center_position in circles:
       cv2.circle(frame, center_position, 5, (0, 0, 255), -1)
      #cv2.circle(image,center_coordinates,radius,color,thickness)
      #image= image on which circle is to be drawn
      #center_coordinates= cnter of the circle (x axis , y axis) values
      #radius =radius of the circle
      #color = color of borderline of circle. For BGR (0,0,255) represents red color
      #thickness = thikness of the circle border line in px. -1 px will fill the circle shape by the red colour

   cv2.imshow("Frame", frame)
   #cv2.imshow(window name , image)
   #to display the image
   key = cv2.waitKey(1)         # waits  for 1 ms for the user to press any key
   if key == 27:                # escape key to stop...27 is the value printed when ESC key is pressed
       exit(0)
print("goto",circles)
while True:                         # run until infinite times
   _, frame = cap.read()            # capture frames every moment

   pts1 = np.float32([list(circles[0]),list(circles[1]),list(circles[2]),list(circles[3])])  #locates points of the document
   pts2 = np.float32([[0,0],[1920, 0],[0, 1080],[1920, 1080]])                               #or object we want to transform

   matrix = cv2.getPerspectiveTransform(pts1,pts2)
            # cv2.getPerspectiveTransform(src,dest)
   # applying perspective transform algorithms
   result = cv2.warpPerspective(frame, matrix, (1920, 1080))
   # applying perspective transform algorithms

   #cv2.imshow("Perspective transformation", result)

   m = cv2.resize(result, (1920, 1080))                 #resize the transformed image
       # cv2.resize( result, width,height)
   hsv = cv2.cvtColor(m, cv2.COLOR_BGR2HSV)             #convert to hsv
        # cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
        #src= color space which is to be changed
        # code= cv2.COLOR_BGR2HSV color space conversion code

   lower_red = np.array([0,34,250])#28,0,255
   upper_red = np.array([18,220,255])#37,161,255
   #lower_blue = np.array([129,115,165])#28,0,255
   #upper_blue = np.array([179,255,255])#37,161,255
   mask = cv2.inRange(hsv, lower_red, upper_red)         # create mask of image
   result1 = cv2.bitwise_and(m, m, mask=mask)
   #cv2.imshow("M", m)# ANDing both the values
   #contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   contours, _ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)     # identifying the shapes present in the image
   #contours are the line joining the point along the boundary of an image that are having the same intensity

   cv2.imshow("Perspective transformation", result1)        # visualise the image
   if len(contours)>0:                                         # if more than one shape is found
       contours=contours[0][0]
       #print(contours[0][0],contours[0][1])
       #pyautogui.click(contours[0][0],contours[0][1])
       #print(contours[len(contours)-1])
       var=1
       pyautogui.moveTo(x=contours[0][0],y=contours[0][1])          # moves mouse to the following x and y coordinates
       #pyautogui.click(button='left',x=contours[0][0],y=contours[0][1])
       #pyautogui.mouseDown(button='left',x=contours[0][0],y=contours[0][1])
       x1=contours[0][0]
       y1=contours[0][1]
   else:
       if var==1:
           pyautogui.mouseUp(button='left', x=x1,y=y1)              # move the mouse to x,y and then release the left button up
           var=2
   #cv2.imshow("result", result1)
   key = cv2.waitKey(1)
   if key == 27:        # when esc break
       break
cap.release()               # release software and hardware resource
cv2.destroyAllWindows()     # closes all the opened  windows at the same time