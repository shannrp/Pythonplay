#! /usr/local/bin/python3

print ("Paste Sequence, hit enter once, then Ctrl-D")
import sys
roughDNA = sys.stdin.readlines()
DNA = ''.join(roughDNA)
NWS = DNA.replace(" ", "").replace("\t", "").replace("\r", "").replace("\n", "").replace("\v", "")
DNA1 = NWS.replace('A', 'X').replace('T', 'A').replace('X', 'T').replace('G', 'Y').replace('C', 'G').replace('Y', 'C')
print ("  ")
print ("Reverse Complement: \n")
print (DNA1[::-1])

