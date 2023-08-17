#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from PIL import Image, ImageEnhance
import os
import matplotlib.pyplot as plt
import skimage.io
import skimage.color
import skimage.filters
os.chdir("D:\\RIYA\\college stuff\\3rd year\\5th sem\\EE604")


# In[2]:


img = input("Enter the cctv number image in jpg form: ")
arr = img.split('.')
print(arr)


# In[3]:


def gammaCorr(src, gamma):
    inv = 1 / gamma
    table = [((i / 255) ** inv) * 255 for i in range(256)]
    table = np.array(table, np.uint8)
    return cv2.LUT(src, table)


# In[9]:


if arr[0][4]=='1':
    img = cv2.imread('cctv1.jpg')
    gammaImg = gammaCorr(img, 2.5)

# cv2.imshow('Original image', img)
# cv2.imshow('Gamma corrected image', gammaImg)
    cv2.imwrite('enhanced-cctv1.jpg',gammaImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif arr[0][4]=='2':
    img = cv2.imread('cctv2.jpg')
    gammaImg = gammaCorr(img, 2.0)

# cv2.imshow('Original image', img)
# cv2.imshow('Gamma corrected image', gammaImg)
    cv2.imwrite('enhanced-cctv2.jpg',gammaImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif arr[0][4]=='3':
    file = "cctv3.jpg"
    img = Image.open(file)
    # img.show()
    im_out = ImageEnhance.Brightness(img).enhance(8.0)
    im_out = ImageEnhance.Contrast(im_out).enhance(1.5)
    im_out = ImageEnhance.Sharpness(im_out).enhance(4.0)
    # im_out.show()
    im_out.save('D:\\RIYA\\college stuff\\3rd year\\5th sem\\EE604\\enhanced-cctv3.jpg')  
elif arr[0][4]=='4':
    cctv4 = cv2.imread(img)
    gray_img=cv2.cvtColor(cctv4,cv2.COLOR_BGR2GRAY)
    eqhist=cv2.equalizeHist(gray_img)
    cv2.imwrite('enhanced-cctv4.jpg ', eqhist)
    cv2.waitKey(0)
    


# In[ ]:



    


# In[5]:





# In[105]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




