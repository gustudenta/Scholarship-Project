import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

pig_0 = html.Div([html.Img(src=app.get_asset_url('pp_title.png'), style={
                 'height': '30%', 'width': '82%', 'margin-top': 10})])    


pig_1 = html.Div([html.Img(src=app.get_asset_url('pp15.png'), style={
                'width': '40%', 'margin-top': 10})])   

text_section_0 = html.Div( dcc.Markdown('''

###### It is known that cancer is caused by changes to certain genes that alter the way our cells function. 
###### Some of these genetic changes occur naturally when DNA is replicated during the process of cell division. 
###### However, others are the result of environmental exposures that damage DNA. For example, 

'''))

pig_2 = html.Div([html.Img(src=app.get_asset_url('pp11.png'), style={
                'width': '70%', 'margin-top': 10})])    


text_section_1 = html.Div( dcc.Markdown('''

###### People can avoid some cancer-causing exposures, such as tobacco smoke and the sun’s rays. 
###### But other ones are harder to avoid, especially if they are in the air we breathe, the water we drink, the food we eat, or the materials we use to do our jobs.


###### An explosion of research has been done in discovering how human health is affected by environmental factors. 
###### In this project, I will discuss the relationship between cancer and the location of power plants and waste sites.

'''))

pig_3 = html.Div([html.Img(src=app.get_asset_url('pp122.png'), style={
                 'height': '30%', 'width': '29%', 'margin-top': 10, 'textAlign': 'center'})])  




text_section_2 = html.Div( dcc.Markdown('''

##### Will large number of power plants and waste sites lead to high cancer rate in a county?

###### An explosion of research has been done in discovering how human health is affected by environmental factors. 
###### In this project, I will discuss the relationship between cancer and the location of power plants and waste sites.

'''))



pig_5 = html.Div([html.Img(src=app.get_asset_url('pp14.png'), style={
                 'height': '30%', 'width': '40%', 'margin-top': 10, 'textAlign': 'center'})])  



text_section_3 = html.Div( dcc.Markdown('''

###### To solve this problem, three datasets are used: cancer rate in the U.S. by counnty, power plat information, NPL sites information.

###### This dashboard is created through Python Plotly Dash, to let users to discover the relationship among cancer, power plant locations and NPL site locations.

###### Users can choose visulization moduel to find which county has the largest amount of cancer cases and where power plants and NPL sites are.

###### Modeling moduel is used to show some advanced statistical methodology to do classifiication. 

###### In the modeling section, counties are splitted into three categories based on cancer rate: low, medium, and high. 

###### Logistic regression, random forest, and gradient boosting machine are applied to annalyze this question.
'''))

pig_6 = html.Div([html.Img(src=app.get_asset_url('powerplant_2.jpg'), style={
                 'height': '30%', 'width': '80%', 'margin-top': 10, 'textAlign': 'center'})])  



text_section_4 = html.Div( dcc.Markdown('''

###### All detailed coding files are saved on the github: https://github.com/gustudenta/Scholarship-Project
'''))



intro_layout = html.Div([pig_0, pig_1, text_section_0, pig_2, text_section_1, pig_3, text_section_2, pig_5,text_section_3, pig_6, text_section_4], style = {'width':'100%', 'margin-left':'15.5%', 'color': 'white'},
                         className = 'main-container')
