#This is the PyPoll challenge

import pandas as pd
import numpy as np

#path for csv file
file_path = "/Users/vineethkumargattu/Desktop/Data/python-challenge/PyPoll/Resources/election_data.csv"

#import csv file into pandas dataframe
df = pd.read_csv(file_path)
print (df.head())
#print (df.dtypes)

print('-------------------------------------------')
print ('Election Results')

#The total number of votes cast
total_votes = df.loc [:, 'Voter ID']
print (f'Total Votes: {total_votes.count()}')

#A complete list of candidates who received votes
df_candidate_group = df.groupby(['Candidate']).count()
print(df_candidate_group)