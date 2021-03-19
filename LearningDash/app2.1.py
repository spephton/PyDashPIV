# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
	'background': '#111111', # (very) dark grey
	'text': '#7FDBFF' # light turquoise. garish lol
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
}) # this is a python dict

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
	plot_bgcolor = colors['background'], 
	paper_bgcolor = colors['background'],
	font_color = colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
    	children='Hello Dash',
    	style={
    		'textAlign': 'center', # camelCased rather than dash-separated keys(like html)
    		'color': colors['text']
    	} # supplying a dictionary rather than a semicolon-separated string (as per html)
    	# also, refer to "className" when you want to refer to the "class" attribute
    ),

    html.Div(children='''
        Dash: A web application framework for Python.
    ''', style={
    	'textAlign': 'center',
    	'color': colors['text']
    }), 
    
    # in Python, triple quotes eliminate the need for escape coding within a string. Additionally, they allow multi-line strings. This lets us include newlines in an intuitively readable way

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    
    # What does this code do?
    # First, we define a pandas dataframe df containing our data: fruit, associated city, and quantity
    # Then we make a plotly express figure, "fig", containing a plot of the data frame, and tell plotly how to lay out this plot
    # Then we define our app layout as a div containing a list of elements: a heading, another div, and a dash core components graph of our figure "fig"