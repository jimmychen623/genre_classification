import pandas as pd
import numpy as np
import pickle
import csv

# #Create csv for msd_tagtraum genre labels
# with open('./datasets/msd_tagtraum_cd2c.cls', 'r') as in_file:
#     stripped = (line.strip() for line in in_file)
#     lines = (line.split("\t") for line in stripped if line)
#     with open('./datasets/tagtraum_genre_labels.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerow(('song_id', 'genre'))
#         writer.writerows(lines)
#     out_file.close()
# in_file.close()
#
# #Create csv for magd genre labels
# with open('./datasets/msd-MAGD-genreAssignment.cls', 'r') as in_file:
#     stripped = (line.strip() for line in in_file)
#     lines = (line.split("\t") for line in stripped if line)
#     with open('./datasets/magd_genre_labels.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerow(('song_id', 'genre'))
#         writer.writerows(lines)
#     out_file.close()
# in_file.close()

#Combine the two genre label datasets

df1 = pd.read_csv('./datasets/tagtraum_genre_labels.csv')
df2 = pd.read_csv('./datasets/magd_genre_labels.csv')

df2 = pd.merge(df1, df2, on=['song_id'], how='inner')
print(df2.head(100))
df2[['song_id', 'genre_x', 'genre_y']].to_csv('all_genre_labels.csv', index=False)

# df2['is_churn'] = (df2['is_churn_x'] + df2['is_churn_y']) / 2.0
#
# df2['is_churn'] = df2['is_churn'].apply(lambda x: x*0.5)
# df2[['msno','is_churn']].to_csv('submission5.csv.gz', index=False, compression='gzip')
