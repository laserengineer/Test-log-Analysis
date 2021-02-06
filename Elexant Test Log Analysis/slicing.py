import re

line = '2/3/2021_1:09:40 PM : TS1 verification passed.  Expected = 116.20 ohms, actual reading= 116.01 ohms.  (Pass range: 115.50 ohms to 116.90 ohms)'
keys = ['TS1','verification']

#if(x in line for x in keys[:]):
if( x in keys[:] for x in line):
    print("found")
else:
    print("Not Found")

