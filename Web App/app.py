# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    className = 'body',
    children = [
    html.H1(
        className = "app-header",
        children = [
        html.Div('COVID-19 Outbreak Visualization Tool', className = "app-header--title")
        ]
        ),
    html.Div(
        className = "nav",
        children = html.Ul([
            html.Li(
                className = "li",
                children = [
                html.Div('Home'), 
                html.Div('3D Nucleocapsid Viewer'),
                html.Div('Global Tracking Map'),
                html.Div('Infections in US')
                ]),
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
            ]) )])



if __name__ == '__main__' :
    app.run_server(debug=True)