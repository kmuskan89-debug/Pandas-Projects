import numpy as np
import pandas as pd

df= pd.read_csv('anime.csv')
print(df)
print()
print(df.head())            #displays top 5 rows
print()


# Q1 Create a seperate column for episodes
print(df.loc[1]['Title'])
print(df.loc[2]['Title'])
print(df.loc[3]['Title'])            #Every title has the no.of episodes written but a seperate column is not made
print()
#We can see that the episode is written in brackets inside the title, so we create a function

def extract_episodes(text):
    data=''
    check=False
    for i in text:
        if i==')':
            break
        if check==True:
            data+=i
        if i=='(':
            check=True
        
    return data       

df['Episodes']= df['Title'].apply(extract_episodes)     #created a new column eps and applied the function on title
print(df) 

df['Episodes']= df['Episodes'].str.replace('eps',"")    #replaced 'eps' with empty string to just get the numbers
print(df)                 #The episodes are still in string format , change it to int
df['Episodes']= df['Episodes'].astype(int)
print(df)


#Q2 Make a new column for timestamps

def extract_timestamps(text):
    data=""
    
    for i in range(len(text)):
        if text[i]==')':
            for j in range(i+1, i+20):
                data+=text[j]
    return data

df['TimeStamps']=df['Title'].apply(extract_timestamps)
print(df)     


#Q3 Which anime has the highest score?      
print(df[df['Score']==df['Score'].max()]['Title'])


#Q4 Top 5 highest scoring animes?
print(df[['Title','Score']].head())


#Q5 Which anime has the highest episodes count
print(df[df['Episodes']==df['Episodes'].max()][['Title','Episodes']])


#Q6 Animes with top 5 episode count
print(df.nlargest(5, 'Episodes')[['Title','Episodes']])