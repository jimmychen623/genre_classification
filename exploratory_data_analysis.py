import pandas as pd
import numpy as np
import pickle
import csv
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import cross_val_score

dataframe = pd.read_csv('./datasets/records_4000.tsv', sep='\t')
dataframe['genre'] = dataframe['genre'].str[:-1]
dataframe = dataframe.drop(['track_id'], axis = 1)

# Format of genre is "Rap\n" with the return character
def create_train_validation_test(df, genre):

    #One hot encode the key and drop the original key
    one_hot_key = pd.get_dummies(df['key'])
    df = df.drop(['key'], axis=1)
    newcols = list(df.columns)
    df = pd.concat([df, one_hot_key], axis=1)
    for keyn in range(12):
        newcols.append('key_' + str(keyn))
    df.columns = newcols

    df = df.fillna(0)
    # 4000 songs from genre
    df_genre = df.loc[df['genre'] == genre]

    # 4000 songs from not genre
    df_non_genre = df.loc[df['genre'] != genre].sample(n=4000)
    df_non_genre['genre'] = 'nongenre'

    # Divide pop rock into train and test
    train_genre, test_genre = train_test_split(df_genre, test_size=0.2)

    # Divide non pop rock into train and test
    train_non_genre, test_non_genre = train_test_split(df_non_genre, test_size = 0.2)

    # Combine pop-rock and non-poprock into train/test
    train = train_genre.append(train_non_genre)
    test = test_genre.append(test_non_genre)

    train, validation = train_test_split(train, test_size=0.2)

    # training, validation, and test data

    X_train = train.drop(['genre'], axis = 1)
    y_train = train[['genre']]

    X_validation = validation.drop(['genre'], axis = 1)
    y_validation = validation[['genre']]

    X_test = test.drop(['genre'], axis = 1)
    y_test = test[['genre']]

    return X_train, y_train, X_validation, y_validation, X_test, y_test


X_train, y_train, X_validation, y_validation, X_test, y_test = create_train_validation_test(dataframe, 'Jazz')

print(X_train.head(100))
clf = svm.SVC(kernel='rbf', C=1).fit(X_train, y_train)
scores = clf.score(X_test, y_test)
print(scores)