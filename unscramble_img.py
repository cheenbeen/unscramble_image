#!/usr/bin/env python
# coding: utf-8

# In[15]:


#Import all necessary modules
from PIL import Image
import numpy as np
import random


# In[16]:


#Read image: downloaded from source
filename = 'scrambled.jpg'
img = Image.open(filename)

#Display information about file
print('Image dimensions: ', img.size)
print('Total number of pixels, ', img.size[0]*img.size[1])

#Transform 2D array of pixels to 1D array 
img_1d = np.asarray(img).flatten()


# In[21]:


#Read the text file containing shuffled index list
f = open('shuffle_indecies.txt', 'r')
file_content = f.read().split('\n')

#Convert the string to integer values and store in dict
#key, value: index, pixel values
l = {}
iterator = 0
for element in file_content:
    l[int(element)] = img_1d[iterator]
    iterator+=1
#Sort the dictionary values with keys and store pixel values in list
pix_vals = []
for element in sorted(l):
    pix_vals.append(l[element])
    
#convert to ndarray
pix_vals = np.asarray(pix_vals)
pix_vals


# In[24]:


#Reshape to 2D and store unscrambled image
pix_vals = pix_vals.reshape(480, 592)
unscrambled_img = Image.fromarray(pix_vals)
unscrambled_img.show()
#Save image
unscrambled_img.save('unscrambled.jpg')


# In[ ]:




