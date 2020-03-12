# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    className = 'body',
    style = {'width': '90%',
    'margin': 0,
    'font-family': 'Georgia'},
    children = [
    html.H1(
        className = "app-header",
        style = {'background-color': '#efefef',
        'padding': '10px',
        'text-align': 'center'},
        children = [
        html.Div('COVID-19 Outbreak Visualization Tool', className = "app-header--title")
        ]
        ),
    html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='3D Nucleocapsid Model', value='tab-1'),
        dcc.Tab(label='Global Tracking Map', value='tab-2'),
        dcc.Tab(label='Infections in the US', value='tab-3')
    ]),
    html.Div(id='tabs-content')
])
    ])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
            ])
            # html.Li(
            #     children = [
            #     html.Div('3D Nucleocapsid Viewer')
            #     ]),
            # html.Li(
            #     children = [
            #     html.Div('Global Tracking Map')
            #     ]),
            # html.Li(
            #     children = [
            #     html.Div('Infections in US')
            #     ])
        

if __name__ == '__main__' :
    app.run_server(debug=True)