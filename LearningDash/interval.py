# -*- coding: utf-8 -*-

# Run this app with `python thisfilename.py` and
# visit http://127.0.0.1:8050/ in your web browser.

## Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import numpy as np
from dash.dependencies import Input, Output, State

## Create dash app
app = dash.Dash(__name__)

## Layout
app.layout = html.Div([
    dcc.Interval(id='interval1', interval=5 * 1000, n_intervals=0),
    html.H1(id='label1', children='')
])


@app.callback(
	Output('label1', 'children'),
    Input('interval1', 'n_intervals')
)
def update_interval(n):
    return 'Intervals Passed: ' + str(n)

if __name__ == '__main__':
	app.run_server(debug = True)