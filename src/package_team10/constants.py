
#!/usr/bin/python3

import os

"""constants and global functions (have to be defined\
    by the user at the beginning; used filedir and \
        filenames are examples)"""
threshv = 1.0e-5      # has to be defined by the user
filedir = '/home/anja/team10/team10/data/'     # has to be defined by the user
filenames = [f for f in os.listdir(filedir) \
    if os.path.isfile(os.path.join(filedir, f))]
