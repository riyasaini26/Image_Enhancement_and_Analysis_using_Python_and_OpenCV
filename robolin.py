#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Python program to illustrate HoughLine
# method for line detection
import cv2
import numpy as np
import os
os.chdir("D:\\RIYA\\college stuff\\3rd year\\5th sem\\EE604")


# In[12]:


img = input('Enter the tile number for which lines to be detected: ')
arr = img.split('.')
print(arr)


# In[13]:


if arr[0]=='tiles1':
    #tile1
    img = cv2.imread('tiles1.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    t_lower = 50  # Lower Threshold
    t_upper = 150  # Upper threshold
    # Applying the Canny Edge filter
    edge = cv2.Canny(gray, t_lower, t_upper,apertureSize=3)
    cv2.imshow('edge', edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    line = cv2.HoughLines(edge,1,np.pi/180,200)
    for l in line:
        r,theta = l[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*r
        y0 = b*r
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
#     cv2.imshow('image',img)
    cv2.imwrite('robolin-tiles1.jpg', img)
    cv2.waitKey(0)
elif arr[0]=='tiles2':
    #tile2
    img = cv2.imread('tiles2.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    Gaussian = cv2.GaussianBlur(gray, (5,5), 0)
    
    t_lower = 50  # Lower Threshold
    t_upper = 150  # Upper threshold
  
    # Applying the Canny Edge filter
    edge = cv2.Canny(Gaussian, t_lower, t_upper,apertureSize=3)
    exp = cv2.dilate(edge, np.ones((3,3), np.uint8))
    cv2.imshow('edge', exp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    line = cv2.HoughLines(edge,1,np.pi/180,150)
    for l in line:
        r,theta = l[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*r
        y0 = b*r
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
#     cv2.imshow('image',img)
    cv2.imwrite('robolin-tiles2.jpg', img)
    cv2.waitKey(0)
elif arr[0]=='tiles5.jpg':
    img = cv2.imread('tiles5.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    Gaussian = cv2.GaussianBlur(gray, (3,3), 0)
    t_lower = 50  # Lower Threshold
    t_upper = 150  # Upper threshold
  
        # Applying the Canny Edge filter
    edge = cv2.Canny(Gaussian, t_lower, t_upper,apertureSize=3)
    exp = cv2.dilate(edge, np.ones((3,3), np.uint8))
    cv2.imshow('edge', exp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    line = cv2.HoughLinesP(exp,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
    for l in line:
        x1,y1,x2,y2 = l[0]
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.imshow('image',img)
    cv2.imwrite('robolin-tiles5.jpg', img)
    cv2.waitKey(0)
elif arr[0]=='tiles8':
    img = cv2.imread('tiles8.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    t_lower = 50  # Lower Threshold
    t_upper = 150  # Upper threshold
  
    # Applying the Canny Edge filter
    edge = cv2.Canny(gray, t_lower, t_upper,apertureSize=3)
    cv2.imshow('edge', edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    exp = cv2.dilate(edge, np.ones((5,5), np.uint8))
    line = cv2.HoughLines(exp,1,np.pi/180,300)
    for l in line:
        r,theta = l[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*r
        y0 = b*r
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.imshow('image',img)
    cv2.imwrite('robolin-tiles8.jpg', img)
    cv2.waitKey(0)
elif arr[0]=='tiles11':
    img = cv2.imread('tiles11.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    Gaussian = cv2.GaussianBlur(gray, (3,3), 0)
    t_lower = 50  # Lower Threshold
    t_upper = 150  # Upper threshold
  
    # Applying the Canny Edge filter
    edge = cv2.Canny(Gaussian, t_lower, t_upper,apertureSize=3)
    exp = cv2.dilate(edge, np.ones((3,3), np.uint8))
    cv2.imshow('edge', exp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    line = cv2.HoughLinesP(exp,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
    for l in line:
        x1,y1,x2,y2 = l[0]
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.imshow('image',img)
    cv2.imwrite('robolin-tiles11.jpg', img)
    cv2.waitKey(0)
    

    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




