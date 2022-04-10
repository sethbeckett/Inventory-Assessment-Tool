# -*- coding: utf-8 -*-
"""InventoryAssessor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N06P_kQRBYMxIemLm54o7XvFUvVitDlM
"""

'''
Program used to get filtered csv of inventory based on certain parameters.
Used to guide budgeting and purchasing decisions. Some fields made generic for privacy reasons.
'''
import pandas as pd
import numpy as np
import os
import datetime

os.getcwd()

os.listdir()

df = pd.read_csv("/content/<csv_file_name>", sep=";", dtype=str)

df['Account info : Expiration Date'] = pd.to_datetime(df['Account info : Expiration Date'], errors='coerce')
df['Last inventory'] = pd.to_datetime(df['Last inventory'], errors='coerce')

from pandas.core.arrays.categorical import contains
replaceDf = df.loc[(df['Account info : Expiration Date'] < np.datetime64('<2021-01-01>')) & #filter based on expiration
                   (df['Account info : Assessed'] == 'Yes') & #only assessed pcs
                   (df['Last inventory'] > np.datetime64('<2021-01-01>')) & #used within specific date
                   (~df['Account info : Department'].str.contains('<department>', na=False, case=False)) & #not Xdepartment computers
                   (~df['IP address'].str.contains('<X.X.X>', na=False)) & #not in Xth segment
                   (df['Model'].str.contains('<model_name>', na=False, case=False)) #not a surface
                   ]
replaceDf = replaceDf.reset_index()
replaceDf

replaceDf = replaceDf.drop(columns=['index', '<Unnamed: X>'])

replaceDf = replaceDf.sort_values(by=['Model', 'Account info : Department'])
replaceDf

replaceDf.to_csv('/content/<output_csv>.csv', index=False)