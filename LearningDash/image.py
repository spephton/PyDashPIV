import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from skimage import data

img = data.chelsea()
red = np.array([255, 0, 0])
green = np.array([0, 255, 0])
blue = np.array([0, 0, 255])
white = np.array([255, 255, 255])
print(img.shape)
img[0][0] = white
img[0][-1] = red
img[-1][-1] = green
img[-1][0] = blue
# Hurray, now each corner shows a different colour! I'm image-editing!
# As expected, the origin is in the top-left, and the above code makes each corner white, red, green, and blue, clockwise from the origin. But on my screen you need pretty good eyes to see it :P
fig = px.imshow(img)
fig.update_layout(dragmode="drawrect")
config = {
    "modeBarButtonsToAdd": [
        "drawline",
        "drawopenpath",
        "drawclosedpath",
        "drawcircle",
        "drawrect",
        "eraseshape",
    ]
}

app = dash.Dash(__name__)
app.layout = html.Div(
    [html.H3("Drag and draw annotations"), dcc.Graph(figure=fig, config=config),]
)

if __name__ == "__main__":
    app.run_server(debug=True)