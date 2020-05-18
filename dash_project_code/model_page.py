import pandas as pd
import numpy as np
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots


Button_1 = html.Div([html.H2('Method',
                style={'font-size': '20px','color':'white', 'text_align': 'left', 'margin-top':30}),
                    html.Div(dcc.RadioItems(id = 'selection_model',
                                options=[
                                    {'label': ' All ', 'value': 'All'},
                                    {'label': ' Logistic ', 'value': 'LR'},
                                    {'label': ' RF ', 'value': 'RF'},
                                    {'label': ' GBM ', 'value': 'GBM'},
                                ],
                                value='All',
                                labelStyle={'font-style': 'inherit','color': 'white', 'font-size': '19px',  'font-weight': 'bold'}),
                                style={'display': 'inline-block'}),
                      html.Div([],style = {'width':'100%', 'margin-left':'15.5%', 'display': 'inline-block'}),

                      #html.Button('Run', id='signal_selection_analysis_button', style={'font-size': '20px', 'color':'black'}),
                      #html.Button('Result', id='signal_selection_check_button', style={'font-size': '20px', 'color':'black', 'display': 'inline-block', 'margin-left':25}),
                      #html.Button('Ranking', id='signal_selection_Driver_button', style={'font-size': '20px', 'color':'black', 'display': 'inline-block', 'margin-left':25}),
 
                                ],style={'margin-top':30, 'margin-bottom':30, 'margin-left':30})

#return_1 = html.Div(id ='signal_explor_run', style = {'width': '45%','display': 'inline-block', 'float': 'right','margin-top':52})
control = html.Div([Button_1], style={"border":"20px rgb(41, 62, 120) solid",
                                                                      'width':'32%', 'margin-left':'15%','display': 'inline-block',
                                                                      'border-radius': '5px'})

data_table = html.Div(id='data_table', style = {'display': 'inline-block', 'float': 'right'})

line_break = html.Div([], style={'width': '100%'})

row_1 = html.Div([control, data_table], style={'color':'continent', 'margin-top':30})

row_2 = html.Div(id ='model_plot',style={'color':'continent',  'margin-top':40})

#row_3 = html.Div(id ='signal_selection_drive',style={'color':'continent',  'margin-top':40})


model_page_layout = html.Div([row_1, line_break, row_2], className = 'main-container')
