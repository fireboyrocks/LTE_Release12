#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 11:01:38 2018

@author: soubhikdeb
"""

"""
This is for Cyclic Redundancy Check
"""


# input_bitstring is of type list with elements of type int

def determine_and_padding_CRC(input_bitstring, CRC_type):
    # dictionary of all available 
    CRC_dict = {'24A':'1100001100100110011111011', '24B':'1100000000000000001100011', \
                '16':'10001000000100001', '8':'110011011'}
    
    polynomial_bitstring = CRC_dict[CRC_type]
    initial_filter = '0'
    len_input  = len(input_bitstring)
    initial_padding = [int(i) for i in list(initial_filter*(len(polynomial_bitstring) - 1))]
    input_padded_array = input_bitstring + initial_padding
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index(1)
        for i in range(len(polynomial_bitstring)):
            if int(polynomial_bitstring[i]) == input_padded_array[cur_shift + i]:
                input_padded_array[cur_shift + i] = 0
            else:
                input_padded_array[cur_shift + i] = 1
     
    CRC_attached_bitstring = input_bitstring + input_padded_array[-(len(polynomial_bitstring)-1):]         
    return CRC_attached_bitstring
                
    

    