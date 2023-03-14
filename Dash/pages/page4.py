# Import libraries nécessaires
from dash import dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import streamlit as st
import plotly.express as px
from app import app


df = pd.read_csv("dataset/df_groupe.csv")

dropdown_col = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']

droplist = html.Div(
    [
    dcc.Dropdown(dropdown_col,id="dropdown_pie" ,clearable=False,  className="m-3",value="Income",),

    ]
)

output_container = html.Div()

row_dropdown = dbc.Container(
    [

        html.Label("Selection de type de produits"),
        droplist,
        dcc.Loading(output_container),
    ],
    fluid=True,
)



#--------------------------------CallBack------------------------------#
@app.callback(
        Output('graphpie2', 'figure'),
        Input('dropdown_pie', 'value'),
        # Output("graph", "figure"),
        # Input("names", "value"),
        # Input("values", "value")
    )

#--------------------------------Function------------------------------#
def update_output(value):
    graphpie2 = px.pie(df, values = value , names='Catégorie', title="Type de produits par catégories clients")
    return  graphpie2


#--------------------------------Rows------------------------------#
row_graph_pie = dbc.Row(
    [
        row_dropdown,
        dbc.Col(""),
        dbc.Col(html.Div(dcc.Graph(id="graphpie2")), width=12),
        dbc.Col(""),
    ],
)



layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("PRODUITS DE CONSOMMATION")),
        html.Br(),
        html.Hr(),
        row_graph_pie,

    ])
])
