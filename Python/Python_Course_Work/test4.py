import os, time
import datetime
from stat import * # ST_SIZE etc


st=os.stat('C:\\Users\\wise_\\Desktop\\Folder A\\1.txt')
ctime=st.st_ctime
mtime=(time.time() - ctime)/3600
if mtime>24:
    print (mtime)
else:
    print ("Too old")
    




    

