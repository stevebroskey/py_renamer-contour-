# @name  py_contour_renamer.py
# @author  Steve Broskey
#
# @description Renames contour video files so they can be copied up one directory layer for keeping in a larger "footage" folder, making the new name FILE####.MOV where #### is a four digit integer one greater than the highest numbered file in the parent folder.

#import
import os
from datetime import datetime

### #LOGGING
# Using Logging
#Import logging libraries
import logging
import logging.handlers

#open log file
logFile = 'log.txt'
f = open(logFile, 'a+')
f.write('----- Logging started '+str(datetime.now())+'\n')

#designate a logfile
Log_filename = os.getcwd()+'/logfile.log'

#set up a specific logger with desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

#Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
  Log_filename, maxBytes=100, backupCount=9)

my_logger.addHandler(handler)

#constants
fPrefix = 'FILE'
fExt = '.MOV'
tempIndicator = 'TEMP'

#get into correct directory
fromDir = os.getcwd()
filesList = os.listdir(fromDir)

#get last used number
oldFilesList = os.listdir(fromDir+'/..')
#DEBUG
f.write('oldFilesList = '+str(oldFilesList)+'\n')

if oldFilesList: #test oldFilesList isn't empty
  lastOldFname = oldFilesList[len(oldFilesList)-1]
  if lastOldFname.startswith(fPrefix): #test lastOldFname starts with pfix
    #DEBUG
    ##f.write('lastOldFname = '+str(lastOldFname)+'\n')
    my_logger.debug('lastOldFname = '+str(lastOldFname)+'\n')
    lastOldIndex = int(lastOldFname[4:8])
  else:
    my_logger.debug('Wrong last file name, exit!ing...')
##    return #This return might require a zero
else: #directory is empty, exit
  my_logger.debug('Parent directory empty')
##  return #This return might require a zero

#--Do Renaming-- (assign to temp filename)
    #I should be able to nest these renames into one for loop done twice (1=temp 2=done)
counter = 0
#DEBUG
f.write('counter = '+str(counter)+'\n')

#for all files in correct directory
for fileNum in range(len(filesList)):
  #is this a movie file?
  if filesList[fileNum].startswith(fPrefix):
    counter += 1
    #DEBUG
    f.write('filesList[fileNum] = '+str(filesList[fileNum]))
    #rename [this] file lastusednumber + index +1
    newFilename = fPrefix+ str(lastOldIndex + counter).zfill(4)+fExt+tempIndicator
    os.rename(filesList[fileNum], newFilename) #Bug: when
                      #fixing an accidental rename, if the file already
                      #exists, the rename can't happen. Fix: use temp files.
    #DEBUG
    f.write(' ... converted to '+newFilename+'\n')
    filesList[fileNum]=newFilename
#endfor
#--End Renaming-- (assigned to tmp file)

#--Do Renaming--
counter = 0
#DEBUG
f.write('counter = '+str(counter)+'\n')

#for all files in correct directory
for fileNum in range(len(filesList)):
  #is this a movie file?
  if filesList[fileNum].startswith(fPrefix):
    counter += 1
    #DEBUG
    f.write('filesList[fileNum] = '+str(filesList[fileNum]))
    #rename [this] file lastusednumber + index +1
    newFilename = fPrefix+ str(lastOldIndex + counter).zfill(4)+fExt
    os.rename(filesList[fileNum], newFilename) #Bug: when
                      #fixing an accidental rename, if the file already
                      #exists, the rename can't happen. Fix: use temp files. (above)
    #DEBUG
    f.write(' ... converted to '+newFilename+'\n')
#endfor
#--End Renaming--

#DEBUG
f.write('Exiting at the end ... '+str(datetime.now())+' -----\n')
#Close logging file
f.close()
