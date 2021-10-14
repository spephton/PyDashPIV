# -*- coding: utf-8 -*-

# Run this app with `python thisfilename.py` and
# visit http://127.0.0.1:8050/ in your web browser.

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


## Variables:
data = np.full((3,13), None)
data[:,0] = np.array(['subject signal', 'comparison signal', 'correlation'])
data[0:2,1:] = np.array([[1, 2, 2, 3, 3, 7, 4, 2, 3, 3, 1 ,3], 
						 [3, 3, 7, 4, 2, 3, 3, 1 ,3, 1, 0, 0]])
df = pd.DataFrame(data)




## Create dash app
app = dash.Dash(__name__)

## Layout
app.layout = html.Div([
	html.H1(
		children='Correlation', style={
		'textAlign': 'center'
		}
	),
	html.Div(children='''
		How does correlation work?
		''', style={
		'textAlign': 'center'
		}
	),
	dashtable.DataTable(
		id = 'correlation-table',
		columns = [{'name': str(i), 'id': str(i)} for i in df.columns],
#		data = df.to_dict('records')[:],
		css = [{
			'selector': 'tr:first-child',
			'rule': 'display: none',
		}],
	),
	html.Div([
		html.Button(
			id = 'left-button',
			children = 'left'
		),
	])
])

## Callbacks
@app.callback(
	Output('correlation-table', 'data'),
	Input('left-button', 'n_clicks'),
	State('correlation-table', 'data'),
)
def rollTopRow(n_clicks, data):
	if not data:
		return df.to_dict('records')
	
	new_df = pd.DataFrame.from_records(data)
	rows = new_df.to_numpy()
	rows[1] = np.roll(rows[1], 1)
	new_df = pd.DataFrame(rows)
	return new_df.to_dict('records')


if __name__ == '__main__':
	app.run_server(debug = True)