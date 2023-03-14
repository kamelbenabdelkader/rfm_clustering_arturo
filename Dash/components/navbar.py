# Import libraries nécessaires
from dash import html
import dash_bootstrap_components as dbc


# On defini ici la structure de la navbar
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Clusters", href="/page1")),
                dbc.NavItem(dbc.NavLink("Comportement", href="/page2")),
                dbc.NavItem(dbc.NavLink("Canal", href="/page3")),
                dbc.NavItem(dbc.NavLink("Produits", href="/page4"))
            ] ,
            brand="Markenting Campagne",
            brand_href="/",
            color="dark",
            dark=True,
        ),
    ])

    return layout
