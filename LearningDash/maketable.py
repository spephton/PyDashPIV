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
data = {'col1':[1, 2, 3], 'col2': [2, 3, 4], 'col3': [3, 4, 5]}
df = pd.DataFrame.from_records(data)




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
		columns=[{"name": i, "id": i} for i in df.columns],
		data = df.to_dict('records')
	)
])

## Callbacks
'''@app.callback(
	Output(componentidstring, componentproperty),
	Input(" "),
	State(" "),
)
def callbackFunction(var1, var2)
'''

if __name__ == '__main__':
	app.run_server(debug = True)