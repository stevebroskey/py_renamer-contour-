#py_renamer.py

#import
import os
#import re

#constants
Fprefix = 'FILE'
Fextension = '.MOVe'

#get into correct directory
fromDir = os.getcwd()
filesList = os.listdir(fromDir)

#get last used number
oldFilesList = os.listdir(fromDir+'/..')
lastOldFname = oldFilesList[len(oldFilesList)-1]
  #//forgetit//break filename into FILE / number / extension

lastOldIndex = int(lastOldFname[4:8])

#for all files in correct directory
for fileNum in range(len(filesList)):
  #rename [this] file lastusednumber + index +1
  os.rename(filesList[filenum], Fprefix+str(lastOldIndex + filenum + 1)+Fextension)
#endfor

