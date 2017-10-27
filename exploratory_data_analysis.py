import pandas as pd
import numpy as np
import pickle
import csv

df = pd.read_csv('./SongCSV2.csv')

corr = df.corr(method='pearson')
print(corr)
