import pandas as pd

df = pd.read_csv("/Users/tabitha/PycharmProjects/dataExploration/data/asian_drama_data/kor_drama.csv")
# find shape of data (rowsxcolumns):df.shape
# find column names of data :df.columns
# explored example data in key columns. df['genres']
# pulled subset of columns from df into a new df:
df_trimmed = df[['drama_name', 'genres', 'type', 'tot_user_score', 'tot_watched']]
# removed rows where genres = movie
df_trimmed = df_trimmed[df_trimmed['type'] == 'Drama']
df_trimmed.query()
# found max and min of user scores:
df_trimmed['tot_user_score'].max()
df_trimmed['tot_user_score'].min()
# created an array of unique values of tot_user_score
array1 = df_trimmed['tot_user_score'].unique()
# ADD comm
df_scored = df_trimmed[df_trimmed['tot_user_score'] == df_trimmed['tot_user_score'].max()]
df_tot_Watched = df_trimmed[df_trimmed['tot_watched'] == df_trimmed['tot_watched'].max()]
a = pd.concat([df_scored, df_tot_Watched])
# add com
df_comedy2 = df_trimmed[df_trimmed["genres"].str.contains('Comedy', na=False)]
# exploring date and time
df_duration = pd.read_csv("/Users/tabitha/PycharmProjects/dataExploration/data/asian_drama_data/kor_drama.csv")
# Converted str date column to datetime datatype
df_duration['start_dt'] = pd.to_datetime(df_duration['start_dt'], format='mixed')
df_duration['end_dt'] = pd.to_datetime(df_duration['end_dt'], format='mixed')
# created new column duration in df
df_duration["duration"] = df_duration["end_dt"] - df_duration["start_dt"]
