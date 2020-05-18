import base64
import datetime
import os
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from flask import Flask, send_from_directory
from urllib.parse import quote as urlquote
import pandas as pd
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
import plotly.express as px


data_plot = html.Div(id='waste_plot1')



row_1 = html.Div([data_plot], style={'width': '80%', 'margin-top': 5,  'margin-left': 200})



waste_layout = html.Div([row_1], className='main-container')
