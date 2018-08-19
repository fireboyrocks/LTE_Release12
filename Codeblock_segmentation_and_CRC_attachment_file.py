#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:23:47 2018

@author: soubhikdeb
"""

"""
This is for code block segmentation and code block CRC attachment
Return the blocks of code in the form of strings in a list of all code blocks
"""
import math
import csv
from CRC_file import determine_and_padding_CRC
import pdb
pdb.set_trace()

def Codeblock_segmentation_and_CRC_attachment(CRC_attached_Transport_Block):
    max_codeblock_size = 6144
    min_codeblock_size = 40
    B = len(CRC_attached_Transport_Block)
 
    
    
    # comparing with minimum codeblock size
    if B < min_codeblock_size:
        num_filler_bits = min_codeblock_size - B
        CRC_attached_Transport_Block = [0 for i in range(num_filler_bits)] + CRC_attached_Transport_Block
        B = min_codeblock_size
        
 
    
    
    
    # determining the number of codeblocks
    if B <= max_codeblock_size:
        L = 0   # additional CRC bits to be attached at each codeblock
        C = 1
        B1 = B  # total number of bits after addition of CRC at each codeblocks
    else:
        L = 24  # note that CRC24B is always in the CRC attachment 
        C = math.ceil(B//(max_codeblock_size - L))
        B1 = B + C*L


   
    
    
    
    
    # determining number of bits in each block   
    with open('Codeblock_size.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            list_of_segmentation_size = [int(i) for i in row[1:]]
            
    for k in list_of_segmentation_size:
        if (C*k >= B1):
            K_plus = k  # first segmentaton size
            break
    if C == 1:
        C_plus = 1
        C_minus= 0
        K_minus = 0
    else:
        for i in range(len(list_of_segmentation_size)):
            if list_of_segmentation_size[i] < K_plus:
                K_minus = list_of_segmentation_size[i-1]
        delta_K = K_plus - K_minus
        C_minus = math.floor((C*K_plus - B1)//delta_K)         
        C_plus = C - C_minus 
  
 
    
    
    
    
    # partitioning the input transport block into smaller codeblocks
    F = C_plus*K_plus+ C_minus*K_minus - B1 #number of filler bits
    
    # Put the codeblocks in list of list
    codeblocks_list = []
    for i in range(C):
        codeblocks_list.append([])
    
    # insertion of filler bits in the first blcok only
    for k in range(F):
        codeblocks_list[0] = codeblocks_list[0] + [0]
    k = F  # this value for inserting the bits from 
    s = 0  # to keep tab on the bit taken from the Transport Block
    CRC_type = '24B'
    
    for r in range(C):
        if r < C_minus:
            K_r = K_minus
        else:
            K_r = K_plus      
        while k < (K_r - L):
            codeblocks_list[r] = codeblocks_list[r] + [CRC_attached_Transport_Block[s]]
            k = k+1
            s = s+1
            
        if C > 1:
            codeblocks_list[r] = determine_and_padding_CRC(codeblocks_list[r],CRC_type)
        k = 0    
      
     
    return codeblocks_list    
            
            
    
        
        