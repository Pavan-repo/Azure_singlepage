import dash
import flask
import dash_bootstrap_components as dbc
import os
from dash import html, dcc
import dash_dangerously_set_inner_html as ddsih
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

import warnings
import pandas as pd 
pd.set_option("display.max_columns", 100)
warnings.filterwarnings("ignore")

from helpers.layout_utils import *
from helpers.create_azure_ticket import create_azure_issue

### SERVER ###
server = flask.Flask(__name__)

app = dash.Dash(
    __name__,
    server=server,
    title="T-Req's",
    update_title="T-Req's is working",
    serve_locally=True,
    prevent_initial_callbacks=False,
    routes_pathname_prefix="/Treq/",
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

app_server = app.server

base_layout = html.Div(
    [
        get_login_header(),
        get_logo_header(),
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content', style=base_div_style),
        dcc.Store(id="currentpage_store", storage_type="session"),
    ],
    style=CONTAINER_STYLE,
)

def layout_azure_landing():
    return dbc.Container(
    [
        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                        ddsih.DangerouslySetInnerHTML(
                                """<span style="color: rgb(0,83,159)"><b>Submit your ticket details here!</b></span>"""   
                        ),
                        style={
                            "font-size": 49,
                            "textAlign": "center",
                            "whiteSpace": "pre-wrap",
                        },   
                        ),
                    ],width="auto",
                ),
            ],justify="center",
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        
        
        dbc.Row(
            [
                dbc.Col(html.Label('Title' ,style={'font-weight': 'bold', 'font-size': '20px'}), width=7),
                dbc.Col(dbc.Input( id = 'title',
                                    type='text',
                                    placeholder = 'Enter title',
                                    className = 'input-text',
                            
                                    style = {
                                        
                                        'width':'700px',
                                        'height':"55px",
                                        'padding':"10px",
                                        "font-size":"16px",
                                        "border-width":"1px",
                                        
                                    }
                                    ),
                         width=7 
                        ), 
            ], 
            justify="center",
        ),
        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(html.Label('Description',  style={'font-weight': 'bold', 'font-size': '20px'}), width=7),
                dbc.Col(dbc.Textarea(id = 'description',
                                     placeholder = 'Enter description',
                                     className = 'input-text',
                                     
                                    style = {
                                        
                                        'width':'700px',
                                        'height':"75px",
                                        'padding':"10px",
                                        "font-size":"16px",
                                        "border-width":"1px",
                                        
                                    }
                                     )
                        ,width=7)
             ], 
             justify="center",
        ),
        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(html.Label('Anforderer' ,style={'font-weight': 'bold', 'font-size': '20px'}), width=7),
                dbc.Col(dbc.Input( id = 'anforderer',
                                    type='text',
                                    placeholder = 'Enter your name',
                                    className = 'input-text',
                                    
                                    style = {
                                        
                                        'width':'700px',
                                        'height':"45px",
                                        'padding':"10px",
                                        "font-size":"16px",
                                        "border-width":"1px",
                                        
                                    }
                                    ),
                         width=7 
                        ), 
            ], 
            justify="center",
        ),
        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(html.Label('Story Points',  style={'font-weight': 'bold', 'font-size': '20px'}), width=7),
                dbc.Col(dbc.Input(id= 'story_points',
                                  type='number', 
                                  min =0, max =30, step =1,
                                  className='input-text',
                                  
                                    style = {
                                        
                                        'width':'700px',
                                        'height':"45px",
                                        'padding':"10px",
                                        "font-size":"16px",
                                        "border-width":"1px",
                                        
                                    }
                                  )
                        , width=7)
             ],
            justify="center",
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(html.Label(' Type',  style={'font-weight': 'bold', 'font-size': '20px'}), width=7),
                dbc.Col(
                    [
                    dcc.Dropdown(id = 'type_picker', 
                                    options = [
                                            {'label': 'Issue', 'value': 'Issue'},
                                            {'label': 'Task', 'value': 'Task'},
                                            ],
                                    value = 'Task',
                                    className = 'inputbox2',
                                    style = {
                                        
                                        'width':'700px',
                                        'height':"45px",
                                    #     'padding':"10px",
                                        "font-size":"16px",
                                    #     "border-width":"3px",
                                        
                                    }
                                    ) 
                                                    
                    ], width= 7
                 ),
             ], 
             justify="center",
        ),
        html.Br(),
        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        id='error-output-azure',
                        style={
                            "color": 'red',
                            "font-size": 30,
                            "textAlign": "center",
                            "whiteSpace": "pre-wrap",
                        },
                    ),
                    width={"size":10, "offset":15}  
                ),
            ],
            justify="left",
        ),

        dbc.Row(
            [
                dbc.Col(
                    [
                    dbc.Button('Create Ticket', 
                            id= 'create_azure_ticket_button',
                             style = badge_style,
                             color='primary',
                             ), 
                    ],width={"size":5, "offset":1} 
                ),
             ],
             justify='center'
        ),

        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        id='success-output-azure',
                        style={
                            "color": 'green',
                            "font-size": 30,
                            "textAlign": "center",
                            "whiteSpace": "pre-wrap",
                        },
                    ),
                    width={"size":10, "offset":15} 
                ),
            ],
            justify="left",
        ),
         
        
    ],
    style=CONTAINER_STYLE,
    fluid=True
)

app.validation_layout = html.Div(
    [
        base_layout,
        layout_azure_landing()
    ]
)

app.layout = base_layout

# Callback to render different pages based on URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def render_page_content(pathname):
    if pathname in ["/Treq/"]:
        return layout_azure_landing()
    else:
        return None


# Callbacks for creating Azure issues
@app.callback(
    Output('error-output-azure', 'children'),
    [
        Input('create_azure_ticket_button', 'n_clicks'),
    ],
    [   
        State('title', 'value'),
        State('description', 'value'),
        State('anforderer', 'value'),
        State('story_points', 'value'),
        State('type_picker', 'value'),
    ]
)
def validate_inputs(n_clicks, title, description, anforderer ,story_points, type_picker):
    if n_clicks:
        if not all ([title, description, anforderer, story_points, type_picker]):
            return "Please enter text in all the fields."
        else:
            return None 


@app.callback(
    Output('success-output-azure','children'),
    [
        Input('create_azure_ticket_button', 'n_clicks'),
    ],
    [   
        State('title', 'value'),
        State('description', 'value'),
        State('anforderer', 'value'),
        State('story_points', 'value'),
        State('type_picker', 'value'),
    ]
)
def create_azure_issue_callback(n_clicks, title, description, anforderer, story_points, type_picker):
    if n_clicks and all([title, description, anforderer, story_points, type_picker]):
        create_azure_issue(title, description, anforderer, story_points, type_picker)
        return f"Azure {type_picker} created successfully"
    return None

if __name__ == '__main__':
    app.run(debug=True)
