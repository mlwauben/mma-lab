import cv2 # this imports the OpenCV functions 

import numpy as np
# grey value image
m_grey = np.zeros((200,200))
# BGR image
im_bgr = np.ones((200,200))


im = cv2.imread('../Images/bookshelf.jpg') 
#cv2.imshow('Books image', im) 
#cv2.waitKey()

# We can convert it to grayscale by using 
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) 
#cv2.imshow('Grayscale', gray) 
#cv2.waitKey()

cv2.imshow('greyvalue', m_grey)
cv2.waitKey()

cv2.imshow('BGRimage', im_bgr)
cv2.waitKey()



