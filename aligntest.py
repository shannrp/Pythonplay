#! /usr/local/bin/python3

NWS1 = 'GATTACA'
NWS2 = 'GAATTAA'
DNAlist1 = list(NWS1)
DNAlist2 = list(NWS2)
DNAlist2.insert(0, 0)
import numpy as np
from numpy import newaxis
axis1 = np.array((DNAlist1))
axis2 = np.array((DNAlist2))
holder = np.zeros((len(DNAlist1),len(DNAlist2)-1))
holder2 = np.vstack((axis1,holder))
alignmat = np.hstack((axis2[:,newaxis],holder2))
print (alignmat)