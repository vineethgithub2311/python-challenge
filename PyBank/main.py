# this is the Pybank challenge

import pandas as pd
import numpy as np

#path for csv file
file_path = "/Users/vineethkumargattu/Desktop/Data/python-challenge/PyBank/Resources/budget_data.csv"

#import csv file into pandas dataframe
df = pd.read_csv(file_path)
#print (df.head())
#print (df.dtypes)

print('-------------------------------------------')

#The total number of months included in the dataset
total_months = df.loc [:, 'Date']
print (f'Total Months: {total_months.count()}')

# The total net amount of Profit/Losses over entire period
net = df.loc [:, 'Profit/Losses']
print (f'Total: ${net.sum()}') 

#The average change in "Profit/Losses" between months over the entire period
df ['change'] = df['Profit/Losses'].diff()

#change_values = np.around(change_values, 2) # round values?
df = df.dropna(how='any')
df2 = round(df['change'].mean(),2)
print (f'Average Change: $ {df2}')

#The greatest increase in profits (date and amount) over the entire period

df2 = df.loc[df['change'].idxmax()]
dDte = df2['Date']
change = df2['change']
print (f'Greatest Increase in Profits: {dDte} ($ {change})')

#The greatest decrease in losses (date and amount) over the entire period
df2 = df.loc[df['change'].idxmin()]
dDte = df2['Date']
change = df2['change']
print (f'Greatest Decrease in Profits: {dDte} ($ {change})')
