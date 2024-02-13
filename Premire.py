import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt




common_teams=['Newcastle United','Tottenham Hotspur','Wolverhampton Wanderers','Manchester United',
              'Manchester City','Arsenal','Leicester City','Crystal Palace','Chelsea',
              'Brighton and Hove Albion','Southampton','Everton','West Ham United','Liverpool']

st.title('Premier League Analysis of Team for Last 5 Seasons')
team=st.selectbox('Select Team:',common_teams)
df=pd.read_csv(r"C:\Users\hp\Downloads\archive (47)\Data.csv")
df.drop(columns=['Date','stadium','referee','attendance'],inplace=True)
df.drop_duplicates(inplace=True)
def winner(df):
    if df['Home_team_score']>df['Away_team_score']:
        return df['Home_team_name']
    elif df['Home_team_score']<df['Away_team_score']:
        return df['Away_team_name']
    else:
        return 'Draw'

def tranform(text):
    return text.split('. ')[1]

df['Winner']=df.apply(winner,axis=1)
df=df.drop(index=22379)
df=df.drop(index=15796)
df['Away_team_score']=df['Away_team_score'].astype(int)
df['Home_team_score']=df['Home_team_score'].astype(int)

df=df[df['Home_team_name'].isin(common_teams)]
df=df[df['Away_team_name'].isin(common_teams)]

df_2018=pd.read_csv(r"D:\pycharm_free\pythonProject\2018-19.csv")
df_2019=pd.read_csv(r"D:\pycharm_free\pythonProject\2019-20.csv")
df_2020=pd.read_csv(r"D:\pycharm_free\pythonProject\2020-21.csv")
df_2021=pd.read_csv(r"D:\pycharm_free\pythonProject\2021-22.csv")
df_2022=pd.read_csv(r"D:\pycharm_free\pythonProject\2022-23.csv")

df_team_stats_2018=pd.read_csv(r"D:\pycharm_free\pythonProject\team_stats_2018-19.csv")
df_team_stats_2019=pd.read_csv(r"D:\pycharm_free\pythonProject\team_stats_2019-20.csv")
df_team_stats_2020=pd.read_csv(r"D:\pycharm_free\pythonProject\team_stats_2020-21.csv")
df_team_stats_2021=pd.read_csv(r"D:\pycharm_free\pythonProject\team_stats_2021-22.csv")
df_team_stats_2022=pd.read_csv(r"D:\pycharm_free\pythonProject\team_stats_2022-23.csv")

df_team_stats_2018['Team']=df_team_stats_2018['Team'].apply(tranform)
df_team_stats_2019['Team']=df_team_stats_2019['Team'].apply(tranform)
df_team_stats_2020['Team']=df_team_stats_2020['Team'].apply(tranform)
df_team_stats_2021['Team']=df_team_stats_2021['Team'].apply(tranform)
df_team_stats_2022['Team']=df_team_stats_2022['Team'].apply(tranform)

df_team_stats_2018.drop(columns=['Unnamed: 6','Unnamed: 7'],inplace=True)
df_team_stats_2019.drop(columns=['Unnamed: 6','Unnamed: 7'],inplace=True)
df_team_stats_2020.drop(columns=['Unnamed: 6','Unnamed: 7'],inplace=True)
df_team_stats_2021.drop(columns=['Unnamed: 6','Unnamed: 7'],inplace=True)
df_team_stats_2022.drop(columns=['Unnamed: 6','Unnamed: 7'],inplace=True)

df_team_stats_2018['Team']=df_team_stats_2018['Team'].replace('Tottenham','Tottenham Hotspur')
df_team_stats_2018['Team']=df_team_stats_2018['Team'].replace('Leicester','Leicester City')
df_team_stats_2018['Team']=df_team_stats_2018['Team'].replace('West Ham','West Ham United')
df_team_stats_2018['Team']=df_team_stats_2018['Team'].replace('Brighton','Brighton and Hove Albion')
df_team_stats_2018['Team']=df_team_stats_2018['Team'].replace('Newcastle','Newcastle United')
df_team_stats_2018['Team']=df_team_stats_2018['Team'].replace('Wolves','Wolverhampton Wanderers')

df_team_stats_2019['Team']=df_team_stats_2019['Team'].replace('Tottenham','Tottenham Hotspur')
df_team_stats_2019['Team']=df_team_stats_2019['Team'].replace('Leicester','Leicester City')
df_team_stats_2018['Team']=df_team_stats_2018['Team'].replace('West Ham','West Ham United')
df_team_stats_2019['Team']=df_team_stats_2019['Team'].replace('Brighton','Brighton and Hove Albion')
df_team_stats_2019['Team']=df_team_stats_2019['Team'].replace('Newcastle','Newcastle United')
df_team_stats_2019['Team']=df_team_stats_2019['Team'].replace('Wolves','Wolverhampton Wanderers')

df_team_stats_2020['Team']=df_team_stats_2020['Team'].replace('Tottenham','Tottenham Hotspur')
df_team_stats_2020['Team']=df_team_stats_2020['Team'].replace('Leicester','Leicester City')
df_team_stats_2020['Team']=df_team_stats_2020['Team'].replace('West Ham','West Ham United')
df_team_stats_2020['Team']=df_team_stats_2020['Team'].replace('Brighton','Brighton and Hove Albion')
df_team_stats_2020['Team']=df_team_stats_2020['Team'].replace('Newcastle','Newcastle United')
df_team_stats_2020['Team']=df_team_stats_2020['Team'].replace('Wolves','Wolverhampton Wanderers')

df_team_stats_2021['Team']=df_team_stats_2021['Team'].replace('Tottenham','Tottenham Hotspur')
df_team_stats_2021['Team']=df_team_stats_2021['Team'].replace('Leicester','Leicester City')
df_team_stats_2021['Team']=df_team_stats_2021['Team'].replace('West Ham','West Ham United')
df_team_stats_2021['Team']=df_team_stats_2021['Team'].replace('Brighton','Brighton and Hove Albion')
df_team_stats_2021['Team']=df_team_stats_2021['Team'].replace('Newcastle','Newcastle United')
df_team_stats_2021['Team']=df_team_stats_2021['Team'].replace('Wolves','Wolverhampton Wanderers')

df_team_stats_2022['Team']=df_team_stats_2022['Team'].replace('Tottenham','Tottenham Hotspur')
df_team_stats_2022['Team']=df_team_stats_2022['Team'].replace('Leicester','Leicester City')
df_team_stats_2022['Team']=df_team_stats_2022['Team'].replace('West Ham','West Ham United')
df_team_stats_2022['Team']=df_team_stats_2022['Team'].replace('Brighton','Brighton and Hove Albion')
df_team_stats_2022['Team']=df_team_stats_2022['Team'].replace('Newcastle','Newcastle United')
df_team_stats_2022['Team']=df_team_stats_2022['Team'].replace('Wolves','Wolverhampton Wanderers')


card_df_2018=pd.read_csv(r"D:\pycharm_free\pythonProject\red_2018-19.csv")
card_df_2019=pd.read_csv(r"D:\pycharm_free\pythonProject\red_2019-20.csv")
card_df_2020=pd.read_csv(r"D:\pycharm_free\pythonProject\red_2020-21.csv")
card_df_2021=pd.read_csv(r"D:\pycharm_free\pythonProject\red_2021-22.csv")
card_df_2022=pd.read_csv(r"D:\pycharm_free\pythonProject\red_2022-23.csv")

player_df_2018=pd.read_csv(r"D:\pycharm_free\pythonProject\Player_2018-19.csv")
player_df_2019=pd.read_csv(r"D:\pycharm_free\pythonProject\Player_2019-20.csv")
player_df_2020=pd.read_csv(r"D:\pycharm_free\pythonProject\Player_2020-21.csv")
player_df_2021=pd.read_csv(r"D:\pycharm_free\pythonProject\Player_2021-22.csv")
player_df_2022=pd.read_csv(r"D:\pycharm_free\pythonProject\Player_2022-23.csv")

player_df_2018.drop(columns=['Unnamed: 0','penalty'],inplace=True)
player_df_2019.drop(columns=['Unnamed: 0','penalty'],inplace=True)
player_df_2020.drop(columns=['Unnamed: 0','penalty'],inplace=True)
player_df_2021.drop(columns=['Unnamed: 0','penalty'],inplace=True)
player_df_2022.drop(columns=['Unnamed: 0','penalty'],inplace=True)

player_df_2018['Team']=player_df_2018['Team'].replace('Arsenal FC ','Arsenal')
player_df_2018['Team']=player_df_2018['Team'].replace('Liverpool FC ','Liverpool')
player_df_2018['Team']=player_df_2018['Team'].replace('Manchester City ','Manchester City')
player_df_2018['Team']=player_df_2018['Team'].replace('Leicester City ','Leicester City')
player_df_2018['Team']=player_df_2018['Team'].replace('Tottenham Hotspur ','Tottenham Hotspur')
player_df_2018['Team']=player_df_2018['Team'].replace('Wolverhampton Wanderers ','Wolverhampton Wanderers')
player_df_2018['Team']=player_df_2018['Team'].replace('Brighton & Hove Albion ','Brighton and Hove Albion')
player_df_2018['Team']=player_df_2018['Team'].replace('Manchester United ','Manchester United')
player_df_2018['Team']=player_df_2018['Team'].replace('Everton FC ','Everton')
player_df_2018['Team']=player_df_2018['Team'].replace('Newcastle United ','Newcastle United')
player_df_2018['Team']=player_df_2018['Team'].replace('Crystal Palace ','Crystal Palace')
player_df_2018['Team']=player_df_2018['Team'].replace('West Ham United ','West Ham United')
player_df_2018['Team']=player_df_2018['Team'].replace('Southampton FC ','Southampton')

player_df_2019['Team']=player_df_2019['Team'].replace('Arsenal FC ','Arsenal')
player_df_2019['Team']=player_df_2019['Team'].replace('Liverpool FC ','Liverpool')
player_df_2019['Team']=player_df_2019['Team'].replace('Manchester City ','Manchester City')
player_df_2019['Team']=player_df_2019['Team'].replace('Leicester City ','Leicester City')
player_df_2019['Team']=player_df_2019['Team'].replace('Tottenham Hotspur ','Tottenham Hotspur')
player_df_2019['Team']=player_df_2019['Team'].replace('Wolverhampton Wanderers ','Wolverhampton Wanderers')
player_df_2019['Team']=player_df_2019['Team'].replace('Brighton & Hove Albion ','Brighton and Hove Albion')
player_df_2019['Team']=player_df_2019['Team'].replace('Manchester United ','Manchester United')
player_df_2019['Team']=player_df_2019['Team'].replace('Everton FC ','Everton')
player_df_2019['Team']=player_df_2019['Team'].replace('Newcastle United ','Newcastle United')
player_df_2019['Team']=player_df_2019['Team'].replace('Crystal Palace ','Crystal Palace')
player_df_2019['Team']=player_df_2019['Team'].replace('West Ham United ','West Ham United')
player_df_2019['Team']=player_df_2019['Team'].replace('Southampton FC ','Southampton')

player_df_2020['Team']=player_df_2020['Team'].replace('Arsenal FC ','Arsenal')
player_df_2020['Team']=player_df_2020['Team'].replace('Liverpool FC ','Liverpool')
player_df_2020['Team']=player_df_2020['Team'].replace('Manchester City ','Manchester City')
player_df_2020['Team']=player_df_2020['Team'].replace('Leicester City ','Leicester City')
player_df_2020['Team']=player_df_2020['Team'].replace('Tottenham Hotspur ','Tottenham Hotspur')
player_df_2020['Team']=player_df_2020['Team'].replace('Wolverhampton Wanderers ','Wolverhampton Wanderers')
player_df_2020['Team']=player_df_2020['Team'].replace('Brighton & Hove Albion ','Brighton and Hove Albion')
player_df_2020['Team']=player_df_2020['Team'].replace('Manchester United ','Manchester United')
player_df_2020['Team']=player_df_2020['Team'].replace('Everton FC ','Everton')
player_df_2020['Team']=player_df_2020['Team'].replace('Newcastle United ','Newcastle United')
player_df_2020['Team']=player_df_2020['Team'].replace('Crystal Palace ','Crystal Palace')
player_df_2020['Team']=player_df_2020['Team'].replace('West Ham United ','West Ham United')
player_df_2020['Team']=player_df_2020['Team'].replace('Southampton FC ','Southampton')

player_df_2021['Team']=player_df_2021['Team'].replace('Arsenal FC ','Arsenal')
player_df_2021['Team']=player_df_2021['Team'].replace('Liverpool FC ','Liverpool')
player_df_2021['Team']=player_df_2021['Team'].replace('Manchester City ','Manchester City')
player_df_2021['Team']=player_df_2021['Team'].replace('Leicester City ','Leicester City')
player_df_2021['Team']=player_df_2021['Team'].replace('Tottenham Hotspur ','Tottenham Hotspur')
player_df_2021['Team']=player_df_2021['Team'].replace('Wolverhampton Wanderers ','Wolverhampton Wanderers')
player_df_2021['Team']=player_df_2021['Team'].replace('Brighton & Hove Albion ','Brighton and Hove Albion')
player_df_2021['Team']=player_df_2021['Team'].replace('Manchester United ','Manchester United')
player_df_2021['Team']=player_df_2021['Team'].replace('Everton FC ','Everton')
player_df_2021['Team']=player_df_2021['Team'].replace('Newcastle United ','Newcastle United')
player_df_2021['Team']=player_df_2021['Team'].replace('Crystal Palace ','Crystal Palace')
player_df_2021['Team']=player_df_2021['Team'].replace('West Ham United ','West Ham United')
player_df_2021['Team']=player_df_2021['Team'].replace('Southampton FC ','Southampton')

player_df_2022['Team']=player_df_2022['Team'].replace('Arsenal FC ','Arsenal')
player_df_2022['Team']=player_df_2022['Team'].replace('Liverpool FC ','Liverpool')
player_df_2022['Team']=player_df_2022['Team'].replace('Manchester City ','Manchester City')
player_df_2022['Team']=player_df_2022['Team'].replace('Leicester City ','Leicester City')
player_df_2022['Team']=player_df_2022['Team'].replace('Tottenham Hotspur ','Tottenham Hotspur')
player_df_2022['Team']=player_df_2022['Team'].replace('Wolverhampton Wanderers ','Wolverhampton Wanderers')
player_df_2022['Team']=player_df_2022['Team'].replace('Brighton & Hove Albion ','Brighton and Hove Albion')
player_df_2022['Team']=player_df_2022['Team'].replace('Manchester United ','Manchester United')
player_df_2022['Team']=player_df_2022['Team'].replace('Everton FC ','Everton')
player_df_2022['Team']=player_df_2022['Team'].replace('Newcastle United ','Newcastle United')
player_df_2022['Team']=player_df_2022['Team'].replace('Crystal Palace ','Crystal Palace')
player_df_2022['Team']=player_df_2022['Team'].replace('West Ham United ','West Ham United')
player_df_2022['Team']=player_df_2022['Team'].replace('Southampton FC ','Southampton')

player_assist_df_2018=pd.read_csv(r"D:\pycharm_free\pythonProject\Player_Assist_2018-19.csv")
player_assist_df_2019=pd.read_csv(r"D:\pycharm_free\pythonProject\Player_Assist_2019-20.csv")
player_assist_df_2020=pd.read_csv(r"D:\pycharm_free\pythonProject\Player_Assist_2020-21.csv")
player_assist_df_2021=pd.read_csv(r"D:\pycharm_free\pythonProject\Player_Assist_2021-22.csv")
player_assist_df_2022=pd.read_csv(r"D:\pycharm_free\pythonProject\Player_Assist_2022-23.csv")

player_assist_df_2018['Team']=player_assist_df_2018['Team'].replace('Arsenal FC ','Arsenal')
player_assist_df_2018['Team']=player_assist_df_2018['Team'].replace('Liverpool FC ','Liverpool')
player_assist_df_2018['Team']=player_assist_df_2018['Team'].replace('Manchester City ','Manchester City')
player_assist_df_2018['Team']=player_assist_df_2018['Team'].replace('Leicester City ','Leicester City')
player_assist_df_2018['Team']=player_assist_df_2018['Team'].replace('Tottenham Hotspur ','Tottenham Hotspur')
player_assist_df_2018['Team']=player_assist_df_2018['Team'].replace('Wolverhampton Wanderers ','Wolverhampton Wanderers')
player_assist_df_2018['Team']=player_assist_df_2018['Team'].replace('Brighton & Hove Albion ','Brighton and Hove Albion')
player_assist_df_2018['Team']=player_assist_df_2018['Team'].replace('Manchester United ','Manchester United')
player_assist_df_2018['Team']=player_assist_df_2018['Team'].replace('Everton FC ','Everton')
player_assist_df_2018['Team']=player_assist_df_2018['Team'].replace('Newcastle United ','Newcastle United')
player_assist_df_2018['Team']=player_assist_df_2018['Team'].replace('Crystal Palace ','Crystal Palace')
player_assist_df_2018['Team']=player_assist_df_2018['Team'].replace('West Ham United ','West Ham United')
player_assist_df_2018['Team']=player_assist_df_2018['Team'].replace('Southampton FC ','Southampton')

player_assist_df_2019['Team']=player_assist_df_2019['Team'].replace('Arsenal FC ','Arsenal')
player_assist_df_2019['Team']=player_assist_df_2019['Team'].replace('Liverpool FC ','Liverpool')
player_assist_df_2019['Team']=player_assist_df_2019['Team'].replace('Manchester City ','Manchester City')
player_assist_df_2019['Team']=player_assist_df_2019['Team'].replace('Leicester City ','Leicester City')
player_assist_df_2019['Team']=player_assist_df_2019['Team'].replace('Tottenham Hotspur ','Tottenham Hotspur')
player_assist_df_2019['Team']=player_assist_df_2019['Team'].replace('Wolverhampton Wanderers ','Wolverhampton Wanderers')
player_assist_df_2019['Team']=player_assist_df_2019['Team'].replace('Brighton & Hove Albion ','Brighton and Hove Albion')
player_assist_df_2019['Team']=player_assist_df_2019['Team'].replace('Manchester United ','Manchester United')
player_assist_df_2019['Team']=player_assist_df_2019['Team'].replace('Everton FC ','Everton')
player_assist_df_2019['Team']=player_assist_df_2019['Team'].replace('Newcastle United ','Newcastle United')
player_assist_df_2019['Team']=player_assist_df_2019['Team'].replace('Crystal Palace ','Crystal Palace')
player_assist_df_2019['Team']=player_assist_df_2019['Team'].replace('West Ham United ','West Ham United')
player_assist_df_2019['Team']=player_assist_df_2019['Team'].replace('Southampton FC ','Southampton')

player_assist_df_2020['Team']=player_assist_df_2020['Team'].replace('Arsenal FC ','Arsenal')
player_assist_df_2020['Team']=player_assist_df_2020['Team'].replace('Liverpool FC ','Liverpool')
player_assist_df_2020['Team']=player_assist_df_2020['Team'].replace('Manchester City ','Manchester City')
player_assist_df_2020['Team']=player_assist_df_2020['Team'].replace('Leicester City ','Leicester City')
player_assist_df_2020['Team']=player_assist_df_2020['Team'].replace('Tottenham Hotspur ','Tottenham Hotspur')
player_assist_df_2020['Team']=player_assist_df_2020['Team'].replace('Wolverhampton Wanderers ','Wolverhampton Wanderers')
player_assist_df_2020['Team']=player_assist_df_2020['Team'].replace('Brighton & Hove Albion ','Brighton and Hove Albion')
player_assist_df_2020['Team']=player_assist_df_2020['Team'].replace('Manchester United ','Manchester United')
player_assist_df_2020['Team']=player_assist_df_2020['Team'].replace('Everton FC ','Everton')
player_assist_df_2020['Team']=player_assist_df_2020['Team'].replace('Newcastle United ','Newcastle United')
player_assist_df_2020['Team']=player_assist_df_2020['Team'].replace('Crystal Palace ','Crystal Palace')
player_assist_df_2020['Team']=player_assist_df_2020['Team'].replace('West Ham United ','West Ham United')
player_assist_df_2020['Team']=player_assist_df_2020['Team'].replace('Southampton FC ','Southampton')

player_assist_df_2021['Team']=player_assist_df_2021['Team'].replace('Arsenal FC ','Arsenal')
player_assist_df_2021['Team']=player_assist_df_2021['Team'].replace('Liverpool FC ','Liverpool')
player_assist_df_2021['Team']=player_assist_df_2021['Team'].replace('Manchester City ','Manchester City')
player_assist_df_2021['Team']=player_assist_df_2021['Team'].replace('Leicester City ','Leicester City')
player_assist_df_2021['Team']=player_assist_df_2021['Team'].replace('Tottenham Hotspur ','Tottenham Hotspur')
player_assist_df_2021['Team']=player_assist_df_2021['Team'].replace('Wolverhampton Wanderers ','Wolverhampton Wanderers')
player_assist_df_2021['Team']=player_assist_df_2021['Team'].replace('Brighton & Hove Albion ','Brighton and Hove Albion')
player_assist_df_2021['Team']=player_assist_df_2021['Team'].replace('Manchester United ','Manchester United')
player_assist_df_2021['Team']=player_assist_df_2021['Team'].replace('Everton FC ','Everton')
player_assist_df_2021['Team']=player_assist_df_2021['Team'].replace('Newcastle United ','Newcastle United')
player_assist_df_2021['Team']=player_assist_df_2021['Team'].replace('Crystal Palace ','Crystal Palace')
player_assist_df_2021['Team']=player_assist_df_2021['Team'].replace('West Ham United ','West Ham United')
player_assist_df_2021['Team']=player_assist_df_2021['Team'].replace('Southampton FC ','Southampton')

player_assist_df_2022['Team']=player_assist_df_2022['Team'].replace('Arsenal FC ','Arsenal')
player_assist_df_2022['Team']=player_assist_df_2022['Team'].replace('Liverpool FC ','Liverpool')
player_assist_df_2022['Team']=player_assist_df_2022['Team'].replace('Manchester City ','Manchester City')
player_assist_df_2022['Team']=player_assist_df_2022['Team'].replace('Leicester City ','Leicester City')
player_assist_df_2022['Team']=player_assist_df_2022['Team'].replace('Tottenham Hotspur ','Tottenham Hotspur')
player_assist_df_2022['Team']=player_assist_df_2022['Team'].replace('Wolverhampton Wanderers ','Wolverhampton Wanderers')
player_assist_df_2022['Team']=player_assist_df_2022['Team'].replace('Brighton & Hove Albion ','Brighton and Hove Albion')
player_assist_df_2022['Team']=player_assist_df_2022['Team'].replace('Manchester United ','Manchester United')
player_assist_df_2022['Team']=player_assist_df_2022['Team'].replace('Everton FC ','Everton')
player_assist_df_2022['Team']=player_assist_df_2022['Team'].replace('Newcastle United ','Newcastle United')
player_assist_df_2022['Team']=player_assist_df_2022['Team'].replace('Crystal Palace ','Crystal Palace')
player_assist_df_2022['Team']=player_assist_df_2022['Team'].replace('West Ham United ','West Ham United')
player_assist_df_2022['Team']=player_assist_df_2022['Team'].replace('Southampton FC ','Southampton')

player_assist_df_2022.drop(columns=['Unnamed: 0'],inplace=True)
player_assist_df_2021.drop(columns=['Unnamed: 0'],inplace=True)
player_assist_df_2020.drop(columns=['Unnamed: 0'],inplace=True)
player_assist_df_2019.drop(columns=['Unnamed: 0'],inplace=True)
player_assist_df_2018.drop(columns=['Unnamed: 0'],inplace=True)

merged_assist_df = pd.merge(player_assist_df_2018, player_assist_df_2019, on='Player', how='outer', suffixes=('_df1', '_df2'))

# Replace NaN with 0 in 'marks' columns
merged_assist_df['Assists_df1'].fillna(0, inplace=True)
merged_assist_df['Assists_df2'].fillna(0, inplace=True)

# Create a new column representing the sum of marks from both dataframes
merged_assist_df['total_Assist'] = merged_assist_df['Assists_df1'] + merged_assist_df['Assists_df2']
merged_assist_df['Country_df2'].fillna(merged_assist_df['Country_df1'],inplace=True)
merged_assist_df['Team_df2'].fillna(merged_assist_df['Team_df1'],inplace=True)
merged_assist_df.drop(columns=['Country_df1','Team_df1','Assists_df1','Assists_df2'],axis=1,inplace=True)
merged_assist_df.rename(columns={'Country_df2':'Country','Team_df2':'Team','total_Assist':'assist'},inplace=True)
merged_assist_df = pd.merge(merged_assist_df, player_assist_df_2020, on='Player', how='outer', suffixes=('_df1', '_df2'))

# Replace NaN with 0 in 'marks' columns
merged_assist_df['assist'].fillna(0, inplace=True)
merged_assist_df['Assists'].fillna(0, inplace=True)

# Create a new column representing the sum of marks from both dataframes
merged_assist_df['total_Assist'] = merged_assist_df['assist'] + merged_assist_df['Assists']

merged_assist_df['Country_df2'].fillna(merged_assist_df['Country_df1'],inplace=True)
merged_assist_df['Team_df2'].fillna(merged_assist_df['Team_df1'],inplace=True)

merged_assist_df.drop(columns=['Country_df1','Team_df1','Assists','assist'],axis=1,inplace=True)
merged_assist_df.rename(columns={'Country_df2':'Country','Team_df2':'Team','total_assist':'assist'},inplace=True)
merged_assist_df = pd.merge(merged_assist_df, player_assist_df_2021, on='Player', how='outer', suffixes=('_df1', '_df2'))


# Replace NaN with 0 in 'marks' columns
merged_assist_df['total_Assist'].fillna(0, inplace=True)
merged_assist_df['Assists'].fillna(0, inplace=True)

# Create a new column representing the sum of marks from both dataframes
merged_assist_df['total_assist'] = merged_assist_df['total_Assist'] + merged_assist_df['Assists']

merged_assist_df['Country_df2'].fillna(merged_assist_df['Country_df1'],inplace=True)
merged_assist_df['Team_df2'].fillna(merged_assist_df['Team_df1'],inplace=True)

merged_assist_df.drop(columns=['Country_df1','Team_df1','Assists','total_Assist'],axis=1,inplace=True)
merged_assist_df.rename(columns={'Country_df2':'Country','Team_df2':'Team','total_assist':'assist'},inplace=True)
merged_assist_df = pd.merge(merged_assist_df, player_assist_df_2021, on='Player', how='outer', suffixes=('_df1', '_df2'))


# Replace NaN with 0 in 'marks' columns
merged_assist_df['assist'].fillna(0, inplace=True)
merged_assist_df['Assists'].fillna(0, inplace=True)

# Create a new column representing the sum of marks from both dataframes
merged_assist_df['total_assist'] = merged_assist_df['assist'] + merged_assist_df['Assists']

merged_assist_df['Country_df2'].fillna(merged_assist_df['Country_df1'],inplace=True)
merged_assist_df['Team_df2'].fillna(merged_assist_df['Team_df1'],inplace=True)

merged_assist_df.drop(columns=['Country_df1','Team_df1','Assists','assist'],axis=1,inplace=True)
merged_assist_df.rename(columns={'Country_df2':'Country','Team_df2':'Team','total_assist':'assist'},inplace=True)
merged_assist_df=merged_assist_df.sort_values(by='assist',ascending=False)


merged_df = pd.merge(player_df_2018, player_df_2019, on='Player', how='outer', suffixes=('_df1', '_df2'))

# Replace NaN with 0 in 'marks' columns
merged_df['goal_df1'].fillna(0, inplace=True)
merged_df['goal_df2'].fillna(0, inplace=True)

# Create a new column representing the sum of marks from both dataframes
merged_df['total_goal'] = merged_df['goal_df1'] + merged_df['goal_df2']
merged_df['Country_df2'].fillna(merged_df['Country_df1'],inplace=True)
merged_df['Team_df2'].fillna(merged_df['Team_df1'],inplace=True)
merged_df.drop(columns=['Country_df1','Team_df1','goal_df1','goal_df2'],axis=1,inplace=True)
merged_df.rename(columns={'Country_df2':'Country','Team_df2':'Team','total_goal':'goal'},inplace=True)
merged_df = pd.merge(merged_df, player_df_2020, on='Player', how='outer', suffixes=('_df1', '_df2'))

# Replace NaN with 0 in 'marks' columns
merged_df['goal_df1'].fillna(0, inplace=True)
merged_df['goal_df2'].fillna(0, inplace=True)

# Create a new column representing the sum of marks from both dataframes
merged_df['total_goal'] = merged_df['goal_df1'] + merged_df['goal_df2']
merged_df['Country_df2'].fillna(merged_df['Country_df1'],inplace=True)
merged_df['Team_df2'].fillna(merged_df['Team_df1'],inplace=True)
merged_df.drop(columns=['Country_df1','Team_df1','goal_df1','goal_df2'],axis=1,inplace=True)
merged_df.rename(columns={'Country_df2':'Country','Team_df2':'Team','total_goal':'goal'},inplace=True)
merged_df = pd.merge(merged_df, player_df_2021, on='Player', how='outer', suffixes=('_df1', '_df2'))

# Replace NaN with 0 in 'marks' columns
merged_df['goal_df1'].fillna(0, inplace=True)
merged_df['goal_df2'].fillna(0, inplace=True)

# Create a new column representing the sum of marks from both dataframes
merged_df['total_goal'] = merged_df['goal_df1'] + merged_df['goal_df2']
merged_df['Country_df2'].fillna(merged_df['Country_df1'],inplace=True)
merged_df['Team_df2'].fillna(merged_df['Team_df1'],inplace=True)
merged_df.drop(columns=['Country_df1','Team_df1','goal_df1','goal_df2'],axis=1,inplace=True)
merged_df.rename(columns={'Country_df2':'Country','Team_df2':'Team','total_goal':'goal'},inplace=True)
merged_df = pd.merge(merged_df, player_df_2022, on='Player', how='outer', suffixes=('_df1', '_df2'))

# Replace NaN with 0 in 'marks' columns
merged_df['goal_df1'].fillna(0, inplace=True)
merged_df['goal_df2'].fillna(0, inplace=True)

# Create a new column representing the sum of marks from both dataframes
merged_df['total_goal'] = merged_df['goal_df1'] + merged_df['goal_df2']
merged_df['Country_df2'].fillna(merged_df['Country_df1'],inplace=True)
merged_df['Team_df2'].fillna(merged_df['Team_df1'],inplace=True)

merged_df.drop(columns=['Country_df1','Team_df1','goal_df1','goal_df2'],axis=1,inplace=True)
merged_df.rename(columns={'Country_df2':'Country','Team_df2':'Team','total_goal':'goal'},inplace=True)
merged_df=merged_df.sort_values(by='goal',ascending=False)




def analyze(team):
    st.header('Premier League Standing for last 5 Seasons')
    standing_2018=df_2018[df_2018['Team']==team].index[0]+1
    st.write('Premier League standing in 2018',standing_2018)
    standing_2019=df_2019[df_2019['Team']==team].index[0]+1
    st.write('Premier League standing in 2019',standing_2019)

    standing_2020=df_2020[df_2020['Team']==team].index[0]+1
    st.write('Premier League standing in 2020',standing_2020)

    standing_2021=df_2018[df_2021['Team']==team].index[0]+1
    st.write('Premier League standing in 2021',standing_2021)

    standing_2022=df_2022[df_2022['Team']==team].index[0]+1
    st.write('Premier League standing in 2022',standing_2022)




    st.header('Overall Analysis For Last 5 Season')
    matches_played = df[df['Home_team_name'] == team].shape[0] + \
                     df[df['Away_team_name'] == team].shape[0]
    st.write('Matches Played-',matches_played)
    matches_won = df[df['Winner'] == team].shape[0]
    st.write('Matches Won-', matches_won)
    data = df[(df['Home_team_name'] == team) | (df['Away_team_name'] == team)]
    matches_draw = data[data['Winner'] == 'Draw'].shape[0]
    st.write('Matches Draw-', matches_draw)
    matches_lost = matches_played - (matches_won + matches_draw)
    st.write('Matches Lost-', matches_lost)
    won_percentage = (matches_won / matches_played) * 100
    draw_percentage = (matches_draw / matches_played) * 100
    lost_percentage = (matches_lost / matches_played) * 100

    labels = ['Won', 'Draw', 'Lost']
    sizes = [won_percentage, draw_percentage, lost_percentage]

    # Plot the pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title('Performance in Last 5 Years')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Show the pie chart
    st.pyplot(fig)

    st.header('Performance in Home Ground For Last 5 Season')
    matches_played_at_Home = df[df['Home_team_name'] == team].shape[0]
    st.write('Matches Played at Home-', matches_played_at_Home)
    data = df[(df['Home_team_name'] == team)]
    matches_won_at_Home = data[data['Winner'] == team].shape[0]
    st.write('Matches won at Home-', matches_won_at_Home)

    matches_draw_at_Home = data[data['Winner'] == 'Draw'].shape[0]
    st.write('Matches draw at Home-', matches_draw_at_Home)
    matches_lost_at_Home = matches_played_at_Home - (matches_draw_at_Home + matches_won_at_Home)
    st.write('Matches lost at Home-', matches_lost_at_Home)

    won_percentage = (matches_won_at_Home / matches_played_at_Home) * 100
    draw_percentage = (matches_draw_at_Home / matches_played_at_Home) * 100
    lost_percentage = (matches_lost_at_Home / matches_played_at_Home) * 100

    labels = ['Won', 'Draw', 'Lost']
    sizes = [won_percentage, draw_percentage, lost_percentage]

    # Plot the pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title('Performance at Home in Last 5 Years')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Show the pie chart
    st.pyplot(fig)

    st.header('Performance at Away Ground For Last 5 Season')
    matches_played_at_Away = df[df['Away_team_name'] == team].shape[0]
    data = df[(df['Away_team_name'] == team)]
    st.write('Macthes Played Away-',matches_played_at_Away)
    matches_won_at_Away = data[data['Winner'] == team].shape[0]
    st.write('Macthes won at Away-', matches_won_at_Away)
    matches_draw_at_Away = data[data['Winner'] == 'Draw'].shape[0]
    st.write('Macthes Draw Away-', matches_draw_at_Away)
    matches_lost_at_Away = matches_played_at_Away - (matches_draw_at_Away + matches_won_at_Away)
    st.write('Macthes Lost Away-', matches_lost_at_Away)

    won_percentage = (matches_won_at_Away / matches_played_at_Away) * 100
    draw_percentage = (matches_draw_at_Away / matches_played_at_Away) * 100
    lost_percentage = (matches_lost_at_Away / matches_played_at_Away) * 100

    labels = ['Won', 'Draw', 'Lost']
    sizes = [won_percentage, draw_percentage, lost_percentage]

    # Plot the pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title('Performance at Away in Last 5 Years')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Show the pie chart
    st.pyplot(fig)

    st.header('Goals Scored and Conceded per season')
    goal_scored_in_2018 = df_2018[df_2018['Team'] == team]['F'].values[0]
    goal_scored_in_2019 = df_2019[df_2019['Team'] == team]['F'].values[0]
    goal_scored_in_2020 = df_2020[df_2020['Team'] == team]['F'].values[0]
    goal_scored_in_2021 = df_2021[df_2021['Team'] == team]['F'].values[0]
    goal_scored_in_2022 = df_2022[df_2022['Team'] == team]['F'].values[0]

    goal_conceded_in_2018 = df_2018[df_2018['Team'] == team]['A'].values[0]
    goal_conceded_in_2019 = df_2019[df_2019['Team'] == team]['A'].values[0]
    goal_conceded_in_2020 = df_2020[df_2020['Team'] == team]['A'].values[0]
    goal_conceded_in_2021 = df_2021[df_2021['Team'] == team]['A'].values[0]
    goal_conceded_in_2022 = df_2022[df_2022['Team'] == team]['A'].values[0]

    total_goals_scored_in_last_5_years = goal_scored_in_2018 + goal_scored_in_2019 + goal_scored_in_2020 + goal_scored_in_2021 + goal_scored_in_2022
    total_goals_conceded_in_last_5_years = goal_conceded_in_2018 + goal_conceded_in_2019 + goal_conceded_in_2020 + goal_conceded_in_2021 + goal_conceded_in_2022

    st.write('Goals Scored in 2018-',goal_scored_in_2018,',  Goals conceded in 2018-',goal_conceded_in_2018)
    st.write('Goals Scored in 2019-', goal_scored_in_2019, ',  Goals conceded in 2019-', goal_conceded_in_2019)
    st.write('Goals Scored in 2020-', goal_scored_in_2020, ',  Goals conceded in 2020-', goal_conceded_in_2020)
    st.write('Goals Scored in 2021-', goal_scored_in_2021, ',  Goals conceded in 2021-', goal_conceded_in_2021)
    st.write('Goals Scored in 2022-', goal_scored_in_2022, ',  Goals conceded in 2022-', goal_conceded_in_2022)
    st.write('Total Goals scored in Last 5 years-',total_goals_scored_in_last_5_years,',  Total Goals conceded in Last 5 years-',total_goals_conceded_in_last_5_years)

    plotdata = pd.DataFrame({

        "Goal_Scored": [goal_scored_in_2018, goal_scored_in_2019, goal_scored_in_2020, goal_scored_in_2021,
                        goal_scored_in_2022],

        "Goal_Conceded": [goal_conceded_in_2018, goal_conceded_in_2019, goal_conceded_in_2020, goal_conceded_in_2021,
                          goal_conceded_in_2022],

    },

        index=['2018-19', '2019-20', '2020-21', '2021-22', '2022-23'])

    fig, ax = plt.subplots(figsize=(15, 8))
    plotdata.plot(kind="bar", ax=ax)
    for i in ax.containers:
        ax.bar_label(i)

    plt.title("Goals per Seasons")
    plt.xlabel("Seasons")
    plt.ylabel("Goals")

    # Display the bar chart in Streamlit
    st.pyplot(fig)

    percentage_2018 = (goal_scored_in_2018 / total_goals_scored_in_last_5_years) * 100
    percentage_2019 = (goal_scored_in_2019 / total_goals_scored_in_last_5_years) * 100
    percentage_2020 = (goal_scored_in_2020 / total_goals_scored_in_last_5_years) * 100
    percentage_2021 = (goal_scored_in_2021 / total_goals_scored_in_last_5_years) * 100
    percentage_2022 = (goal_scored_in_2022 / total_goals_scored_in_last_5_years) * 100

    labels = ['2018', '2019', '2020', '2021', '2022']
    sizes = [percentage_2018, percentage_2019, percentage_2020, percentage_2021, percentage_2022]

    # Plot the pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title('Goals Scored in last 5 Years')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Show the pie chart
    st.pyplot(fig)

    percentage_2018 = (goal_conceded_in_2018 / total_goals_conceded_in_last_5_years) * 100
    percentage_2019 = (goal_conceded_in_2019 / total_goals_conceded_in_last_5_years) * 100
    percentage_2020 = (goal_conceded_in_2020 / total_goals_conceded_in_last_5_years) * 100
    percentage_2021 = (goal_conceded_in_2021 / total_goals_conceded_in_last_5_years) * 100
    percentage_2022 = (goal_conceded_in_2022 / total_goals_conceded_in_last_5_years) * 100

    labels = ['2018', '2019', '2020', '2021', '2022']
    sizes = [percentage_2018, percentage_2019, percentage_2020, percentage_2021, percentage_2022]

    # Plot the pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title('Goals Conceded in last 5 Years')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Show the pie chart
    st.pyplot(fig)

    shot_pg_2018 = df_team_stats_2018[df_team_stats_2018['Team'] == team]['Shots pg'].values[0]
    shot_pg_2019 = df_team_stats_2019[df_team_stats_2019['Team'] == team]['Shots pg'].values[0]
    shot_pg_2020 = df_team_stats_2020[df_team_stats_2020['Team'] == team]['Shots pg'].values[0]
    shot_pg_2021 = df_team_stats_2021[df_team_stats_2021['Team'] == team]['Shots pg'].values[0]
    shot_pg_2022 = df_team_stats_2022[df_team_stats_2022['Team'] == team]['Shots pg'].values[0]

    st.header('Shots per Season')
    values = [shot_pg_2018, shot_pg_2019, shot_pg_2020, shot_pg_2021, shot_pg_2022]
    labels = ['2018', '2019', '2020', '2021', '2022']
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    for i in ax.containers:
        ax.bar_label(i)

    # Additional customization
    ax.set_xlabel('Season')
    ax.set_ylabel('Shots')
    ax.set_title('Shots per Season')

    # Display the bar chart in Streamlit
    st.pyplot(fig)

    st.header('Possession % per Season')
    possession_pg_2018 = df_team_stats_2018[df_team_stats_2018['Team'] == team]['Possession%'].values[0]
    possession_pg_2019 = df_team_stats_2019[df_team_stats_2019['Team'] == team]['Possession%'].values[0]
    possession_pg_2020 = df_team_stats_2020[df_team_stats_2020['Team'] == team]['Possession%'].values[0]
    possession_pg_2021 = df_team_stats_2021[df_team_stats_2021['Team'] == team]['Possession%'].values[0]
    possession_pg_2022 = df_team_stats_2022[df_team_stats_2022['Team'] == team]['Possession%'].values[0]

    values = [possession_pg_2018,possession_pg_2019,possession_pg_2020,possession_pg_2021,possession_pg_2022]
    labels = ['2018', '2019', '2020', '2021', '2022']
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    for i in ax.containers:
        ax.bar_label(i)

    # Additional customization
    ax.set_xlabel('Season')
    ax.set_ylabel('Possession % ')
    ax.set_title('Possession % per Season')

    # Display the bar chart in Streamlit
    st.pyplot(fig)

    st.header('Pass % per Season')
    pass_pg_2018 = df_team_stats_2018[df_team_stats_2018['Team'] == team]['Pass%'].values[0]
    pass_pg_2019 = df_team_stats_2019[df_team_stats_2019['Team'] == team]['Pass%'].values[0]
    pass_pg_2020 = df_team_stats_2020[df_team_stats_2020['Team'] == team]['Pass%'].values[0]
    pass_pg_2021 = df_team_stats_2021[df_team_stats_2021['Team'] == team]['Pass%'].values[0]
    pass_pg_2022 = df_team_stats_2022[df_team_stats_2022['Team'] == team]['Pass%'].values[0]

    values =[pass_pg_2018,pass_pg_2019,pass_pg_2020,pass_pg_2021,pass_pg_2022]
    labels = ['2018', '2019', '2020', '2021', '2022']
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    for i in ax.containers:
        ax.bar_label(i)

    # Additional customization
    ax.set_xlabel('Season')
    ax.set_ylabel('Pass % ')
    ax.set_title('Pass % per Season')

    # Display the bar chart in Streamlit
    st.pyplot(fig)



    st.header('Cards per Season')
    yellow_cards_2018 = card_df_2018[card_df_2018['TEAM'] == team]['YC'].values[0]
    yellow_cards_2019 = card_df_2019[card_df_2019['TEAM'] == team]['YC'].values[0]
    yellow_cards_2020 = card_df_2020[card_df_2020['TEAM'] == team]['YC'].values[0]
    yellow_cards_2021 = card_df_2021[card_df_2021['TEAM'] == team]['YC'].values[0]
    yellow_cards_2022 = card_df_2022[card_df_2022['TEAM'] == team]['YC'].values[0]

    red_cards_2018 = card_df_2018[card_df_2018['TEAM'] == team]['RC'].values[0]
    red_cards_2019 = card_df_2019[card_df_2019['TEAM'] == team]['RC'].values[0]
    red_cards_2020 = card_df_2020[card_df_2020['TEAM'] == team]['RC'].values[0]
    red_cards_2021 = card_df_2021[card_df_2021['TEAM'] == team]['RC'].values[0]
    red_cards_2022 = card_df_2022[card_df_2022['TEAM'] == team]['RC'].values[0]

    plotdata = pd.DataFrame({

        "Yellow Cards":[yellow_cards_2018,yellow_cards_2019,yellow_cards_2020,yellow_cards_2021,yellow_cards_2022],

        "Red Cards":[red_cards_2018,red_cards_2019,red_cards_2020,red_cards_2021,red_cards_2022],

    },

        index=['2018-19', '2019-20', '2020-21', '2021-22', '2022-23'])

    fig, ax = plt.subplots(figsize=(15, 8))
    plotdata.plot(kind="bar", ax=ax)
    for i in ax.containers:
        ax.bar_label(i)

    plt.title("Cards per Seasons")
    plt.xlabel("Seasons")
    plt.ylabel("Cards")

    # Display the bar chart in Streamlit
    st.pyplot(fig)

    st.header('Favourite and Nightmare Team')
    data = df[(df['Away_team_name'] == team) | (df['Home_team_name'] == team)]
    new = data[data['Winner'] == team]

    d = {}
    for i in common_teams:
        if i != team:
            me = new[(new['Home_team_name'] == i) | (new['Away_team_name'] == i)].shape[0]
            d[i] = me
    top_scorers = sorted(d.items(), key=lambda x: x[1], reverse=True)[:3]

    # Extract only the names from the result
    top_scorer_names = [name for name, _ in top_scorers]
    st.write('Most Matches won  against-',top_scorer_names[0],'  , ',top_scorer_names[1],'  , ',top_scorer_names[2])

    data = df[(df['Away_team_name'] == team) | (df['Home_team_name'] == team)]
    new = data[(data['Winner'] != team) & (data['Winner'] != 'Draw')]

    d = {}
    for i in common_teams:
        if i != team:
            me = new[(new['Home_team_name'] == i) | (new['Away_team_name'] == i)].shape[0]
            d[i] = me

    top_scorers = sorted(d.items(), key=lambda x: x[1], reverse=True)[:3]

    # Extract only the names from the result
    top_scorer_names = [name for name, _ in top_scorers]
    st.write('Most Matches lost against-',top_scorer_names[0],'  , ',top_scorer_names[1],'  , ',top_scorer_names[2])

    data = df[df['Home_team_name'] == team]
    new = data[data['Winner'] == team]

    d = {}
    for i in common_teams:
        if i != team:
            me = new[new['Away_team_name'] == i].shape[0]
            d[i] = me
    top_scorers = sorted(d.items(), key=lambda x: x[1], reverse=True)[:3]

    # Extract only the names from the result
    top_scorer_names = [name for name, _ in top_scorers]
    st.write('Most Home Matches won  against-',top_scorer_names[0],'  , ',top_scorer_names[1],'  , ',top_scorer_names[2])

    data = df[df['Home_team_name'] == team]
    new = data[(data['Winner'] != team) & (data['Winner'] != 'Draw')]

    d = {}
    for i in common_teams:
        if i != team:
            me = new[new['Away_team_name'] == i].shape[0]
            d[i] = me

    top_scorers = sorted(d.items(), key=lambda x: x[1], reverse=True)[:3]

    # Extract only the names from the result
    top_scorer_names = [name for name, _ in top_scorers]
    st.write('Most Home Matches Lost  against-',top_scorer_names[0],'  , ',top_scorer_names[1],'  , ',top_scorer_names[2])

    data = df[df['Away_team_name'] == team]
    new = data[data['Winner'] == team]

    d = {}
    for i in common_teams:
        if i != team:
            me = new[new['Home_team_name'] == i].shape[0]
            d[i] = me
    top_scorers = sorted(d.items(), key=lambda x: x[1], reverse=True)[:3]

    # Extract only the names from the result
    top_scorer_names = [name for name, _ in top_scorers]
    st.write('Most Away Matches Won  against-',top_scorer_names[0],'  , ',top_scorer_names[1],'  , ',top_scorer_names[2])

    data = df[df['Away_team_name'] == team]
    new = data[(data['Winner'] != team) & (data['Winner'] != 'Draw')]

    d = {}
    for i in common_teams:
        if i != team:
            me = new[new['Home_team_name'] == i].shape[0]
            d[i] = me

    top_scorers = sorted(d.items(), key=lambda x: x[1], reverse=True)[:3]

    # Extract only the names from the result
    top_scorer_names = [name for name, _ in top_scorers]
    st.write('Most Away Matches Lost  against-',top_scorer_names[0],'  , ',top_scorer_names[1],'  , ',top_scorer_names[2])

    st.header(f'Player Stats 2018-19 season for {team}')
    st.write(f"Top 3 goal scorer")
    data = player_df_2018[player_df_2018['Team'] == team][:3]
    st.table(data)
    st.write('Most Assist Given')
    data=player_assist_df_2018[player_assist_df_2018['Team']==team][0:3]
    st.table(data)

    st.header(f'Player Stats 2019-20 season for {team}')
    st.write(f"Top 3 goal scorer")
    data = player_df_2019[player_df_2019['Team'] == team][:3]
    st.table(data)
    st.write('Most Assist Given')
    data=player_assist_df_2019[player_assist_df_2019['Team']==team][0:3]
    st.table(data)

    st.header(f'Player Stats 2020-21 season for {team}')
    st.write(f"Top 3 goal scorer")
    data = player_df_2020[player_df_2020['Team'] == team][:3]
    st.table(data)
    st.write('Most Assist Given')
    data=player_assist_df_2020[player_assist_df_2020['Team']==team][0:3]
    st.table(data)

    st.header(f'Player Stats 2021-22 season for {team}')
    st.write(f"Top 3 goal scorer")
    data = player_df_2021[player_df_2021['Team'] == team][:3]
    st.table(data)
    st.write('Most Assist Given')
    data=player_assist_df_2021[player_assist_df_2021['Team']==team][0:3]
    st.table(data)

    st.header(f'Player Stats 2022-23 season for {team}')
    st.write(f"Top 3 goal scorer")
    data = player_df_2022[player_df_2022['Team'] == team][:3]
    st.table(data)
    st.write('Most Assist Given')
    data=player_assist_df_2022[player_assist_df_2022['Team']==team][0:3]
    st.table(data)

    st.header(f"Player stats of {team} for last 5 season")
    st.write('Most Goals Scored')
    data=merged_df[merged_df['Team']==team][:3]
    st.table(data)
    st.write('Most Assist Given')
    data=merged_assist_df[merged_assist_df['Team']==team][:3]
    st.table(data)














if st.button('Analyze'):
    analyze(team)
