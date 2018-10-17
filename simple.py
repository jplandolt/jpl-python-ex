#!/opt/app-root/bin/python3
# Simple python thing

import os
import io
import sys
import time
from time import gmtime, strftime


# main function
def main (argv=sys.argv[1:]):
    print("in function - main")

    while True:
        print("waiting - " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        time.sleep(2.0) 

    return

# end function main

# main loop
if __name__ == '__main__':
    main()

