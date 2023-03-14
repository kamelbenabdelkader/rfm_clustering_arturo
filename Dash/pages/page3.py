# Import libraries nécessaires
from dash import dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import streamlit as st
import plotly.express as px
from app import app


df = pd.read_csv("dataset/df_groupe.csv")

dropdown_col = ['NumWebPurchases' , 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth' ]

droplist = html.Div(
    [
    dcc.Dropdown(dropdown_col,id="dropdown_pie" ,clearable=False,  className="m-3",value="Income",),

    ]
)

output_container = html.Div()

row_dropdown = dbc.Container(
    [

        html.Label("Selection canal de consommation"),
        droplist,
        dcc.Loading(output_container),
    ],
    fluid=True,
)



#--------------------------------CallBack------------------------------#
@app.callback(
        Output('graphpie', 'figure'),
        Input('dropdown_pie', 'value'),
        # Output("graph", "figure"),
        # Input("names", "value"),
        # Input("values", "value")
    )

#--------------------------------Function------------------------------#
def update_output(value):
    graphpie = px.pie(df, values = value , names='Catégorie', title="Number of purchases made through the compan's web site by categories")
    return  graphpie


#--------------------------------Rows------------------------------#
row_graph_pie = dbc.Row(
    [
        row_dropdown,
        dbc.Col(""),
        dbc.Col(html.Div(dcc.Graph(id="graphpie")), width=12),
        dbc.Col(""),
    ],
)



layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("CANAL DE CONSOMMATION")),
        html.Br(),
        html.Hr(),
        row_graph_pie,

    ])
])
