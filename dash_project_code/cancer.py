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



data_plot = html.Div(id='cancer_plot1')

row_1 = html.Div([data_plot], style={'width': '80%', 'margin-top': 5,  'margin-left': 200})

data_plot_2 = html.Div(id='cancer_plot2', style={'width': '47%', 'display': 'inline-block'})
data_plot_3 = html.Div(id='cancer_plot3', style={'width': '47%', 'display': 'inline-block', 'float':'right'})

row_2 = html.Div([data_plot_2, data_plot_3], style={'margin-top': 30,  'margin-left': 200, 'width': '80%'})

#map_2 =  html.Div(id='cancer_plot4')
#row_3 = html.Div([map_2], style={'width': '80%', 'margin-top': 30,  'margin-left': 200})


cancer_layout = html.Div([row_1, row_2, ], className='main-container')
