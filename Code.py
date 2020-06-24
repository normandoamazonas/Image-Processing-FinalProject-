



import numpy as np
import matplotlib.pyplot as plt
import imageio as imageio
import math

'''Functions definitions'''

kernel1= [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
kernel2= [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

kernels = [kernel1,kernel2]
def crop(im):
   w,h=im.shape
   return im[1:w-1, 1:h-1]
def padding(im):
   w,h=im.shape
   im2= np.zeros ((w+2,h+2),np.float32)
   im2[1:w+1, 1:h+1] = im  
   return im2

def conv2d(image,kernel):
    temp=padding(image)
    w,h=temp.shape
    wk,hk=kernel.shape    
    result= np.zeros ((w,h),np.float32)
    mk=int((wk-1)/2)
    for i in range(mk,h-mk):
      for j in range(mk,h-mk):
           reg=temp[i-mk:i+mk+1,j-mk:j+mk+1]
           result[i,j]=np.sum(reg*kernel)

    return crop(result).astype(np.uint8)

    def kernelgs (n, sigma): 
    k= np.zeros ((n,n),np.float64)
    #k= [[0]*n]*n
    cx =int (n/2)
    cy= int (n/2)
    
    for i in range (n):  #o..n-1
        for j in range (n):
           #print (i,j,E (cx-j, cy-i))
           k [i,j]= G (E (cx-j, cy-i), sigma)
           #print (k[i,j])

    return k

def kernelgr (I, n, sigma): 
    k= np.zeros ((n,n),np.float64)
    #k= [[0]*n]*n
    cx =int (n/2)
    cy= int (n/2)
   
    for i in range (n):
        for j in range (n):
           k [i,j]= G ( I[cx, cy]- I[j, i], sigma)

    return k
