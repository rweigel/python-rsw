# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 18:33:59 2017

@author: robertweigel
"""
import traceback
import sys

def run(fname):
    file = open(fname, 'r')
    try:
        script = file.read()
        script = script.split("stop")[0]
        file.close()
        exec(script)
    except:
        # we want to format the exception as if no frame was on top.
        exp, val, tb = sys.exc_info()
        listing = traceback.format_exception(exp, val, tb)
        # remove the entry for the first frame
        #print listing
        del listing[1]
        files = [line for line in listing if line.startswith("  File")]
        if len(files) == 1:
            # only one file, remove the header.
            del listing[0]
        print '\x1b[31m' + listing[0].split(",")[1].strip() + ": " + listing[1] + '\x1b[0m'
            #print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')