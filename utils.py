import ast

import pandas as pd
import plotly.express as px


def get_duration(df_orig, col_strt, col_end):
    df_orig[col_strt] = pd.to_datetime(df_orig[col_strt], format='mixed')
    df_orig[col_end] = pd.to_datetime(df_orig[col_end], format='mixed')
    df_orig['duration'] = df_orig[col_end] - df_orig[col_strt]
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


def draw_bar_year(df, selected_year):
    df_years = df[df['year'] == selected_year]
    df_years = df_years.sort_values('tot_user_score', ascending=False)
    df_years = df_years.head(30)
    fig = draw_bar(df_years, 'tot_user_score', 'drama_name', f'Highest scored dramas of {selected_year}')
    return fig


def draw_icicle_year(df, selected_year):
    df_years = df[df['year'] == selected_year].dropna()
    df_years['hi_low'] = df_years['tot_user_score'] < df_years['tot_user_score'].median()
    df_years['hi_low'] = df_years['hi_low'].replace(True, 'low rated').replace(False, 'high rated')
    df_years['org_net'] = df_years['org_net'].where(~df_years['org_net'].str.contains('Netflix'), 'Netflix')
    df_years['org_net'] = df_years['org_net'].where(~df_years['org_net'].str.contains('Amazon'), 'Amazon')
    df_years['org_net'] = df_years['org_net'].where(~df_years['org_net'].str.contains('SBS'), 'SBS')
    df_years['org_net'] = df_years['org_net'].where(~df_years['org_net'].str.contains('Naver'), 'Naver')
    df_years['org_net'] = df_years['org_net'].where(~df_years['org_net'].str.contains('Daum'), 'Daum')
    df_years['org_net'] = df_years['org_net'].where(~df_years['org_net'].str.contains('KBS'), 'KBS')
    df_years['org_net'] = df_years['org_net'].where(~df_years['org_net'].str.contains('MBC'), 'MBC')
    df_years['org_net'] = df_years['org_net'].where(~df_years['org_net'].str.contains('Disney'), 'Disney')
    df_years['org_net'] = df_years['org_net'].where(~df_years['org_net'].str.contains('Hulu'), 'Hulu')
    df_years['org_net'] = df_years['org_net'].where(~df_years['org_net'].str.contains('jTBC'), 'jTBC')
    df_years['org_net'] = df_years['org_net'].where(~df_years['org_net'].str.contains('TVING'), 'TVING')
    df_years['org_net'] = df_years['org_net'].where(~df_years['org_net'].str.contains('ENA'), 'ENA')
    df_years['org_net'] = df_years['org_net'].where(~df_years['org_net'].str.contains('tvN'), 'tvN')
    df_years = df_years.sort_values('popularity', ascending=False)
    # df_years = df_years.head(40)
    fig = px.icicle(df_years, path=[px.Constant(selected_year), 'hi_low', 'org_net', 'content_rt', 'drama_name'], values='tot_user_score')
    fig.update_traces(root_color='lightgrey')
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    return fig


def draw_bar_genres(df, selected_genres):
    df_genres = df[df['genres'].str.contains(selected_genres, na=False)]
    df_genres = df_genres.sort_values('tot_user_score', ascending=False)
    # print(df_genres)
    df_genres = df_genres.head(30)
    print(f'selected_genres: {selected_genres}')
    print(f'\tdf: {df_genres["drama_name"]}')
    fig = draw_bar(df_genres, 'tot_user_score', 'drama_name', 'Scores by users')
    return fig


def draw_bar_director(df, selected_director):
    df_director = df[df['director'].str.contains(selected_director, na=False)]
    df_director = df_director.sort_values('popularity', ascending=False)
    df_director = df_director.head(30)
    fig = draw_bar(df_director, 'popularity', 'drama_name', f'Dramas by {selected_director}')
    return fig


def draw_bar_sc_writer(df, selected_sc_writer):
    df_sc_wr = df[df['sc_writer'].str.contains(selected_sc_writer, na=False)]
    df_sc_wr = df_sc_wr.sort_values('popularity', ascending=False)
    df_sc_wr = df_sc_wr.head(30)
    fig = draw_bar(df_sc_wr, 'popularity', 'drama_name', f'Dramas by {selected_sc_writer}')
    return fig