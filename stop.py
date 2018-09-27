# Usage in script:
# from stop import stop
# a = 1
# stop()
# c = 1 # Not executed

import sys
import inspect

def stop():
    # Based on https://stackoverflow.com/a/39007009

    # Reset so get full traceback next time you run the script and a "real" exception occurs
    if hasattr(sys, 'tracebacklimit'):
        del sys.tracebacklimit

    # Raise this class for "soft halt" with minimum traceback.
    class Stop(Exception):
        sys.tracebacklimit = 0
        def __init__(self,value):
            self.value = value
        def __str__(self):
            return self.value

    frame,filename,line_number,function_name,lines,index = inspect.stack()[1]
    raise Stop("\b\b\b\b\b\b\b\b\b\b\bstop() on line %d of %s" % (line_number,filename))

