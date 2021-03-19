# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_html_components as html
import pandas as pd
import certifi

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=11):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns]) # the table header contains a html.Tr (table row?), containing the table header (html.Th) of each column in df.columns
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows)) # post-block for loop? Have investigated (see forloo.py) -- the for loop applies when declared within a block, at the end of the block. If the line after the for loop deindents, it's treated as a post-declared for-loop and everything on the indent level of the declaration repeats (as opposed to a pre-declared loop, where everything one indent level in below the loop declaration repeats)
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
    