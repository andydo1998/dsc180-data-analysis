#!/usr/bin/env python

import sys
import sqlite3
import pandas as pd
import numpy as np
import os
import json

sys.path.insert(0, 'src/data')

from get_data import get_data

def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data'. 
    '''

    if 'data' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)

        # make the data target
        data = get_data(**data_cfg)
        print("variable 'data' has been loaded with 2 dataframes")


if __name__ == '__main__':
    # run via:
    # python main.py data
    targets = sys.argv[1:]
    main(targets)