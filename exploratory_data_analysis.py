import pandas as pd
import numpy as np
import pickle
import csv
from sklearn.model_selection import train_test_split

df = pd.read_csv('./datasets/records_4000.tsv', sep='\t')
# print(df.columns)
# print(df.head())
#3200 4 fold cross validation

df_poprock = df.loc[df['genre'] == 'Pop_Rock\n']

df_non_poprock = df.loc[df['genre'] != 'Pop_Rock\n']
print(df_poprock.shape)
print(df_non_poprock.shape)

train_poprock, test_poprock = train_test_split(df_poprock, test_size=0.2)
train_non_poprock, test_non_poprock = train_test_split(df_non_poprock, test_size = 0.2)
# print(df_pop_rock)