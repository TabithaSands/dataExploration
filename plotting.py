import ast

import pandas as pd
import plotly.express as px
import uvicorn as uv
import fastapi as fa
from dash import Dash, dcc, html, callback, Output, Input
from utils import *

df = pd.read_csv("/Users/tabitha/PycharmProjects/dataExploration/data/asian_drama_data/kor_drama.csv")
filter_by = ['drama_name', 'genres', 'director', 'sc_writer', 'tot_user_score', 'tot_watched', 'content_rt',
             'popularity', 'year', 'duration']
# create genres clean set
gen_series = df["genres"].dropna()
gen_list = gen_series.to_list()
split_list = []
for i in gen_list:
    try:
        for j in i.split(","):
            split_list.append(j)
    except Exception as e:
        print(f'Culprit: {i}, E: {e}')
set_clean = set(split_list)
no_spaces = []
for s in set_clean:
    no_spaces.append(s.strip())
no_spaces = list(set(no_spaces))
# create cleaned director set
series_director = df['director'].dropna()
list_director = []
for i in series_director:
    for item in ast.literal_eval(i):
        list_director.append(item)
list_director = list(set(list_director))
# get unique sc_writers
series_sc = df['sc_writer'].dropna()
list_sc = []
for i in series_sc:
    for item in ast.literal_eval(i):
        list_sc.append(item)
list_sc = list(set(list_sc))


app = Dash(__name__)

app.layout = html.Div(
                children=[
                            dcc.RadioItems(filter_by, 'duration', id='radioId', inline=True),
                            dcc.Dropdown(id="dropdownId", value=''),
                            dcc.Graph(id="graphId")
                        ]
                    )
@callback(
    [Output("graphId", "figure"), Output("dropdownId", "options")],
    [Input("radioId", "value"), Input("dropdownId", "value")]
)
def dropdown_update(value, dd_value):
    # print(f'dd_value: {dd_value}')
    if value != "genres":
        if value == "duration":
            df_duration = get_duration(df, "start_dt", "end_dt")
            df_duration = df_duration.head(30)
            fig = draw_bar(df_duration, "duration", "drama_name", "Drama by duration")
            return [fig, ['']]
        elif value == 'director':
            fig = draw_bar_director(df, dd_value)
            return [fig, list_director]
        elif value == 'sc_writer':
            fig = draw_bar_sc_writer(df, dd_value)
            return [fig, list_sc]
        else:
            df_comedy = df[df["genres"].str.contains('Comedy', na=False)]
            df_comedy = df_comedy.head(30)
            fig = draw_bar(df_comedy, "tot_user_score", "drama_name", "Drama by duration")
            return [fig, ['']]
    else:
        fig = draw_bar_genres(df, dd_value)
        return [fig, no_spaces]


if __name__ == "__main__":
    app.run(debug=True)
