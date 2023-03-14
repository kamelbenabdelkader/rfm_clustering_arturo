# Import libraries nécessaires
from dash import dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import streamlit as st
import plotly.express as px
from app import app


df = pd.read_csv("dataset/df_groupe.csv")



dropdown_col = ["Income","age",	"Montant", "NumDealsPurchases"]

droplist = html.Div(
    [
    dcc.Dropdown(dropdown_col,id="dropdown" ,clearable=False,  className="m-3",value="Income",),

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
        Output('graph', 'figure'),
        Input('dropdown', 'value'),
        # Output("graph", "figure"),
        # Input("names", "value"),
        # Input("values", "value")
    )

#--------------------------------Function------------------------------#
def update_output(value):
    graph = px.bar(df, x='Catégorie', y=value,color='Catégorie', text_auto='.0f')
    # graph.data[0].textinfo = 'label+text+value+percent parent'
    return graph


#--------------------------------Rows------------------------------#
row_graphs = dbc.Row(
    [
        row_dropdown,
        dbc.Col(""),
        dbc.Col(html.Div(dcc.Graph(id="graph")), width=12),
        dbc.Col(""),
    ],
)



layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("SEGMENTATION CLIENTS")),
        html.Br(),
        html.Hr(),
        row_graphs,

    ])
])
