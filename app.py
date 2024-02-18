# classe que configura a aplicação

import dash
from flask import Flask


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = Flask(__name__)
app = dash.Dash(__name__, server=server, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets, update_title=None, meta_tags=[
    # A description of the app, used by e.g.
    # search engines when displaying search results.
    {
        'name': 'description',
        'content': 'Aplicação referente a Bancada de Refrigeração do LABRADS - Cear/UFPB.'
    },
    # A tag that tells Internet Explorer (IE)
    # to use the latest renderer version available
    # to that browser (e.g. Edge)
    {
        'http-equiv': 'X-UA-Compatible',
        'content': 'IE=edge'
    },
    # A tag that tells the browser not to scale
    # desktop widths to fit mobile screens.
    # Sets the width of the viewport (browser)
    # to the width of the device, and the zoom level
    # (initial scale) to 1.
    #
    # Necessary for "true" mobile support.
    {
      'name': 'viewport',
      'content': 'width=device-width, initial-scale=1.0'
    }
])





