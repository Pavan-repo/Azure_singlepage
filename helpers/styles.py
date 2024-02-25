import builtins

###########################################################################################################################
# COLOR
###########################################################################################################################

primary_palette = {
        "colorblue": "rgb(0,83,159)",
        "colorred": "rgb(238,28,46)",
        "white": "rgb(255,255,255",
        "dark_grey": "rgb(110,103,103)",
        "black": "rgb(0, 0, 0)",
    }

# secondary_palette = {
#         "colororange": "rgb(255,166,38)",
#         "colorsalmon": "rgb(255,125,130)",
#         "colorturquoise": "rgb(0,188,212)",
#         "colorteal": "rgb(0,191,165)",
#         "colorsand": "rgb(204,186,161)",
#         "colorpink": "rgb(255,128,171)",
#         "colorbronze": "rgb(157,28,23)",
#         "coloryellow": "rgb(250,189,43)",
#         "coloremerald": "rgb(12,126,103)",
#         "colorgreen": "rgb(105,178,74)",
#         "colorindigo": "rgb(92,107,192)",
#         "colorpurple": "rgb(156,38,176)",
#         "colorlight_orange": "rgb(255,224,178)",
#         "colorlight_salmon": "rgb(255,204,191)",
#         "colorlight_turquoise": "rgb(178,235,242)",
#         "colorlight_teal": "rgb(178,223,219)",
#         "colorlight_sand": "rgb(245,240,224)",
#         "colorlight_pink": "rgb(248,187,208)",
#         "colordark_orange": "rgb(214,67,0)",
#         "colordark_salmon": "rgb(199,74,82)",
#         "colordark_turquoise": "rgb(0,131,143)",
#         "colordark_teal": "rgb(0,77,64)",
#         "colordark_sand": "rgb(123,107,89)",
#         "colorlight_blue_grey": "rgb(176,191,196)",
#         "colorlight_emerald": "rgb(166,207,173)",
#         "colorlight_green": "rgb(197,225,165)",
#         "colorlight_grey": "rgb(246,246,246)",
#         "colorlight_indigo": "rgb(197,202,233)",
#         "colorlight_purple": "rgb(224,191,232)",
#         "colordark_blue_grey": "rgb(56,71,79)",
#         "colordark_emerald": "rgb(38,96,84)",
#         "colordark_green": "rgb(51,105,30)",
#         "colordark_indigo": "rgb(26,35,126)",
#         "colordark_pink": "rgb(200,27,96)",
#         "colordark_purple": "rgb(92,41,87)",
#         "colorpurple": "rgb(156,38,176)",
#     }

# interaction_palette = {
#     "highlight_blue": "rgb(0,126,179)",
#     "error_red": "rgb(204,51,51)",
# }

# text_palette = {
#     "text_grey_1": "rgb(51,51,51)",
#     "text_grey_2": "rgb(102,102,102)",
#     "text_grey_3": "rgb(204,204,204)",
# }

# background_palette = {
#     "bg_grey_1": "rgb(246,246,246)",
#     "bg_blue": "rgb(229,232,234)",
#     "ut_blue": "rgb(0,41,79)",
#     "bg_grey_2": "rgb(229,229,229)",
# }

# line_palette = {"line_1": "rgb(204,204,204)", "line_2": "rgb(229,229,229)"}


###########################################################################################################################
# STYLES
###########################################################################################################################

bg_color_1 = primary_palette["white"]
bg_color_2 = primary_palette["colorblue"]
bg_color_3 = primary_palette["black"]
bg_color_4 = primary_palette["dark_grey"]
#hover_color = secondary_palette["colorlight_turquoise"]
base_div_style = {"overflowX": "none", "overflowY": "auto"}

# footer_div_style = {
#     "position": "fixed",
#     "bottom": "0px",
#     "right": "0px",
#     "left": "0px",
#     "height": "35px",
#     "background": bg_color_3,
#     "color": bg_color_1,
#     "textAlign": "center",
#     "width": "100%",
#     "overflow": "none",
#     "display": "inline-block",
#     "zIndex": 1001,
#     "font-size": 10,
# }

# the main container style
CONTAINER_STYLE = {
    "margin": "none",
    "padding": "none",
    "overflowY": "auto",
    "overflowX": "none",
    "maxWidth": "none",
    "maxHeight": "none",
    "border": "none",
    "backgroundColor": bg_color_1,
}

NAVBAR_STYLE = {
    "fontSize": 25,
    "border": "none",
    "backgroundColor": bg_color_3,
    "color": "white",
    "fontWeight": 700,
}

# Chart_Header = {
#     "backgroundColor": bg_color_4,
#     "textAlign": "center",
#     "hover": {"color": hover_color},
#     "color": "white",
#     # "height": "42px",
#     "fontweight": 800,
#     "font-size": 15,
# }

# Section_Header = {
#     "backgroundColor": bg_color_2,
#     "textAlign": "center",
#     "hover": {"color": hover_color},
#     "color": "white",
#     "fontWeight": 800,
#     "font-size": 15,
# }

# Method_Selection_Header = {
#     "backgroundColor": bg_color_4,
#     "textAlign": "center",
#     "hover": {"color": hover_color},
#     "color": "white",
#     "fontweight": 400,
# }

# Table_Header = {
#     "fontFamily": "Tesco Modern",
#     "fontWeight": 700,
#     "fontSize": "16",
#     "backgroundColor": bg_color_4,
#     "color": "white",
#     "whiteSpace": "normal",
#     "height": "auto",
#     "lineHeight": "20px",
#     "overflow": "hidden",
#     "textOverflow": "ellipsis",
#     "minWidth": 95,
#     "maxWidth": 95,
#     "width": 95,
#     "textAlign": "center",
# }

# Table_Data_Left = {
#     "fontFamily": "Tesco Modern",
#     "fontWeight": 400,
#     "paddingRight": "10px",
#     "whiteSpace": "pre-line",
#     "height": "auto",
#     "lineHeight": "20px",
#     "textAlign": "left",
#     "tableLayout": "fixed",
# }

# Table_Data = {
#     "fontFamily": "Tesco Modern",
#     "fontWeight": 400,
#     "paddingRight": "10px",
#     "whiteSpace": "normal",
#     "height": "auto",
#     "lineHeight": "20px",
#     "textAlign": "center",
# }

# Inline with Tesco Site
Ribbon_Style = {
    "fontSize": "20px",
    "border": "none",
    "color": bg_color_1,
    "weight": 700,
    "fontWeight": "bold",
    "active": {"background-color": "#4CAF50"},
   # "borderRight": "1.5px solid rgb(246,246,246)",
    "margin": 0.5,
    "padding": -0.5,
    # "border" : 0,
    "verticalAlign": "baseline",
    # "cursor":"pointer",
    # "fontStyle": "normal",
    # "fontVariantLigatures": "normal",
    # "fontVariantCaps": "normal",
    # "fontStretch": "normal",
    # "lineHeight": "1.5",
}

# LastItem_Ribbon_Style = {
#     "fontSize": "25px",
#     "border": "none",
#     "color": bg_color_1,
#     "weight": 700,
#     "fontWeight": "bold",
#     "backgroundColor": bg_color_2,
#     # "border-right": "1.5px solid rgb(246,246,246)"
# }


# Navicon_Style = {
#     "borderRight": "1.5px solid rgb(246,246,246)",
#     "margin": 3,
#     "padding": -1.5,
#     "verticalAlign": "baseline",
# }

###########################################################################################################################

logo_style = {"align": "left", "display": "inline-block"}

btn_active_style = {
    "color": bg_color_2,
    "backgroundColor": bg_color_1,
}
btn_inactive_style = {
    "color": bg_color_4,
    "backgroundColor": bg_color_1,
}
btn_hidden_style = {"display": "none"}

# dropdown_style = {
#     "fontFamily": "Tesco Modern",
#     "fontWeight": 400,
# }

# upload_style = {
#     "borderWidth": "1px",
#     "borderStyle": "dashed",
#     "borderRadius": "2.5px",
#     "textAlign": "center",
#     "margin": "5px",
#     # "background-color": bg_color_4,
#     # "color": "white",
# }

# download_btn_style = {
#     "color": bg_color_1,
#     "backgroundColor": bg_color_3,
# }
# save_btn_style = {
#     "color": bg_color_2,
#     "backgroundColor": bg_color_1,
#     "fontWeight": 700,
#     "fontFamily": "Tesco Modern",
#     "borderRadius": "8px",
# }

# summary_btn_style = {
#     "color": bg_color_2,
#     "backgroundColor": bg_color_1,
#     "fontWeight": 700,
#     "fontSize": "25px", 
#     "fontFamily": "Tesco Modern",
#     "borderRadius": "8px",
#     "width" : "400px",
#     "height" : "60px"
# }

# summary_btn_style_header = {
#     "color": bg_color_2,
#     "backgroundColor": bg_color_1,
#     "fontWeight": 700,
#     "fontSize": "20px", 
#     "fontFamily": "Tesco Modern",
#     "borderRadius": "8px",
#     "width" : "350px",
#     "height" : "50px",
#     "textAlign": "center",
# }


badge_style = {
    "backgroundColor": bg_color_2,
    "textAlign": "center",
    "fontFamily": "Tesco Modern",
    "fontWeight": 700,
    "fontSize": "25px", 
    "fontFamily": "Tesco Modern",
    "borderRadius": "8px",
    "width" : "200px",
    "height" : "50px",
    "textAlign": "center",
}

# warning_style = {
#     "fontSize": "15px",
#     "fontWeight": 700,
#     "color": primary_palette["colorred"],
# }

# kpicard_background_style = {"light_grey": "rgb(248,246,248)"}
