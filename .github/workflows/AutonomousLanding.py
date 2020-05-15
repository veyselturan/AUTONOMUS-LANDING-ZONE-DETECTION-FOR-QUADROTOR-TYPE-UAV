# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 05:05:57 2020

@author: Veysel Turan
"""

import numpy as np
import cv2
from random import choice
import random
import sys
import os



while(True):
        #To clear all saved values in memory before running
        def clear():
            os.system('cls')
            return None
        
        cls=clear
        
        def clear_all():
            cls()
            gl = globals().copy()
            for var in gl:
                if var[0] == '_': continue
                if 'func' in str(globals()[var]): continue
                if 'module' in str(globals()[var]): continue
                
                del globals()[var]

        clear_all() 

        
        size = 400,600,3
        img1 = cv2.imread('trial1.jpg')
        img1 = cv2.resize(img1, (600,400))
        img2 = np.zeros(size,np.uint8)

        
        
        gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray1,(7,7),0)
        gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        edge = cv2.Canny(blur,100,200)
        ret,th2 = cv2.threshold(gray2, 127, 255,cv2.THRESH_OTSU)
        #cv2.imshow('Canny',edge)
        
        
        
        
        color =(255,0,0) #red color for landing area zone
        h1 = 50
        w1 = 50
        
        #to make a choice in the image between pixels
        sequence1 = [xi for xi in range(50,550)]    
        sequence2 = [yi for yi in range(50,350)]       
        a = random.choice(sequence1)
        b = random.choice(sequence2)
        
    
    
    
        #to create  landing area on non-real image
        c = cv2.rectangle(th2, (a,b), (a+h1,b+w1), (255,255,255), -1)
        el = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        dilate_image1 = cv2.dilate(edge,el,iterations=9)
        d = cv2.dilate(c, el, iterations=7)
        result = cv2.bitwise_and(dilate_image1, d)
        #cv2.imshow('result',result)
        #cv2.imshow('imaginary',c)
        
        
        contours, hierarchy = cv2.findContours(result,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        centers = []
    
    
    
        #To calculate how many pixels overlap between two image
        for contour in contours:
            m = cv2.moments(contour)
            try:
                center = (int(m['m10'] / m['m00']), int(m['m01'] / m['m00']))
                centers.append(center)
                
            except ZeroDivisionError:
                m=0
    
    
  
        print("There are {} circles".format(len(centers)))
        print(len(centers))
        
        
        #if the are is available for landing then show image and landing area
        if len(centers) == 0:
            print("Alan uygun")
            cv2.rectangle(img1,(a,b),(a+h1,b+w1),(0,0,255),-1)
            cv2.imshow('Sonuc',img1)
            
            break
        
        
         #if selected area is NOT avaliable for landing then go back the loop and run again  
        else:
            print("Alan uygun değil")
            continue
    

cv2.waitKey(0)
cv2.destroyAllWindows()



