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
