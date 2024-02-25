# layout_utils
# functions to generate dynamic layout for dash

from helpers.styles import *

import dash_bootstrap_components as dbc
from dash import Dash ,dcc, dash_table, html, Input,Output, State

#import plotly.graph_objects as go
import plotly.express as px
#from plotly.subplots import make_subplots
#from datetime import datetime, date

import pandas as pd
#from itertools import cycle
#import builtins

###########################################################################################################################


# top header
def get_login_header():
    return dbc.NavbarSimple(
        [
            dbc.NavItem(
                dbc.NavLink(
                    "Logout",
                    href="/Treq/",
                    style=Ribbon_Style,
                    id="home",
                )
            )

        ],
        sticky="top",
        fluid=True,
        color=bg_color_2,
        id="get-login-header-navbar",
    )


# logo header
def get_logo_header():
    return dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(
                                    src="assets/images/tef_logo.png", height="75px"
                                )
                            ),
                        ],
                        align="center",
                        justify="between",
                    ),
                    href="/Treq/",
                ),
            ],
            fluid=True,
        ),
    )

###########################################################################################################################

# def colrow2(a, b):
#     return dbc.Row([dbc.Col([a], width=6), dbc.Col([b], width=6)])


# def colrow3(a, b, c):
#     return dbc.Row(
#         [
#             dbc.Col([a], width=4),
#             dbc.Col([b], width=4),
#             dbc.Col([c], width=4),
#         ]
#     )


# def input_field_col(field, placeholder, id, value=None, disabled=False, pers_type=None):
#     params = {
#         "autoComplete": True,
#         "id": id,
#         "debounce": True,
#         "maxLength": 200,
#         "style": {"font-size": "15px", "height": "100%"},
#         "disabled": disabled,
#     }
#     if value is None:
#         params["placeholder"] = placeholder
#     else:
#         params["value"] = value
#     if pers_type in ["local", "memory", "session"]:
#         params["persistence"] = True
#         params["persistence_type"] = pers_type
#     return dbc.Row(
#         dbc.Col(
#             [
#                 dbc.InputGroup(
#                     [
#                         dbc.InputGroupText(field),
#                         dbc.Input(**params),
#                     ],
#                 )
#             ],
#             width={"size": 12},
#         )
#     )