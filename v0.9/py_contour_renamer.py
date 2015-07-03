# @name  py_contour_renamer.py
# @author  Steve Broskey

#import
import os
from datetime import datetime

# #LOGGING
#open log file
logFile = 'log.txt'
f = open(logFile, 'a+')
f.write('Logging started '+str(datetime.now())+'\n')

#constants
fPrefix = 'FILE'
fExt = '.MOV'

#get into correct directory
fromDir = os.getcwd()
filesList = os.listdir(fromDir)

#get last used number
oldFilesList = os.listdir(fromDir+'/..')
lastOldFname = oldFilesList[len(oldFilesList)-1]
#DEBUG
f.write('lastOldFname = '+str(lastOldFname)+'\n')
lastOldIndex = int(lastOldFname[4:8])

counter = 0
#for all files in correct directory
for fileNum in range(len(filesList)):
  #is this a movie file?
  if filesList[fileNum].startswith(fPrefix):
    counter += 1
    #DEBUG
    f.write('filesList[fileNum] = '+str(filesList[fileNum]))
    #rename [this] file lastusednumber + index +1
    os.rename(filesList[fileNum], fPrefix+  \
              str(lastOldIndex + counter).zfill(4)+fExt)
    #DEBUG
    f.write(' ... converted to '+fPrefix+  \
            str(lastOldIndex + counter).zfill(4)+fExt+'\n')
#endfor

#DEBUG
f.write('Exiting at the end ... '+str(datetime.now())+'\n')
#Close logging file
f.close()
