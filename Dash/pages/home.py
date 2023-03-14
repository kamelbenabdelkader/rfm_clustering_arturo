# Import libraries nécessaires
import dash
from dash import dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv("dataset/df_groupe.csv")
df['Recency'] = df['Recency']*-1


fig = px.bar(df, x='Catégorie', y=['Recency', 'Frequency', 'Montant'],text_auto=True)
fig.update_layout(title='Recency, Frequency, Monetary by Categories',
    xaxis = dict(showgrid=True),
    yaxis = dict(showgrid=True),
    legend = dict(orientation='v'),
    barmode='group', paper_bgcolor='#FFFFFF')


row_mean_graph2 = dbc.Row(
    [
        dbc.Col("", width=1),
        dbc.Col(dcc.Graph(figure=fig), width=10),
        dbc.Col("", width=1)
    ],
)


layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("RFM")),
        html.Br(),
        html.Hr(),
        row_mean_graph2



    ])
])
