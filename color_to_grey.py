from skimage.io import imread
from skimage.color import rgb2lab, lab2rgb
import numpy as np
import matplotlib.pyplot as plt


im=imread('sachin.jfif')
im1=rgb2lab(im)

im1[...,1]=im1[...,2]=0

im1=lab2rgb(im1)

plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.imshow(im)
plt.axis('off')
plt.title('origianl image',size=20)

plt.subplot(1,2,2)
plt.imshow(im1)
plt.axis('off')
plt.title('greyscale image',size=20)

plt.show()





