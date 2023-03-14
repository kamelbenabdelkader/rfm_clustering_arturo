# Import necessary libraries
from dash import html, dcc
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app

# Connect to your app pages
from pages import home, page1, page2, page3,  page4

# Connect the navbar to the index
from components import navbar

# define the navbar
nav = navbar.Navbar()



# Define the index page layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content', children=[]),
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    if pathname == '/page1':
        return page1.layout
    if pathname == '/page2':
        return page2.layout
    if pathname == '/page3':
        return page3.layout
    if pathname == '/page4':
        return page4.layout
    else:
        return "404 Page Error! Please choose a link"

# Run the app on localhost:8050
if __name__ == '__main__':
    app.run_server(debug=True)


# st.title("Title")
# categories_count = df['Catégorie'].unique().tolist()

# chosen_count = st.sidebar.selectbox(
#    'Cluster de client ? ',
#    categories_count
# )


# df_filtered = df[df["Catégorie."] == chosen_count]
# df_plot = pd.DataFrame({'sum': [df_filtered.NumWebPurchases.sum(), df_filtered.NumCatalogPurchases.sum(), df_filtered.NumStorePurchases.sum()],},
#                   index=['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases'])

# fig3 = fig = px.pie(df_plot, values='sum', names=df_plot.index,title=f'Repatition des achat des {chosen_count} ')
# boxplot_chart = st.plotly_chart(fig3)


# fig = px.bar(df, x='Catégorie', y='Income',color='Catégorie')
# # fig.show(renderer="iframe")

# fig2 = px.bar(df, x='Catégorie', y='age',color='Catégorie')

# row_fig = dbc.Row(
#     [
#         dbc.Col("", width=1),
#         dbc.Col(dcc.Graph(figure=fig, id="g"), width=10),
#         dbc.Col("", width=1),
#     ],
# )

# row_fig1 = dbc.Row(
#     [
#         dbc.Col("", width=1),
#         dbc.Col(dcc.Graph(figure=fig2, id="t"), width=10),
#         dbc.Col("", width=1),
#     ],
# )


# st.title("Title")
# categories_count = df.Catégorie.unique().tolist()

# chosen_count = st.sidebar.selectbox(
#    'Cluster de client ? ',
#    categories_count
# )


# df_filtered = df[df["Catégorie."] == chosen_count]
# df_plot = pd.DataFrame({'sum': [df_filtered.NumWebPurchases.sum(), df_filtered.NumCatalogPurchases.sum(), df_filtered.NumStorePurchases.sum()],},
#                   index=['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases'])

# fig3 = fig = px.pie(df_plot, values='sum', names=df_plot.index,title=f'Repatition des achat des {chosen_count} ')
# boxplot_chart = st.plotly_chart(fig3)
