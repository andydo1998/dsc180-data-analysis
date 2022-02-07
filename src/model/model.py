from sklearn.model_selection import train_test_split
import sys
import sqlite3
import pandas as pd
import numpy as np
import os
import json
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from collections import defaultdict

def getPred(numExe, start='s0'):
    """
    Predicts laptop foreground window for a specfied number of exe and starting exe
    """
    pred = [start]
    for action in range(numExe-1):
        prev = pred[-1]
        max_prob = 0
        new_exe = ''
        for k in pairProb.keys(): # Finds the most likely following exe given the previous
            if k[0] == prev and pairProb[k] > max_prob:
                new_exe = k[1]
                max_prob = pairProb[k]
        if new_exe == '': # If the exe was not in the training data return the most common exe
            new_exe = 'chrome.exe'
        pred.append(new_exe)
    return pred

def model(data):
    """
    
    """
    pairCount = defaultdict(int) # dict with unique senquential exe pairs being keys
    allPairs = []
    for i in range(df.shape[0]-1):
        pair = (df.iloc[i]['VALUE'], df.iloc[i+1]['VALUE'])
        allPairs.append(pair)
        pairCount[pair] += 1

    X = np.array([x[0] for x in allPairs])
    y = np.array([x[1] for x in allPairs])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    pairCountTrain = defaultdict(int)
    for i in range(len(X_train)):
        pair = (X_train[i], y_train[i])
        pairCountTrain[pair] += 1

    pairProb = defaultdict(int)
    for pair in pairCountTrain:
        b_count = sum(X_train == pair[0])
        pairProb[pair] = pairCountTrain[pair] / b_count # divides counts by number of pairs for the first exe ('B' in P(A|B))


    f = open('output.txt', 'w')

    f.write('Input Exe  Predicted Exe \n')

    for exe in exes:
        prediction = getPred(2, exe)
        string = exe + ', ' + prediction[1] + '\n'
        f.write(string)

    f.close()
    
    print('done')
