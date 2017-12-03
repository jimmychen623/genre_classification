import pandas as pd
import numpy as np
import pickle
import csv
from sklearn.model_selection import train_test_split

dataframe = pd.read_csv('./datasets/records_4000.tsv', sep='\t')

# Format of genre is "Rap\n" with the return character
def create_train_validation_test(df, genre):
    # 4000 songs from genre
    df_poprock = df.loc[df['genre'] == genre]

    # 4000 songs from not genre
    df_non_poprock = df.loc[df['genre'] != genre].sample(n=4000)

    # Divide pop rock into train and test
    train_poprock, test_poprock = train_test_split(df_poprock, test_size=0.2)

    # Divide non pop rock into train and test
    train_non_poprock, test_non_poprock = train_test_split(df_non_poprock, test_size = 0.2)

    # Combine pop-rock and non-poprock into train/test
    train = train_poprock.append(train_non_poprock)
    test = test_poprock.append(test_non_poprock)

    train, validation = train_test_split(train, test_size=0.2)

    # training, validation, and test data

    X_train = train.drop(['genre'], axis = 1)
    y_train = train[['genre']]

    X_validation = validation.drop(['genre'], axis = 1)
    y_validation = validation[['genre']]

    X_test = test.drop(['genre'], axis = 1)
    y_test = test[['genre']]

    return X_train, y_train, X_validation, y_validation, X_test, y_test


X_train, y_train, X_validation, y_validation, X_test, y_test = create_train_validation_test(dataframe, 'Rap\n')

