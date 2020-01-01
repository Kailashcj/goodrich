#!/bin/python3

import os
import sys
from datetime import datetime

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    infmt = s if s[-3] == " " else s[:-2]+" "+s[-2:]
    if infmt[-2:] == "AM":
        if infmt[:2] == "12":
            infmt = "00"+infmt[2:]
            print('*******let print***:', infmt)
            intime = datetime.strptime(infmt, "%H:%M:%S")
            print('1st intime:', intime)
        intime = datetime.strptime(infmt, "%I:%M:%S %a")
        print('2nd intime:', intime)
    else:
        intime = datetime.strptime(infmt, "%I:%M:%S %p")
    return datetime.strftime(intime, "%H:%M:%S")
    

if __name__ == '__main__':
   # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    #f.write(result + '\n')

    #f.close()

