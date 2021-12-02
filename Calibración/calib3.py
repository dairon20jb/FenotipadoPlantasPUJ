#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:38:57 2019
@author: francisco
"""

import numpy as np
import cv2 as cv2
import glob
import json
import random

DIMX=9
DIMY=6
square_size=20

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)


path = glob.glob('*.jpeg')
error_min = 1
parameters_min = {'mtx_cam':[],'new_cam_mtx':[],'dist':[]}
errores = []
for j in range(1,300):
    objp = np.zeros((DIMY*DIMX,3), np.float32)
    objp[:,:2] = np.mgrid[0:DIMX,0:DIMY].T.reshape(-1,2)
    objp *= square_size
    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    images = []
    random.shuffle(path)
    for x in range(1,10,1):
        images.append(path[x]) 

    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (DIMX,DIMY),None)

        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)

            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            imgpoints.append(corners2)

            # Draw and display the corners
            img = cv2.drawChessboardCorners(img, (DIMX,DIMY), corners2,ret)
            #cv2.imshow('img',img)
            #cv2.waitKey(1)

    #cv2.destroyAllWindows()
    #cv2.waitKey(1)
    #print(imgpoints)


    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

    #print(mtx)
    #print(type(mtx))
    #print(dist)
    #print(type(dist))
    # termina la calibración


    

    # Inicia etapa de usuario

    img = cv2.imread('cam16.10.jpeg')
    h,  w = img.shape[:2]
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),0,(w,h))
    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

    # crop the image
    x,y,w,h = roi
    dst1 = dst[y:y+h, x:x+w]
    

    mean_error = 0
    for i in range(len(objpoints)):
        imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
        error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
        mean_error += error

    #print ("matriz inversa ")
    mtx_inv=np.linalg.inv(mtx)


    error_total = mean_error/len(objpoints)
    print ("total error: ", mean_error/len(objpoints))
    
    #print ("matriz inversa ")
    mtx_inv=np.linalg.inv(mtx)
    
    errores.append(error_total) 

    if (error_total < error_min):
        error_min = error_total
        parameters_min['mtx_cam'] = mtx.tolist()
        parameters_min['new_cam_mtx'] = newcameramtx.tolist()
        parameters_min['dist'] = dist.tolist()
        parameters_min['roi'] = roi
        cv2.imwrite('calibresult1.png',dst1)
    print(j) 

print(error_min)
with open('best_cam_parameters.json','w') as json_file:
    json.dump(parameters_min,json_file)

with open('errors_vect.json','w') as json_file:
    json.dump(errores,json_file)