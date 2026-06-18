import numpy as np
import pandas as pd

df= pd.read_csv('Countries.csv')
# print(df)
print()

#Q1 Which country has the highest population?
print(df[df['population']==df['population'].max()]['country'])
print()

#Q2 What is the capital of the country with highest population?
print(df[df['population']==df['population'].max()]['capital_city'])
print()

#Q3 Which country has the least population?
print(df[df['population']==df['population'].min()]['country'])
print()

#Q4 What is the capital of the country with least population?
print(df[df['population']==df['population'].min()]['capital_city'])
print()

#Q5 Give me top 5 countries with highest democratic score?
print(df.nlargest(5,'democracy_score')['country'])
# print(df.columns)

#Q6 How many total regions are there?
print(df['region'].value_counts().count())       #value_counts how many times a particular region appeared and count counts the regions
print()

#Q7 How many countries lie in eastern europe region?
print(df['region'].value_counts()['Eastern Europe'])
print()

#Q8 Who is the political leader of the highest populated country?
print(df.nlargest(2, 'population').iloc[1]['political_leader'])          #method 1
print()
print(df[df['population']==df['population'].nlargest(2).iloc[1]])       #method 2
print()
# when we find 2 largest , the largest will be on index 0 and second largest on index 1 , so to find second largest use iloc[1]

#Q9 How many countries are there whose political leaders are unknown?
print(df[df['political_leader'].isna()]['country'].count())
print()

#Q10 How many countries have republic in their full name?
count=0
def counting(text):
    global count
    if 'republic' in text.lower():
        count+=1
    return text    
print(df['country_long'].apply(counting))  
print(count)      

#Q11 Which country in african region has the highest population
african_df = df[df['continent']=='Africa']
print(african_df[african_df['population']==african_df['population'].max()])