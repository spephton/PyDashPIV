import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dashtable
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
import numpy as np
from dash.dependencies import Input, Output, State



## Functions:
def gaussian(domain, mean, st_dev):
	return np.exp(-(domain - mean) ** 2 / (2 * st_dev ** 2))



## Constants:
DOMAIN = np.linspace(0, 5, 500)
INPUT_MEAN = 2.5
INPUT_ST_DEV = 0.1
INPUT_SIGNAL = gaussian(DOMAIN, INPUT_MEAN, INPUT_ST_DEV)
INPUT_SERIES = pd.Series(INPUT_SIGNAL, index = DOMAIN, name = 'Input Signal')




## Create dash app
app = dash.Dash(__name__)

## Layout
app.layout = html.Div([
	html.H1(
		children='Correlation'
	),
	html.Div(children='''
		1-D Correlation
		'''
	),
	html.Div(
		dcc.Graph(
			id = 'correlation-graph',
		),
		style = {'width': '80%',
				'margin-left': 'auto',
				'margin-right': 'auto',
				'margin-top': '10px',
				'margin-bottom': '10px'}
	),
	html.Div([
		html.Button(
			id = 'left-button',
			children = 'left'
		),
	])
],
style={
		'textAlign': 'center',
})

## Callbacks
@app.callback(
	Output('correlation-graph', 'figure'),
	Input('left-button', 'n_clicks'),
)
def translate_compare_signal(n_clicks):
	n_clicks = n_clicks or 0
	
	displace_step = 0.125 # how far should we displace the comparison signal each step.
	# Set to a divisor of 0.5 to ensure perfect correlation between input and comparison occurs
	comparison_mean = (1 + n_clicks * displace_step) % 5
	
	comparison_signal = gaussian(DOMAIN, comparison_mean, INPUT_ST_DEV)
	comp_series = pd.Series(comparison_signal, index = DOMAIN, name = 'Comparison Signal')
	
	df = pd.concat([INPUT_SERIES, comp_series], axis = 1)
	
	fig = px.line(df, df.index, y = ['Input Signal', 'Comparison Signal'])
	return fig

if __name__ == '__main__':
	app.run_server(debug = True)