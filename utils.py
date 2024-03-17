import pandas as pd
import plotly.express as px


def get_duration(df_orig, col_strt, col_end):
    df_orig[col_strt] = pd.to_datetime(df_orig[col_strt], format='mixed')
    df_orig[col_end] = pd.to_datetime(df_orig[col_end], format='mixed')
    df_orig["duration"] = df_orig[col_end] - df_orig[col_strt]
    return df_orig


def get_score(df_orig, indicator):
    if indicator == 'user_score':
        return df_orig[df_orig['tot_user_score'] == df_orig['tot_user_score'].max()]
    elif indicator == 'watched_time':
        return df_orig[df_orig['tot_watched'] == df_orig['tot_watched'].max()]


def draw_bar(df, y_str, x_str, title_str):
    fig = px.bar(df, y=y_str, x=x_str, title=title_str)
    return fig
