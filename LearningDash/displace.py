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
	
def displacePointsBy(points, function, time):
	'''Perturb points by a velocity field function over interval dt.
	
	Units must agree between points in 'Units', field function in 'Units/TimeInterval', time in 'TimeInterval'. Example: 'm', 'm/s', 's'. '''
	velocity = function(*points)
	# The following pattern is called 'list comprehension'. See footnote for more.
	perturbations = [vComponent * time for vComponent in velocity]
	listOfNewPoints = [points[i] + perturbations[i] for i in range(len(points))]
	updatedPoints = (*listOfNewPoints,) # turn it back into a tuple
	return updatedPoints


## Variables
domain = [[-3, 3], [-3, 3]]
samples = 121
points = randomWithinDomain(*domain, samples)
dt = 0.01

## Layout
app.layout = html.Div([
	html.H1(
		children='Displacing points in a vector field with Plotly/Dash', style={
		'textAlign': 'center'
		}
	),
	html.Div(children='''
		Loren ipsum dolor blurst of times
		''', style={
		'textAlign': 'center'
		}
	),
	dcc.Graph(id = 'points-plot'),
	html.Button(children = f'Advance {dt}s',id = 'displace-button')
])

## Callbacks
@app.callback(
	Output('points-plot', 'figure'),
	Input('displace-button','n_clicks'),
	State('points-plot', 'figure'),
)
def displacePoints(nClicks, existingFigure):
	global points
	points = displacePointsBy(points, swirlyfield, 0.1)
	figure = px.scatter(x = points[0], y = points[1])
	return figure


if __name__ == '__main__':
	app.run_server(debug = True)
	
'''>>> mylist = [x*x for x in range(3)] # list comprehension pattern


This: 

	listOfNewPoints = []
	for i in range(len(points)):
		listOfNewPoints.append(points[i] + perturbations[i])
	updatedPoints = (*listOfNewPoints,)

can be rewritten with list comprehension as: 

	listOfNewPoints = [points[i] + perturbations [i] for i in range(len(points))]
	updatedPoints = (*listOfNewPoints,)'''