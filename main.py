import csv
def get_filelist():
    """
    read the file name to be processed from the command line.
    """
    import sys
    import os
    rootdir=str(os.getcwd())
    if ( len (sys.argv) == 1 ):
        sys.exit("Please input file name")
    else:
        return(sys.argv[-1])




filename = get_filelist()
print(filename)
