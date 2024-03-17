import pandas as pd
import plotly.express as px
import uvicorn as uv
import fastapi as fa
from dash import Dash, dcc, html, callback, Output, Input
from utils import get_duration, draw_bar

df = pd.read_csv("/Users/tabitha/PycharmProjects/dataExploration/data/asian_drama_data/kor_drama.csv")
filter_by = ['drama_name', 'genres', 'director', 'sc_writer', 'tot_user_score', 'tot_watched', 'content_rt',
             'popularity', 'year', 'duration']

app = Dash(__name__)

app.layout = html.Div(
    children=[dcc.RadioItems(filter_by, 'duration', id='radioId', inline=True),
              dcc.Graph(id="graphId")]
)


@callback(
    Output("graphId", "figure"),
    Input("radioId", "value")
)
def update_graph(value):
    if value == "duration":
        df_duration = get_duration(df, "start_dt", "end_dt")
        df_duration = df_duration.head(20)
        fig = draw_bar(df_duration, "duration", "drama_name", "Drama by duration")
    elif value == "genres":
        df_comedy = df[df["genres"].str.contains('Comedy', na=False)]
        df_comedy = df_comedy.head(20)
        fig = draw_bar(df_comedy, "tot_user_score", "drama_name", "Drama by duration")
    else:
        df_comedy = df[df["genres"].str.contains('Comedy', na=False)]
        df_comedy = df_comedy.head(20)
        fig = draw_bar(df_comedy, "tot_user_score", "drama_name", "Drama by duration")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
