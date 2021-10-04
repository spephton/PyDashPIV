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
app = dash.Dash(__name__, suppress_callback_exceptions=False)

## Functions
def swirlyfield(x, y):
	'''Generate array of vectors corresponding to points, for a vector field described by (u, v) = (r*sin(theta), -r*cos(theta)). (Cartesian input!)'''
	r = np.sqrt(x**2 + y**2)
	theta = np.arctan2(y, x)
	
	return r*np.sin(theta), -r*np.cos(theta)

def randomWithinDomain(xDomain, yDomain, nSamples):
	'''Generate array containing n uniformly randomly placed points within the 2d domain given. xDomain and yDomain are two-element lists specifying the minimum and maximum x and y values respectively'''
	xSourceValues = np.random.rand(nSamples)
	x = xSourceValues * (xDomain[1]-xDomain[0]) + xDomain[0]
	
	ySourceValues = np.random.rand(nSamples)
	y = ySourceValues * (yDomain[1] - yDomain[0]) +yDomain[0]
	
	return x, y

## Variables
nSamplesDefault = 121
nSamplesMax = 1000
domain = [[-3, 3], [-3, 3]]

linearResDefault = int(np.sqrt(nSamplesDefault))
x, y = np.meshgrid(np.linspace(*domain[0], linearResDefault), np.linspace(*domain[1], linearResDefault)) # New to me: the prefix "*" operator unpacks an array or list into the arguments of a function. In this case, when domain is defined earlier as "domain = [[-3, 3], [-3, 3]]", "linspace(*domain[0], 11)" unpacks to "linspace(-3, 3, 11)"
u, v = swirlyfield(x, y)
meshFig = ff.create_quiver(x, y, u, v)


## Layout
app.layout = html.Div([
	html.H1(
		children='Displaying Vector Fields in Plotly/Dash', style={
		'textAlign': 'center'
		}
	),
	html.Div(children='''
		Random point sampling vs grid sampling
		''', style={
		'textAlign': 'center'
		}
	),
	html.H2('Grid sampling'),
	dcc.Graph(
		id = 'meshgraph',
		figure = meshFig
	),
	html.H2('Random sampling'),
	dcc.Graph(
		id = 'randgraph'
	),
	html.Div([
		html.Div('Samples:\u205F', style={'width': 'text-width', 'display': 'inline-block'}),
		dcc.Input(value = '121', id = 'samplesInput', type = 'number', style={'width': '20%', 'display': 'inline-block'}),
		html.Button('Resample', id = 'resampleButton')
	])
])

## Callbacks
@app.callback(
	Output('randgraph', 'figure'),
	Input('resampleButton', 'n_clicks'),
	State('samplesInput', 'value'),
)
def callbackFunction(nclicks, samples):
	samples = int(samples)
	if samples <= 0 or samples > 1000:
		samples = nSamplesDefault
	samplePoints = randomWithinDomain(*domain, samples)
	velocities = swirlyfield(*samplePoints)
	randFig = ff.create_quiver(*samplePoints, *velocities)
	return randFig


if __name__ == '__main__':
	app.run_server(debug = True)