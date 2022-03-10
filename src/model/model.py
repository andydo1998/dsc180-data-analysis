from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

def getPred(numExe, pairProb, start='s0'):
	@@ -24,48 +30,41 @@ def getPred(numExe, pairProb, start='s0'):

def model(df):
    """
    Outputs the predicted following exe for every exe in our data in the outputs.txt file.
    This will differ everytime due to randomization in the data split
    """
    # groups data into sequential pairs
    allPairs = []
    for i in range(df.shape[0]-1):
        pair = (df.iloc[i]['VALUE'], df.iloc[i+1]['VALUE'])
        allPairs.append(pair)

    # split the data with x being the first part of the pair and y being the second
    X = np.array([x[0] for x in allPairs])
    y = np.array([x[1] for x in allPairs])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) # 80-20 train test split

    # collects unique pair frequency
    pairCountTrain = defaultdict(int)
    for i in range(len(X_train)):
        pair = (X_train[i], y_train[i])
        pairCountTrain[pair] += 1

    # collects unique pair proability of appearing given the first exe
    pairProb = defaultdict(int)
    for pair in pairCountTrain:
        b_count = sum(X_train == pair[0])
        pairProb[pair] = pairCountTrain[pair] / b_count # P(A|B)

    exes = df['VALUE'].unique()

    # record predictions
    f = open('outputs/output.txt', 'w')
    f.write('Input Exe  Predicted Exe \n')
    for exe in exes:
        prediction = getPred(2, pairProb, exe)
        string = exe + ', ' + prediction[1] + '\n'
        f.write(string)
    f.close()

    # calculate accuracy
    outcome = []
    for i in range(len(X_test)):
        pred = getPred(2, pairProb, X_test[i])
        outcome.append(pred[1] == y_test[i])
    acc = (np.sum(outcome) / len(outcome)) * 100

    print('\nPredictions have been saved in "outputs\outputs.txt" \n\nAccuracy is ' + str(acc) + '%')
