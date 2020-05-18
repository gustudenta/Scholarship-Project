import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

pig_0 = html.Div([html.Img(src=app.get_asset_url('p9.jpg'), style={
                 'height': '30%', 'width': '77%', 'margin-top': 10})])    



text_section_1 = html.Div( dcc.Markdown('''

### Conclusion

###### Through visulization and modeling, it is found that the number of NPL sites and power plants will affect cancer rate.

###### First, in visulization section, it is easy to notice that Californina state has the highest number of cancer cases.
###### However, based on the pie chart, 67.2% of counties in California has failing trend. Why?
###### By looking at the NPL sites in California, it is noticed that there are a lot of deleted NPL sites, and only 2 proposed NPL sites.

###### Florida is also a good example that showing deleting NPL sites may help stop cancer rate rising. 
###### Florida is the second highest cancer rate state inn the U.S., but 86.6% of counties have stable cancer rate trend.
###### It is also nonticed that there are many deleted NPL sites and only 1 proposed NPL site.

###### Overall, there are more deleted NPL sites than proposed NPL sites, especially in those states with high cancer rates.

'''))  

pig_1 = html.Div([html.Img(src=app.get_asset_url('p8.jpg'), style={
                 'height': '30%', 'width': '77%', 'margin-top': 10})])  

text_section_2 = html.Div( dcc.Markdown('''

###### Secondly, from modeling perspective, the cancer rate of one county can be classfied based on these features:

* ###### *Age adjusted cancer cases*

* ###### *Confidence interval of cancer cases*

* ###### *Number of power plants*

* ###### *Number of NPL sites*
 
###### Additionally, based on random forest and gradient boosting machine models, number of NPL sites is an important feature.

###### In logistic regression model, the coefficients of the number of NPL sites and the number of power plants are positive.

###### This means as the number of power plants and NPL siites increases, the county has a higher probability to have higher cancer rate.

###### Also in the logistic regression model, the coefficient of the number of NPL sites is larger than the coefficient of power plant amount.

###### Therefore, comparing with power plants, NPL sites may lead to more negative environmental effect and cause higher cancer rate.



'''))  

pig_2 = html.Div([html.Img(src=app.get_asset_url('p4.jpg'), style={
                 'height': '30%', 'width': '77%', 'margin-top': 10})])   



con_layout = html.Div([pig_2, text_section_1, pig_1, text_section_2, pig_0], style = {'width':'100%', 'margin-left':'15.5%', 'color': 'white'},
                         className = 'main-container')
