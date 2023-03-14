# Import libraries nécessaires
from dash import dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import streamlit as st
import plotly.express as px
from app import app

df = pd.read_csv("dataset/df_groupe.csv")
#--------------------------------Variables------------------------------#
dropdown_col = ['NumWebPurchases','NumCatalogPurchases','NumStorePurchases','NumWebVisitsMonth']
refresh = html.A(html.Button('Refresh df'),href='/')

droplist = html.Div(
    [
    dcc.Dropdown(dropdown_col,id="dropdown" ,clearable=False,  className="m-3",value="NumWebPurchases",),

    ]
)

output_container = html.Div()

row_dropdown = dbc.Container(
    [

        html.Label("Selection de paramétres"),
        droplist,
        dcc.Loading(output_container),
    ],
    fluid=True,
)

#--------------------------------CallBack------------------------------#
@app.callback(
        Output('graphtree', 'figure'),
        Input('dropdown', 'value'),
        # Output("graph", "figure"),
        # Input("names", "value"),
        # Input("values", "value")
    )

#--------------------------------Function------------------------------#
def update_output(value):
    graphtree = px.treemap(df, path=['Catégorie',value])
    # graphtree.data[0].textinfo = 'label+text+value+percent parent'
    return graphtree


#--------------------------------Rows------------------------------#
row_graphs = dbc.Row(
    [
        row_dropdown,
        dbc.Col(""),
        dbc.Col(html.Div(dcc.Graph(id="graphtree")), width=12),
        dbc.Col(""),
    ],
)


#--------------------------------Layout------------------------------#

layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("Tree Map")),
        html.Br(),
        html.Hr(),
        row_graphs,
    ])
])
