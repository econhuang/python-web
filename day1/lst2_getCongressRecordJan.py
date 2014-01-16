import os
import time

#Download "Entire Issue" of the Congressional Record for the period January 1- 31 2014"""

month = 1

for day in range(1,10):
    fileURL="http://beta.congress.gov/crec/2014/%02d/%02d/CREC-2014-%02d-%02d.pdf" \
                                                        % (month,day,month,day)
    print("Downloading file %s." % fileURL)

    #construct the wget command string  
    cmdStr = "wget %s" % fileURL

    #execute the command
    os.system(cmdStr) 

    time.sleep(2)