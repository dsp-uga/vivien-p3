#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:06:56 2021

@author: kadir
"""

import cv2
import numpy as np
import sys, os
import tarfile     
from matplotlib import pyplot as plt
import operator

# input arguments
text_dir = sys.argv[1] # 
data_dir = sys.argv[2] # 
mask_dir = sys.argv[3] # 
prediction_dir = sys.argv[4] # 

# load hashes
train_files = open(text_dir).read().split()
             
# extract images from tar files                                                            
def get_np_array_from_tar_object(tar_extractfl):
     '''converts a buffer from a tar file in np.array'''
     return np.asarray(
        bytearray(tar_extractfl.read())
        , dtype=np.uint8)

# average score of the method
total_score = []
count = 0
# loop over hashes
for hash_name in train_files:
    count = count + 1
    print(count)
    
    # open tar file with the certain hash name
    tar0 = tarfile.open(data_dir + hash_name + '.tar')
    
    # store all images in a list
    imgs = []
    names = tar0.getnames()
    names.sort()
    for i in range(0,100):
        img_read = cv2.imdecode(get_np_array_from_tar_object(tar0.extractfile(names[i])), 0)
        # img_read = cv2.medianBlur(img_read,5)
        imgs.append(img_read.astype(np.float))
    
    # number of images (100)        
    num_imgs = len(imgs)
    
    # calculate mean of each pixel across images
    mean = sum(imgs)/(num_imgs)
    
    # sizes of images
    nrow, ncol = imgs[1].shape

    # calculate variance
    var = np.zeros((nrow,ncol))
    for i in imgs:
        var = var + (i - mean)**2/(num_imgs)
        
    # convert variance to uint8 (values 0-255)
    var = var.astype(np.uint8) 
        
    # load mask for certain hash name
    mask = cv2.imread(mask_dir + hash_name + '.png', 0) 
    
    # apply median filter
    # mask = cv2.medianBlur(mask, 5)
    
    # get only cilia pixels 
    mask_test = (mask == 2)
    
    # initialize lists to store accuracy metrics
    cilia = []
    overall = []
    
    # test different threshold values for variance
    rng = range(0,50)
    
    # testing threshold values
    for threshold in rng:  
        # get pixels that expected to be moving with certain threshold
        var_test = var >= threshold
        
        # plotting variance images
        #plt.imshow(var_test, cmap = 'gray')
        #plt.xticks([]), plt.yticks([])
        #plt.show()
        
        # calculate accuracy according to IoU (eliminating overflow errors with if()) 
        if(np.sum(var_test + mask_test) > 0):
            overall_acc = round(np.sum(var_test*mask_test)/np.sum(var_test + mask_test), 3)
        else:
            overall_acc = 0
        
        # append accuracy score to list    
        overall.append(overall_acc)
        
        # print('overall accuracy with threshold =' + str(threshold) + ' ==> ' + str(overall_acc))
    
    # plot threshold vs accuracy
    # plt.plot(rng, cilia, 'r', rng, overall, 'b')
    # plt.show()
    
    # get maximum accuracy and related threshold value
    max_index, max_value = max(enumerate(overall), key=operator.itemgetter(1))
    print('overall accuracy with threshold =' + str(rng[max_index]) + ' ==> ' + str(max_value))
    
    # append best score for certain hash 
    total_score.append(max_value)
    
    # just to get 2's for cilia pixels (did not care about the rest of the pixels)
    var_est = (var >= rng[max_index]) + 1
    # export the prediction image
    cv2.imwrite(prediction_dir + hash_name + '.png', var_est)
    
print('AVG SCORE = ' + str(round(np.mean(total_score),3)))
    
    
        


