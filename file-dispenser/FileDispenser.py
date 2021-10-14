# we will check all the files then if we got a folder inside in that we will again go into that and check for all the files
import os
from datetime import datetime, timedelta

# threshold = what will be your specific time before that you are going to delete your files
# base=True --> here baselocation means the parent dir if it got deleted how will you add files in it
def file_dispenser(path, thresh, base=True):
    # checking the path you gave me is folder or file
    if os.path.isdir(path):                     # os.listdir(path) will give files form this if it a folder
        for internal in os.listdir(path):       # will apply loop to run file dispenser
            file_dispenser(path + "/" + internal,
                           thresh, False)             # we don't know file name which we have to delete file name so we will make a file name (path + "/" + internal)
        if (not base) and (len(os.listdir(path)) == 0):
            os.rmdir(path)
        return

    mod = os.path.getmtime(path)
    if mod < thresh:
        print("This is Old file")
        os.remove(path)
    else:
        print("This is New file")


# this is a millisecond version of 1 min. before current time
threshold = (datetime.now() - timedelta(minutes=1)).timestamp()
# print(threshold)
file_dispenser("fol1", threshold)
