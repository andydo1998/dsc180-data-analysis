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

def get_data(filepath):
    '''
    Converts all database files in filepath into a single Dataframe
    Also converts columns into the correct data type
    
    Tests whether columns are correct data type
    Prints 'Dataframe is working intended' if data types are correct
    Return will be 2 DataFrames, the first one is the String values and the second one will be integer values
    
    Returns None if DataFrames are not in correct formats
    '''
    # 2 queries, one for string value and one for integer values
    appended_data_string = [] 
    appended_data_ull = []
    
    # loop through all files in test/testdata
    for filename in os.listdir(filepath):
        if filename == '.ipynb_checkpoints':
            continue
            
        # create the sql connection
        cnx = sqlite3.connect(filepath + filename)

        # read as dataframe, set 'MEASUREMENT_TIME' as date time object
        sub_df_string = pd.read_sql_query("SELECT * FROM COUNTERS_STRING_TIME_DATA", cnx)
        sub_df_ull = pd.read_sql_query("SELECT * FROM COUNTERS_ULL_TIME_DATA", cnx)

        # append "Start Row"
        first_row_string = sub_df_string.loc[0]
        new_row_string = pd.DataFrame({'MEASUREMENT_TIME': first_row_string[0], 'ID_INPUT': first_row_string[1], 'VALUE': 's0', 'PRIVATE_DATA': 0}, index =[0])
        sub_df_string = pd.concat([new_row_string, sub_df_string]).reset_index(drop=True)
        
        # append the informations
        appended_data_string.append(sub_df_string)
        appended_data_ull.append(sub_df_ull)

    # converting into 2 dataframes
    df_string = pd.concat(appended_data_string, ignore_index = True)
    df_ull = pd.concat(appended_data_ull, ignore_index = True)
    
    # preprocess the data
    df_string = preprocess(df_string)
    df_ull = preprocess(df_ull)
    
    # run tests on dataframe
    if (test_dataframe_string(df_string) and test_dataframe_ull(df_ull)):
        return df_string, df_ull
    
    # something went wrong!
    print('Data Processing Error')
    return None


def preprocess(df):
    '''
    Preprocess DataFrame so all data types are correct
    '''
    df['MEASUREMENT_TIME'] = pd.to_datetime(df['MEASUREMENT_TIME'])
    df['PRIVATE_DATA'] = df['PRIVATE_DATA'].astype(int)
    
    # We are currently focusing the string df
    if test_dataframe_string(df):
        df = df[df['ID_INPUT'] == 3]
        df['VALUE'] = df['VALUE'].str.lower()
    
    return df

def test_dataframe_string(df):
    '''
    Checks whether the string DataFrame is in the correct format
    '''
    # get all dtypes
    dtypes = df.dtypes
    
    # columns should be date time, integer, string, then integer
    if dtypes[0] == 'datetime64[ns]' and dtypes[1] == 'int64' and dtypes[2] == 'object' and (dtypes[3] == 'int32' or dtypes[3] == 'int64'):
        return True
    
    return False
        

def test_dataframe_ull(df):
    '''
    Checks whether the ull DataFrame is in the correct format
    '''
    # get all dtypes
    dtypes = df.dtypes
    
    # columns should be date time, integer, integer, then integer
    if dtypes[0] == 'datetime64[ns]' and dtypes[1] == 'int64' and dtypes[2] == 'int64' and (dtypes[3] == 'int32' or dtypes[3] == 'int64'):
        return True
    
    return False