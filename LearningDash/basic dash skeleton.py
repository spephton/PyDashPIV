# -*- coding: utf-8 -*-

# Run this app with `python thisfilename.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
	html.H1(
		children='Displaying Vector Fields in Plotly/Dash', style={
		'textAlign': 'center'
		}
	),
	html.Div(children='''
		Use quiver plots
		''', style={
		'textAlign': 'center'
		}
	)
])

if __name__ == '__main__':
	app.run_server(debug = True)