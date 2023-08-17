#!/usr/bin/env python
# coding: utf-8

# In[32]:


import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import skimage.io
import skimage.color
import skimage.filters
os.chdir('D:\\RIYA\\college stuff\\3rd year\\5th sem\\EE604')


# In[33]:


img = cv2.imread('gutters1.jpg')


# In[34]:


gray_image = skimage.color.rgb2gray(img)
fig,ax = plt.subplots()
plt.imshow(gray_image,cmap='gray')


# In[35]:


# create a histogram of the blurred grayscale image
histogram, bin_edges = np.histogram(gray_image, bins=256, range=(0.0, 1.0))

fig, ax = plt.subplots()
plt.plot(bin_edges[0:-1], histogram)
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim(0, 1.0)


# In[36]:


image_array = np.array(img)
print(image_array.shape)


# In[40]:


split_img = cv2.split(gray_image)

final_img = []
for plane in split_img:
    exp = cv2.dilate(plane, np.ones((5,5), np.uint8)) #to expand the image( convolving an image with kernel)
    dst = cv2.GaussianBlur(exp,(3,3),0) #applying gaussian filter to reduce noise and blur the image
    shad = 255 - cv2.absdiff(plane, dst) #to remove the shadow
    norm = cv2.normalize(shad, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    final_img.append(norm) #to add rgb plane in an array

result = cv2.merge(final_img) #merge all plane to form multicolor image
final = skimage.color.gray2rgb(result)
cv2.imwrite('cleaned-gutter.jpg', final)


# In[ ]:





# In[ ]:




