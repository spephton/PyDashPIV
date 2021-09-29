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
from dash.dependencies import Input, Output

## Create dash app
app = dash.Dash(__name__)

## Figures
x, y = np.meshgrid(np.linspace(-3, 3, 11), np.linspace(-3, 3, 11))
u = 0*x + 1
v = 0*x + 2

fig1 = ff.create_quiver(x, y, u, v)






## Layout
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
	),
	html.H2(children = 'Here is a vector field where the vector is constant'),
	dcc.Graph(
        id='figure1',
        figure=fig1
    ),
    html.H2(children = 'Here is a vector field where the vector varies with positon'),
	dcc.Graph(
        id='figure2',
    ),
    html.Label('Slide to adjust sampling resolution'),
    dcc.Slider(
    	id = 'f2resSlider',
    	min = 3,
    	max = 21,
    	#marks = {i: 'Label {}'.format(i) if i == 3 else str(i) for i in range(3, 6)},
    	marks = {i: str(i) for i in range(3, 21)},
    	value = 11,
    ),
    html.Div(
    	id = 'resolutionDescription',
    	children = 'nelekjlkrj',
	),
])

## Callbacks
@app.callback(
	Output(component_id = 'resolutionDescription', component_property = 'children'),
	Input(component_id = 'f2resSlider', component_property = 'value')
)
def updateResolutionDisplayed(input_value):
	return 'Default resolution: 11x11' if input_value == 11 else '{}x{}'.format(input_value, input_value)

@app.callback(
	Output('figure2', 'figure'),
	Input('f2resSlider', 'value'),
)
def updateFigure(resolution):
	x, y = np.meshgrid(np.linspace(-3, 3, resolution), np.linspace(-3, 3, resolution))
	u = 0*x + 1
	v = 0.5*y
	fig2 = ff.create_quiver(x, y, u, v)
	return fig2

if __name__ == '__main__':
	app.run_server(debug = True)