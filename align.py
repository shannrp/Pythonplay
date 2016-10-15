#! /usr/local/bin/python3

print ("Paste Sequence 1, hit enter once, Paste Sequence 2, hit enter once, then Ctrl-D")
import sys
entry = sys.stdin.readlines()
roughDNAseq1 = entry[0]
roughDNAseq2 = entry[1]
DNAseq1 = ''.join(roughDNAseq1)
DNAseq2 = ''.join(roughDNAseq2)
NWS1 = DNAseq1.replace(" ", "").replace("\t", "").replace("\r", "").replace("\n", "").replace("\v", "")
NWS2 = DNAseq2.replace(" ", "").replace("\t", "").replace("\r", "").replace("\n", "").replace("\v", "")
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