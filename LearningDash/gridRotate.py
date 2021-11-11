## Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dashtable
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import numpy as np
from dash.dependencies import Input, Output, State


points = [(1, 0), (0, 1), (-1, 0)]
to_graph = list(zip(*points))

def gridular_rotate(point): 
    '''Given a point on a discrete 2d grid, rotate it 90 degrees clockwise about the origin'''
    return (-point[1], point[0])

## Create dash app
app = dash.Dash(__name__)

## Layout
app.layout = html.Div([
    html.H1(
        children='rotate this point on a grid!'
    ),
    html.Div(children='''
        rote ate rote ate?
        '''
    ),
    html.Div([
    dcc.Graph(
        figure = px.scatter(x = to_graph[0], y = to_graph[1]),
        id = 'graph'
    ),
    html.Button(children = 'rotorotoroto', id = 'yaya')
    ])
])


## Callbacks
@app.callback(
    Output('graph', 'figure'),
    Input('yaya', 'n_clicks'),
)
def rotatepoints(n_clicks):
    global points
    new_points = []
    for point in points:
        new_points.append(gridular_rotate(point))
    points = new_points
    to_graph = list(zip(*points))
    fig = px.scatter(x = to_graph[1], y = to_graph[0])
    return fig

if __name__ == '__main__':
    app.run_server(debug = True)