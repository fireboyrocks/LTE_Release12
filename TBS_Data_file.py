"""

"""


import csv 
#import pdb
#import numpy as np

#pdb.set_trace()

def PDSCH_TBS_Function(tbs_data):
    
    """
    This function is for reading the csv files containing the table on Transport Block size and
    Modulation Indices from TS 36.213
    """
    
    with open('TBS_Table.csv', 'r') as f:
        reader = csv.reader(f)
        cnt = 0;
        for row in reader:
            if cnt == 0:
                arr = [row]
            else:
                arr = arr + [row]
            cnt += 1
            
    
    TBS = {}
    
    
    
    for cnt in range(0,cnt):
        if cnt == 0:
            PRB_ID = arr[cnt][1:]
        elif cnt in range(1,29):
            for j in range(0,len(PRB_ID)):
                TBS[(arr[cnt][0],PRB_ID[j])] = arr[cnt][j+1]
    
        
    
    
    
    with open('Modulation_Table.csv', 'r') as f:
        reader = csv.reader(f)
        cnt = 0;
        for row in reader:
            if cnt == 0:
                arr1 = [row]
            else:
                arr1 = arr1 + [row]
            cnt += 1
            
    MCS_Index = []
    Modulation_Order = []
    TBS_Index = []
    
    for cnt in range(0,cnt):
        MCS_Index.append(arr1[cnt][0])
        Modulation_Order.append(arr1[cnt][1])
        TBS_Index.append(arr1[cnt][3])
    
    MCS_Index[0] = '0' 
    
    tbs_data.MCS_Index = MCS_Index
    tbs_data.Modulation_Order = Modulation_Order
    tbs_data.TBS_Index = TBS_Index
    tbs_data.TBS = TBS
    
    return tbs_data
               
         