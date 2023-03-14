# Import libraries nécessaires
from dash import dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import streamlit as st
import plotly.express as px
from app import app


df = pd.read_csv("dataset/df_groupe.csv")

#--------------------------------Variables------------------------------#
fig1 = px.bar(df, x='Catégorie', y=['NumWebPurchases','NumCatalogPurchases','NumStorePurchases','NumWebVisitsMonth'],
    text_auto='.2f')
fig1.update_layout(title="Proportion des flux d'achat par Catégorie de clients",
    xaxis = dict(showgrid=True),
    yaxis = dict(showgrid=True),
    legend = dict(orientation='v'),
    barmode='stack', barnorm='percent', paper_bgcolor='#FFFFFF'
)

fig2= px.bar(df, x='Catégorie', y=['MntWines', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds'],text_auto='.2f' )
fig2.update_layout(title='Proportion des produits achetés par Catégorie de clients',
    xaxis = dict(showgrid=True),
    yaxis = dict(showgrid=True),
    legend = dict(orientation='v'),
    barmode='stack', barnorm='percent', paper_bgcolor='#FFFFFF'
)

#--------------------------------Rows------------------------------#
row_mean_graph1 = dbc.Row(
    [
        dbc.Col("", width=1),
        dbc.Col(dcc.Graph(figure=fig1), width=10),
        dbc.Col("", width=1),
    ],
)

row_mean_graph2 = dbc.Row(
    [
        dbc.Col("", width=1),
        dbc.Col(dcc.Graph(figure=fig2), width=10),
        dbc.Col("", width=1)
    ],
)




#--------------------------------Layout------------------------------#

layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("COMPORTANT D'ACHAT")),
        html.Br(),
        html.Hr(),
        row_mean_graph1,
        row_mean_graph2

    ])
])
