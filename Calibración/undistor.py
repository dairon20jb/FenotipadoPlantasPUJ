import numpy as np
import cv2 as cv2
import glob
import json
import random

with open('best_cam10_parameters.json') as json_data:
    paramsCam10 = json.load(json_data)
    mtx10 = paramsCam10['mtx_cam']
    new_mtx10 = paramsCam10['new_cam_mtx']
    dist10 = paramsCam10['dist']
    roi10 = paramsCam10['roi']
    json_data.close()
    
with open('best_cam11_parameters.json') as json_data:
    paramsCam11 = json.load(json_data)
    mtx11 = paramsCam11['mtx_cam']
    new_mtx11 = paramsCam11['new_cam_mtx']
    dist11 = paramsCam11['dist']
    roi11 = paramsCam11['roi']
    json_data.close()
    
with open('best_cam12_parameters.json') as json_data:
    paramsCam12 = json.load(json_data)
    mtx12 = paramsCam12['mtx_cam']
    new_mtx12 = paramsCam12['new_cam_mtx']
    dist12 = paramsCam12['dist']
    roi12 = paramsCam12['roi']
    json_data.close()
    
with open('best_cam13_parameters.json') as json_data:
    paramsCam13 = json.load(json_data)
    mtx13 = paramsCam13['mtx_cam']
    new_mtx13 = paramsCam13['new_cam_mtx']
    dist13 = paramsCam13['dist']
    roi13 = paramsCam13['roi']
    json_data.close()
    
with open('best_cam14_parameters.json') as json_data:
    paramsCam14 = json.load(json_data)
    mtx14 = paramsCam14['mtx_cam']
    new_mtx14 = paramsCam14['new_cam_mtx']
    dist14 = paramsCam14['dist']
    roi14 = paramsCam14['roi']
    json_data.close()
    
with open('best_cam15_parameters.json') as json_data:
    paramsCam15 = json.load(json_data)
    mtx15 = paramsCam15['mtx_cam']
    new_mtx15 = paramsCam15['new_cam_mtx']
    dist15 = paramsCam15['dist']
    roi15 = paramsCam15['roi']
    json_data.close()
    
with open('best_cam16_parameters.json') as json_data:
    paramsCam16 = json.load(json_data)
    mtx16 = paramsCam16['mtx_cam']
    new_mtx16 = paramsCam16['new_cam_mtx']
    dist16 = paramsCam16['dist']
    roi16 = paramsCam16['roi']
    json_data.close()


images = glob.glob('*.jpeg')


for fname in images:

    if (fname.startswith("cam10")):
        img = cv2.imread(fname)
        h,  w = img.shape[:2]
        dst = cv2.undistort(img, mtx10, dist10, None, new_mtx10)
        x,y,w,h = roi10
        dst = dst[y:y+h, x:x+w]
        cv2.imwrite(fname + 'undistr.png',dst)

    elif (fname.startswith("cam11")):
        img = cv2.imread(fname)
        h,  w = img.shape[:2]
        dst = cv2.undistort(img, mtx11, dist11, None, new_mtx11)
        x,y,w,h = roi11
        dst = dst[y:y+h, x:x+w]
        cv2.imwrite(fname + 'undistr.png',dst)

    elif (fname.startswith("cam12")):
        img = cv2.imread(fname)
        h,  w = img.shape[:2]
        dst = cv2.undistort(img, mtx12, dist12, None, new_mtx12)
        x,y,w,h = roi12
        dst = dst[y:y+h, x:x+w]
        cv2.imwrite(fname + 'undistr.png',dst)

    elif (fname.startswith("cam13")):
        img = cv2.imread(fname)
        h,  w = img.shape[:2]
        dst = cv2.undistort(img, mtx13, dist13, None, new_mtx13)
        x,y,w,h = roi13
        dst = dst[y:y+h, x:x+w]
        cv2.imwrite(fname + 'undistr.png',dst)

    elif (fname.startswith("cam14")):
        img = cv2.imread(fname)
        h,  w = img.shape[:2]
        dst = cv2.undistort(img, mtx14, dist14, None, new_mtx14)
        x,y,w,h = roi14
        dst = dst[y:y+h, x:x+w]
        cv2.imwrite(fname + 'undistr.png',dst)

    elif (fname.startswith("cam15")):
        img = cv2.imread(fname)
        h,  w = img.shape[:2]
        dst = cv2.undistort(img, mtx15, dist15, None, new_mtx15)
        x,y,w,h = roi15
        dst = dst[y:y+h, x:x+w]
        cv2.imwrite(fname + 'undistr.png',dst)

    elif (fname.startswith("cam16")):
        img = cv2.imread(fname)
        h,  w = img.shape[:2]
        dst = cv2.undistort(img, mtx16, dist16, None, new_mtx16)
        x,y,w,h = roi16
        dst = dst[y:y+h, x:x+w]
        cv2.imwrite(fname + 'undistr.png',dst)

    else:
        print('La imagen no es parte del sistema')




