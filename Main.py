# -*- coding: utf-8 -*-
"""
The main file
"""

from TBS_Data_file import PDSCH_TBS_Function
from Bit_generation_file import Bit_generation
from CRC_file import determine_and_padding_CRC
from Codeblock_segmentation_and_CRC_attachment_file import Codeblock_segmentation_and_CRC_attachment

class TBS_DATA:
    """
    This class contains the data/look-up table required for calculating the TBS
    """
    def _init_(self,MCS_Index,Modulation_Order,TBS_Index,TBS):
        self.MCS_Index = MCS_Index
        self.Modulation_Order = Modulation_Order
        self.TBS_Index = TBS_Index
        self.TBS = TBS
        

tbs_data  = TBS_DATA()
tbs_data = PDSCH_TBS_Function(tbs_data) 

  

"""
In LTE, there are 6 options for number of RBs
"""
PRB_list = {'Case 1':'6', 'Case 2':'15', 'Case 3':'25', 'Case 4':'50', 'Case 5':'75', 'Case 6':'100'}
FFT_size = 2048
Subcarriers_per_RB = 12


"""
Input
"""
case = 'Case 5' # for determining number of PRBs
PRB = PRB_list[case] 
I_MCS = '26'  # for determining MCS Index
CRC_Type = '24A'

Q_m = tbs_data.Modulation_Order[int(I_MCS)] # Modulation Order
I_TBS = tbs_data.TBS_Index[int(I_MCS)]  # TBS Index
TBS_Table_elem_ID = (I_TBS,PRB)
tbs = tbs_data.TBS[TBS_Table_elem_ID] # transport block size


Transport_Block = Bit_generation(int(tbs))
CRC_attached_Transport_Block = determine_and_padding_CRC(Transport_Block,CRC_Type)

Segmented_Codeblock = Codeblock_segmentation_and_CRC_attachment(CRC_attached_Transport_Block)