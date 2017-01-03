#!/usr/bin/env python
"""processor main program

@status:  experimental
@version: $Revision$
@author:  Chi Zhang
"""

from __future__ import print_function
import sys
import argparse
import random
import bisect
import logging

RELEASE = True

if RELEASE:
    # for release version of processor
    from processor import *
    from processor.crisprFunction import *
    from processor.processorCount import *
    from processor.pathwayFunc import *
    from processor.argsParser import *
    from processor.testVisual import *
else:
    # for beta test only
    from processor_db import *
    from processor_db.crisprFunction import *
    from processor_db.processorCount import *
    from processor_db.pathwayFunc import *
    from processor_db.argsParser import *
    from processor_db.testVisual import *



# main function
def main():
    args=parseargs();
    logging.info('Welcome to barcode processor. Command: '+args.subcmd);
    # get read counts
    if args.subcmd == 'run' or args.subcmd == 'count':
        processorcount_main(args);

    # stat test
    if args.subcmd == 'run' or args.subcmd == 'test':
        processortest_main(args);

    # pathway test
    if args.subcmd == 'pathway':
        processor_pathwaytest(args);

    # visualizaiton
    if args.subcmd == 'plot':
        plot_main(args);
      
      


    if __name__ == '__main__':
        try:
            main();
        except KeyboardInterrupt:
            sys.stderr.write("User interrupt me! ;-) Bye!\n")
        sys.exit(0)
