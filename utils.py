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
    label = {y_str: ' '.join(y_str.split('_')), x_str: ' '.join(x_str.split('_'))}
    fig = px.bar(df, y=y_str, x=x_str, title=title_str, color='tot_watched', labels=label)
    return fig


def draw_bar_genres(df, selected_genres):
    df_genres = df[df["genres"].str.contains(selected_genres, na=False)]
    df_genres = df_genres.sort_values("tot_user_score", ascending=False)
    # print(df_genres)
    df_genres = df_genres.head(30)
    print(f'selected_genres: {selected_genres}')
    print(f'\tdf: {df_genres["drama_name"]}')
    fig = draw_bar(df_genres, "tot_user_score", "drama_name", "Scores by users")
    return fig

