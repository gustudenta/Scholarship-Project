# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import requests
import plotly
import plotly.figure_factory as ff
from plotly.offline import *
from colour import Color
import dash_table
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from os import path
import warnings
import base64
import intro
import model_page
import cancer
import powerplant_page
import cancertrend
import plotly.express as px
import waste
from urllib.request import urlopen
import conclu
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


app = dash.Dash(__name__)
server = app.server

app.config['suppress_callback_exceptions'] = True
app.title = 'GU Analytics Scholarship Project'

colors = {
    'theme_color': 'rgb(7, 28, 68)',
    'theme_color_2': 'rgb(41, 62, 120)',
    'text': '#F0F8FF',
    'plot_color': '#41EEC8'

}
USERNAME_PASSWORD_PAIRS = [
    ['jingyu', '261025'],['user1', '001']
]

# read USA powerplant dataset

powerplant = pd.read_csv("powerplant_with_state.csv")


us_states  = list(powerplant.State.unique()) 
us_states.sort()
us_states = ['All'] + us_states

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 main tab layout
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

state_list= ['All', "Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

npl_element = html.Div(id='npl_drop')
powerplant_element = html.Div(id='power_drop')

sidebar = html.Div(
    [
        html.Div([html.Img(src=app.get_asset_url('gu_logo_2.png'), style={
                 'height': '100%', 'width': '100%', 'margin-top': 10})]),       

        html.Div([
            html.H2('Function', className='control_header'),             
            dcc.Dropdown(id='function_dropdown',
                         options=[
                                  {'label': 'Introduction',  'value': 'Introduction'},
                                  {'label': 'Visualization',  'value': 'Virtualization'},
                                  {'label': 'Modeling',  'value': 'Modeling'},
                                  {'label': 'Conclusion',  'value': 'Conclusion'},
                                  ],
                          value='Introduction',

                         style={'color': 'continent', 'margin-top': 20}
                         ),

            html.H2('Selection', className='control_header'),             
            dcc.Dropdown(id='sidebar_dropdown',
                         options=[
                                  {'label': 'Cancer Rate',  'value': 'CancerRate'},
                                  {'label': 'Power Plant Location', 'value': 'PowerPlant'}, 
                                  {'label': 'NPL Sites Location', 'value': 'WasteSites'}],
                        value='CancerRate',

                         style={'color': 'continent', 'margin-top': 20}
                         ),
            html.H2('State', className='control_header'),             
            dcc.Dropdown(id='state_id',
                         options=[ {'label': i, 'value': i} for i in state_list],
                         value='All',
                         clearable=False,
                         style={'color': 'continent', 'margin-top': 20}),

            powerplant_element,
            npl_element,
            

        ],
            className='main-container'),


    ],
    #style=SIDEBAR_STYLE,
    id="sidebar",
    className="sidebar"
)

@app.callback(Output('npl_drop', 'children'),
              [Input('sidebar_dropdown', 'value')])
def npl_content(sidebar_dropdown):
    nlp = html.Div(
            [
                html.Div([
                    html.H2('NPL Status', className='control_header'),             
                    dcc.Dropdown(id='NLP_drop',
                                options=[
                                        {'label': 'All',  'value': 'All'},                                    
                                        {'label': 'NPL Site',  'value': 'NPL Site'},
                                        {'label': 'Deleted NPL Site', 'value': 'Deleted NPL Site'}, 
                                        {'label': 'Proposed NPL Site', 'value': 'Proposed NPL Site'}],
                                value='All',
                                clearable=False,
                                style={'color': 'continent', 'margin-top': 20}
                                )


                ]),
            ])
    if sidebar_dropdown == 'WasteSites':
        npl_out = html.Div([nlp])
    else:
        npl_out = html.Div([nlp], style={'display':'none'})
    return [npl_out]

@app.callback(Output('power_drop', 'children'),
              [Input('sidebar_dropdown', 'value')])
def power_content(sidebar_dropdown):
    pl = html.Div(
            [
                html.Div([
                    html.H2('Primary Fuel', className='control_header'),             
                    dcc.Dropdown(id='power_drop_down',
                                options=[
                                        {'label': 'All',  'value': 'All'},                                    
                                        {'label': 'Solar',  'value': 'Solar'},                                    
                                        {'label': 'Gas',  'value': 'Gas'},
                                        {'label': 'Oil', 'value': 'Oil'},
                                        {'label': 'Hydro', 'value': 'Hydro'}, 
                                        {'label': 'Wind', 'value': 'Wind'}, 
                                        {'label': 'Coal', 'value': 'Coal'},
                                        {'label': 'Biomass', 'value': 'Biomass'},
                                        {'label': 'Waste', 'value': 'Waste'},
                                        {'label': 'Cogeneration', 'value': 'Cogeneration'},
                                        {'label': 'Storage', 'value': 'Storage'},
                                        {'label': 'Geothermal', 'value': 'Geothermal'},
                                        {'label': 'Nuclear', 'value': 'Nuclear'},
                                        {'label': 'Petcoke', 'value': 'Petcoke'},
                                        {'label': 'Other', 'value': 'Other'},
                                        ],
                                value='All',
                                clearable=False,
                                style={'color': 'continent', 'margin-top': 20}
                                )


                ]),
            ])
    if sidebar_dropdown == 'PowerPlant':
        pl_out = html.Div([pl])
    else:
        pl_out = html.Div([pl], style={'display':'none'})
    return [pl_out]


tab_element = html.Div(id='tabs-content')



app.layout = html.Div([sidebar, tab_element])


@app.callback(Output('tabs-content', 'children'),
              [Input('sidebar_dropdown', 'value'), 
              Input('function_dropdown', 'value')])
def render_content(tab, function_dropdown):
    
    if function_dropdown == 'Modeling':
        return model_page.model_page_layout
    elif function_dropdown == 'Introduction':
        return intro.intro_layout
    elif function_dropdown == 'Conclusion':
        return conclu.con_layout
    else:
        if tab == 'CancerRate':
            return cancer.cancer_layout
        elif tab == 'PowerPlant':
            return powerplant_page.powerplant_layout
        elif tab == 'WasteSites':
            return waste.waste_layout


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Callback Function for powerplant tab
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@app.callback(
    Output('power_plot1', 'children'),
    [Input('state_id', 'value'),
    Input('power_drop_down', 'value')])
def dataexplor_plot(State, power_drop):

    data = pd.read_csv("powerplant_with_state.csv")

    color_dict = {"Solar":"blue", "Gas":"red", "Oil":"orange", "Hydro":"navy", "Wind":"purple", "Coal":"yellow", 
              "Biomass":"black", "Waste":"grey", "Cogeneration":"green", "Storage":"pink", "Geothermal":"olive", 
              "Nuclear":"gold", "Petcoke":"lime", "Other":"hotpink"}

    if  State != 'All' and power_drop != "All":
        final_powerplant = data[data['State']==State]
        final_powerplant = final_powerplant[final_powerplant['primary_fuel'] == power_drop]
        c1 = [color_dict[power_drop]]

    elif State == 'All' and power_drop != "All":
        final_powerplant = data[data['primary_fuel'] == power_drop]
        c1 = [color_dict[power_drop]]

    elif State != 'All' and power_drop == "All":
        final_powerplant = data[data['State']==State]
        c1 = list(color_dict.values())
    else:
        final_powerplant = data
        c1 = list(color_dict.values())


     # draw powerplant location in USA

    if final_powerplant.empty:
        fig_powerplant_usa = px.scatter_mapbox(data, lat="latitude", lon="longitude", zoom=2.5, height = 480, width = 938, opacity = 0)
        fig_powerplant_usa.update_layout(hovermode=False)
    else:
        fig_powerplant_usa = px.scatter_mapbox(final_powerplant, lat="latitude", lon="longitude", 
                                            hover_name="name", hover_data=["latitude", "longitude", "State"],
                                            zoom=2.5,
                                            color_discrete_sequence = c1, color = "primary_fuel")



    fig_powerplant_usa.update_layout(title = "Power Plant Locations", 
                                    font = dict(family="Courier New, monospace",size=18,color="#7f7f7f"))
    fig_powerplant_usa.update_layout(mapbox_style="open-street-map")
    fig_powerplant_usa.update_layout(template='plotly_dark', paper_bgcolor='rgb(7, 28, 68)', )


        #except:
        #    return [html.Div([], className='dash-elem')]
    
    return [html.Div(dcc.Graph(id='plot1', figure=fig_powerplant_usa, 
                config={"displaylogo": False}, style = {'height': 500}), className='dash-elem')]
        


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Callback Function for cancer tab
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}


@app.callback(
    Output('cancer_plot1', 'children'),
    [Input('state_id', 'value')])
def dataexplor_plot(State):
    data = pd.read_csv("cancer_rate_usa_with_fips.csv")

    if  State != 'All':
        data = data[data['State Name']==us_state_abbrev[State]]

    # draw USA heatma
    fig = px.choropleth_mapbox(data, geojson=counties, locations='FIPS', color="Average Annual Count",
                           color_continuous_scale="Viridis",
                           range_color=(50, 2000),
                           mapbox_style='open-street-map',
                           zoom=2.5, 
                           center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'Average Annual Count':'Average Annual Count'},
                          )
    fig.update_layout(title =  "Average Annual Count in the U.S. by County", plot_bgcolor='rgb(10,10,10)',
                      font = dict(family="Courier New, monospace",size=18,color="#7f7f7f"))
    #fig.update_layout(mapbox_style="carto-darkmatter")
    #fig.layout.plot_bgcolor = '#fff'
    #fig.layout.paper_bgcolor = '#fff'
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgb(7, 28, 68)', )

        #except:
        #    return [html.Div([], className='dash-elem')]
    
    return [html.Div(dcc.Graph(id='plot1', figure=fig, 
                config={"displaylogo": False},  style = {'height': 500}), className='dash-elem')]
        

@app.callback(
    Output('cancer_plot2', 'children'),
    [Input('state_id', 'value')])
def dataexplor_plot_2(State):
    
    data = pd.read_csv("cancer_rate_usa_with_fips.csv")
    top10_cancerrate = data[['Average Annual Count', 'State Name']]
    
    #top10_cancerrate.head(10)
    if State == 'All':
        top10_cancerrate = top10_cancerrate.groupby('State Name', as_index=False).agg({"Average Annual Count": "sum"})
        top10_cancerrate = top10_cancerrate.sort_values(by=['Average Annual Count'], ascending=False)
        # top10_cancerrate
        fig = px.bar(top10_cancerrate[:10], x='State Name', y='Average Annual Count', title = "Top States with High Cancer Rate")

    else:
        state = data['State Name'] == us_state_abbrev[State]
        state_cancerrate = data[state]
        top10_state = state_cancerrate[['Average Annual Count', 'Name']]
        top10_state = top10_state.sort_values(by=['Average Annual Count'], ascending=False)
        fig = px.bar(top10_state[:10], x='Name', y='Average Annual Count', title = "Top Counties with High Cancer Rate")

    fig.update_layout(template='plotly_dark', 
                      plot_bgcolor='rgb(7, 28, 68)', paper_bgcolor='rgb(7, 28, 68)',
                      font = dict(family="Courier New, monospace",size=14,color="#7f7f7f"))
    #fig.update_layout(mapbox_style="carto-darkmatter")
    #fig.layout.plot_bgcolor = '#fff'
    #fig.layout.paper_bgcolor = '#fff'
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgb(7, 28, 68)', )

        #except:
        #    return [html.Div([], className='dash-elem')]
    
    return [html.Div(dcc.Graph(id='plot2', figure=fig, 
                config={"displaylogo": False}, style = {'height': 360}), className='dash-elem')]


@app.callback(
    Output('cancer_plot3', 'children'),
    [Input('state_id', 'value')])
def dataexplor_plot_3(State):
    cancer_data = pd.read_csv("cancer_rate_usa_with_fips.csv")
    if State == "All":
        trend = cancer_data[['FIPS','Recent Trend']]

        trend = trend.groupby('Recent Trend').count()
        trend = trend.reset_index()

        trend.columns = ['Recent Trend', 'Number of Counties']
        trend["Recent Trend"].replace({"*": "unknown"}, inplace=True)
    

        # top10_cancerrate
        fig =  px.pie(trend, values='Number of Counties', names='Recent Trend', title = "Pie Chart for Recent Trend")
        
    else:
        state = cancer_data['State Name'] == us_state_abbrev[State]
        state_cancerrate = cancer_data[state]

        trend_state = state_cancerrate[['FIPS','Recent Trend']]
        trend_state = trend_state.groupby('Recent Trend').count()
        trend_state = trend_state.reset_index()
        trend_state.columns = ['Recent Trend', 'Number of Counties']
        trend_state["Recent Trend"].replace({"*": "unknown"}, inplace=True) 
        fig = px.pie(trend_state, values='Number of Counties', names='Recent Trend', title = "Pie Chart for Recent Trend")


    fig.update_layout(template='plotly_dark', 
                      plot_bgcolor='rgb(7, 28, 68)', paper_bgcolor='rgb(7, 28, 68)',
                      font = dict(family="Courier New, monospace",size=14,color="#7f7f7f"))
    #fig.update_layout(mapbox_style="carto-darkmatter")
    #fig.layout.plot_bgcolor = '#fff'
    #fig.layout.paper_bgcolor = '#fff'
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgb(7, 28, 68)', )

        #except:
        #    return [html.Div([], className='dash-elem')]
    
    return [html.Div(dcc.Graph(id='plot3', figure=fig, 
                config={"displaylogo": False}, style = {'height': 360}), className='dash-elem')]


@app.callback(
    Output('cancer_plot4', 'children'),
    [Input('state_id', 'value')])
def dataexplor_plot_4(State):
    data = pd.read_csv("cancer_rate_usa_with_fips.csv")
    if  State != 'All':
        return []

    fig = px.choropleth_mapbox(data, geojson=counties, locations='FIPS', color="Recent Trend",
                            color_continuous_scale="Viridis",
                            range_color=(50, 2000),
                            mapbox_style="carto-positron",
                            zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                            opacity=0.5,
                            labels={'Average Annual Count':'Average Annual Count'}
                            )

    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    #fig.update_layout(mapbox_style="carto-darkmatter")
    #fig.layout.plot_bgcolor = '#fff'
    #fig.layout.paper_bgcolor = '#fff'
    fig.update_layout(template='plotly_dark', paper_bgcolor='rgb(7, 28, 68)', )

        #except:
        #    return [html.Div([], className='dash-elem')]
    
    return [html.Div(dcc.Graph(id='plot4', figure=fig, 
                config={"displaylogo": False},  style = {'height': 500}), className='dash-elem')]
        
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Callback Function for waste tab
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
@app.callback(
    Output('waste_plot1', 'children'),
    [Input('state_id', 'value'), 
    Input('NLP_drop', 'value')])
def dataexplor_plot(State, npl_drop):

    npl = pd.read_csv("Superfund National Priorities List (NPL) Sites with Status Information.csv")
    color_dict2 = {"NPL Site":"red", "Deleted NPL Site":"blue", "Proposed NPL Site":"black"}
    #c2 = color_dict2.values()
    #print(npl.Status)
    if  State != 'All' and npl_drop != "All":
        state_npl = npl[npl['State'] == State]
        final_npl = state_npl[state_npl.Status == npl_drop]
        c2 = [color_dict2[npl_drop]]
        #c2 = list(color_dict2.values())

    elif State == "All" and npl_drop != "All":
        final_npl = npl[npl.Status == npl_drop]
        c2 = [color_dict2[npl_drop]]
        #c2 = list(color_dict2.values())

    elif State != "All" and npl_drop == "All":
        final_npl = npl[npl['State'] == State]
        c2 = list(color_dict2.values())

    else:
        c2 = list(color_dict2.values())
        final_npl = npl


    if final_npl.empty:
        fig3 = px.scatter_mapbox(npl, lat="Latitude", lon="Longitude", zoom=2.5, height = 480, width = 938, opacity = 0)
        fig3.update_layout(hovermode=False)
    else:
        fig3 = px.scatter_mapbox(final_npl, lat="Latitude", lon="Longitude", hover_name="Site Name", 
                        hover_data=["State", "City", "County"],
                        color_discrete_sequence=c2, color = "Status",
                        zoom=2.5)




    

    # draw powerplant location in USA

    #fig3 = px.scatter_mapbox(final_npl, lat="Latitude", lon="Longitude", hover_name="Site Name", hover_data=["State", "City", "County"],
    #                    color_discrete_sequence=c2, color = "Status",
    #                    zoom=2.5, height = 480, width = 938)

    #fig3 = px.scatter_mapbox(npl, lat="Latitude", lon="Longitude", hover_name="Site Name", hover_data=["Latitude", "Longitude"],
                        #color_discrete_sequence=c2, 
     #                   zoom=2.5, height = 480, width = 938, color = "Status")
    #fig3.update_layout(mapbox_style="open-street-map")
    #fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    fig3.update_layout(title = "National Priorities List (NPL) Sites", 
                                    font = dict(family="Courier New, monospace",size=18,color="#7f7f7f"))
    fig3.update_layout(mapbox_style="open-street-map")
    fig3.update_layout(template='plotly_dark', paper_bgcolor='rgb(7, 28, 68)', )


        #except:
        #    return [html.Div([], className='dash-elem')]
    
    return [html.Div(dcc.Graph(id='plot1', figure=fig3, 
                config={"displaylogo": False}, style = {'height': 500}), className='dash-elem')]
        
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Callback Function for model tab
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""               

@app.callback(
    Output('data_table', 'children'),
    [ Input('selection_model', 'value')])
def model_table(selection_model):

    result_lr = pd.read_csv("result_lr.csv").round(3)
    result_rf = pd.read_csv("result_rf.csv").round(3)
    result_gbm = pd.read_csv("result_gbm.csv").round(3)
    model_rank = pd.read_csv("model_rank.csv").round(3)

    data_table_1 = html.Div([
           dash_table.DataTable(
               data=result_lr.to_dict('records'),
               columns=[{'id': c, 'name': c} for c in result_lr.columns],
               sort_action="native",
               #style_as_list_view=True,
               fixed_rows={'headers': True},
               fixed_columns={'headers': True, 'data': 1},

               style_header={'backgroundColor': 'rgb(41, 62, 120)'},
               style_cell={
                   'backgroundColor': colors['theme_color'],
                   'color': 'white',
                   'fontSize': 15,
                   'font-family': 'sans-serif',
                   'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'
               },

               style_data_conditional=[{
                   'if': {'column_id': 'Measure'},
                   'backgroundColor': 'rgb(41, 62, 120)',
                   'color': 'white',
               }],
               style_table={
                   #'maxHeight': '500',
                   #'overflowY': 'scroll',
                   'border': 'thin lightgrey solid',
               }
           )])

    data_table_2 = html.Div([
           dash_table.DataTable(
               data=result_rf.to_dict('records'),
               columns=[{'id': c, 'name': c} for c in result_rf.columns],
               sort_action="native",
               #style_as_list_view=True,
               fixed_rows={'headers': True},
               fixed_columns={'headers': True, 'data': 1},

               style_header={'backgroundColor': 'rgb(41, 62, 120)'},
               style_cell={
                   'backgroundColor': colors['theme_color'],
                   'color': 'white',
                   'fontSize': 15,
                   'font-family': 'sans-serif',
                   'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'
               },

               style_data_conditional=[{
                   'if': {'column_id': 'Measure'},
                   'backgroundColor': 'rgb(41, 62, 120)',
                   'color': 'white',
               }],
               style_table={
                   #'maxHeight': '500',
                   #'overflowY': 'scroll',
                   'border': 'thin lightgrey solid',
               }
           )])

    data_table_3 = html.Div([
           dash_table.DataTable(
               data=result_gbm.to_dict('records'),
               columns=[{'id': c, 'name': c} for c in result_gbm.columns],
               sort_action="native",
               #style_as_list_view=True,
               fixed_rows={'headers': True},
               fixed_columns={'headers': True, 'data': 1},

               style_header={'backgroundColor': 'rgb(41, 62, 120)'},
               style_cell={
                   'backgroundColor': colors['theme_color'],
                   'color': 'white',
                   'fontSize': 15,
                   'font-family': 'sans-serif',
                   'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'
               },

               style_data_conditional=[{
                   'if': {'column_id': 'Measure'},
                   'backgroundColor': 'rgb(41, 62, 120)',
                   'color': 'white',
               }],
               style_table={
                   #'maxHeight': '500',
                   #'overflowY': 'scroll',
                   'border': 'thin lightgrey solid',
               }
           )])

    data_table_4 = html.Div([
           dash_table.DataTable(
               data=model_rank.to_dict('records'),
               columns=[{'id': c, 'name': c} for c in model_rank.columns],
               sort_action="native",
               #style_as_list_view=True,
               fixed_rows={'headers': True},
               fixed_columns={'headers': True, 'data': 1},

               style_header={'backgroundColor': 'rgb(41, 62, 120)'},
               style_cell={
                   'backgroundColor': colors['theme_color'],
                   'color': 'white',
                   'fontSize': 15,
                   'font-family': 'sans-serif',
                   'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'
               },

               style_data_conditional=[{
                   'if': {'column_id': 'Model Rank'},
                   'backgroundColor': 'rgb(41, 62, 120)',
                   'color': 'white',
               }],
               style_table={
                   #'maxHeight': '500',
                   #'overflowY': 'scroll',
                   'border': 'thin lightgrey solid',
               }
           )])

    if selection_model == 'LR':
        return [data_table_1]
    elif selection_model == 'RF':
        return [data_table_2]
    elif selection_model == 'GBM':
        return [data_table_3]
    elif selection_model == 'All':
        return [data_table_4]   

@app.callback(
    Output('model_plot', 'children'),
    [ Input('selection_model', 'value')])
def model_ploy(selection_model):
    
    feature_importance_lr = pd.read_csv("feature_importance_lr.csv").round(3)

    fig_2 = go.Figure(data=[go.Pie(labels=feature_importance_lr.variable.map(lambda x: x.replace('_', '<br>')),
                                values=feature_importance_lr.percentage, hole=.5)])
    title = 'Logistic Regression Feature Importance %'
    # Change the bar mode
    fig_2.update_layout(title=title,template='plotly_dark', paper_bgcolor='rgb(7, 28, 68)')
    fig_2_div = html.Div(dcc.Graph(id='signal_selection_plot2', figure = fig_2, config={"displaylogo": False},
                                    style = {'height': 360}),
                                                style={'margin-top':40, 'width':'32%', 'margin-left':'15%',\
                                                       'display': 'inline-block'},
                                                className='dash-elem')
    fig_3 = go.Figure(data=[
            go.Bar(name='Corrletion', x=feature_importance_lr.variable,
                y=feature_importance_lr.scaled_importance),
        ])
    fig_3.update_layout(title='Logistic Regression Scaled Feature Importance',template='plotly_dark', 
                        paper_bgcolor='rgb(7, 28, 68)',
                        plot_bgcolor='rgb(7, 28, 68)')
    fig_3_div = html.Div(dcc.Graph(id='signal_selection_plot3', figure = fig_3, config={"displaylogo": False},
                         style = {'height': 360}),
                                                style = {'width': '38%','display': 'inline-block', 'float': 'right',\
                                                         'margin-top':40},
                                                className='dash-elem')

################################
    feature_importance_rf = pd.read_csv("feature_importance_rf.csv").round(3)

    fig_4 = go.Figure(data=[go.Pie(labels=feature_importance_rf.variable.map(lambda x: x.replace('_', '<br>')),
                                values=feature_importance_rf.percentage, hole=.5)])
    title = 'Random Forest Feature Importance %'
    # Change the bar mode
    fig_4.update_layout(title=title,template='plotly_dark', paper_bgcolor='rgb(7, 28, 68)')
    fig_4_div = html.Div(dcc.Graph(id='signal_selection_plot2', figure = fig_4, config={"displaylogo": False},
                                    style = {'height': 360}),
                                                style={'margin-top':40, 'width':'32%', 'margin-left':'15%',\
                                                       'display': 'inline-block'},
                                                className='dash-elem')
    fig_5 = go.Figure(data=[
            go.Bar(name='Corrletion', x=feature_importance_rf.variable,
                y=feature_importance_rf.scaled_importance),
        ])
    fig_5.update_layout(title='Random Forest Scaled Feature Importance',template='plotly_dark', 
                        paper_bgcolor='rgb(7, 28, 68)',
                        plot_bgcolor='rgb(7, 28, 68)')
    fig_5_div = html.Div(dcc.Graph(id='signal_selection_plot3', figure = fig_5, config={"displaylogo": False},
                         style = {'height': 360}),
                                                style = {'width': '38%','display': 'inline-block', 'float': 'right',\
                                                         'margin-top':40},
                                                className='dash-elem')

###########################
    feature_importance_gbm = pd.read_csv("feature_importance_gbm.csv").round(3)

    fig_6 = go.Figure(data=[go.Pie(labels=feature_importance_gbm.variable.map(lambda x: x.replace('_', '<br>')),
                                values=feature_importance_gbm.percentage, hole=.5)])
    title = 'GBM Feature Importance %'
    # Change the bar mode
    fig_6.update_layout(title=title,template='plotly_dark', paper_bgcolor='rgb(7, 28, 68)')
    fig_6_div = html.Div(dcc.Graph(id='signal_selection_plot2', figure = fig_6, config={"displaylogo": False},
                                    style = {'height': 360}),
                                                style={'margin-top':40, 'width':'32%', 'margin-left':'15%',\
                                                       'display': 'inline-block'},
                                                className='dash-elem')
    fig_7 = go.Figure(data=[
            go.Bar(name='Corrletion', x=feature_importance_gbm.variable,
                y=feature_importance_gbm.scaled_importance),
        ])
    fig_7.update_layout(title='GBM Scaled Feature Importance',template='plotly_dark', 
                        paper_bgcolor='rgb(7, 28, 68)',
                        plot_bgcolor='rgb(7, 28, 68)')
    fig_7_div = html.Div(dcc.Graph(id='signal_selection_plot3', figure = fig_7, config={"displaylogo": False},
                         style = {'height': 360}),
                                                style = {'width': '38%','display': 'inline-block', 'float': 'right',\
                                                         'margin-top':40},
                                                className='dash-elem')

    if selection_model == 'LR':
        return [fig_2_div, fig_3_div]
    if selection_model == 'RF':
        return [fig_4_div, fig_5_div]
    if selection_model == 'GBM':
        return [fig_6_div, fig_7_div]
    
    if selection_model == 'All':
        return [fig_2_div, fig_3_div, fig_4_div, fig_5_div, fig_6_div, fig_7_div]

if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    app.run_server(debug=True,  port=8080)
