import dash
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import airqualityapi as ai
import weatherapi as wapi

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}])


app.layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col(
                html.H1("Weather Monitoring"), xl=5, lg=6, sm=8),
            dbc.Col([
                html.A(

                    html.Img(
                        # LinkedIn logo image URL
                        src="https://cdn3.iconfinder.com/data/icons/free-social-icons/67/linkedin_circle_color-512.png",
                        height=50,  # Adjust the height as needed

                    ),
                    href="https://www.linkedin.com/in/elango-s-578770229/",  # LinkedIn profile URL
                    target="_blank",  # Open link in a new tab
                ),
            ]),
            dbc.Col([html.H1("Developer")]),
            dbc.Col([

                    # html.A(

                    #     html.Img(
                    #         src="assets/1687361194136.jpg",  # LinkedIn logo image URL
                    #         height=50,  # Adjust the height as needed

                    #     ),
                    # ),
                    ])
        ]),


        dbc.Input(id="input-field", type="text", placeholder="Enter text..."),
        dbc.Button("Print Text", id="print-button",
                   color="primary", className="mt-2"),
        html.Div(id="card", className="cardclass"),
        # html.Div(id="card2", className="cardclass"),
        # html.Div(id="card3", className="cardclass"),
        # html.Div(id="card4", className="cardclass"),
    ],
)


@app.callback(
    Output("card", "children"),
    [Input("print-button", "n_clicks")],
    [State("input-field", "value")],
)
def make_card(n_clicks, input_txt):
    if n_clicks and input_txt:  # Check if n_clicks and input have values
        loc = str(input_txt).capitalize()
        des=wapi.get_weather_description(loc)
        temp=wapi.get_temperature(loc)
        hum=wapi.get_humidity(loc)
        ws=wapi.get_wind_speed(loc)
        cnt=wapi.get_country(loc)
        if des == "Cloudy":
             ic="assets\icons8-cloudy.gif"
        else:
            ic="assets\icons8-rain.gif"
           
        if loc == None or des == None or  temp==None or hum ==  None or ws == None or cnt == None:
            return html.H1("Kindly Enter the Valid Name")
        
        return dbc. Container([dbc.Row([
            dbc.Col(  # First card starts (first row first column card wise)
                dbc.Card(
                    dbc.Row(
                        [
                            html.H1(f"{des}", className="card-title"),
                            dbc.Col(
                                dbc.CardImg(
                                    src=ic,
                                    className="img-fluid rounded-start",
                                ),
                                width=4,
                            ),
                            dbc.Col(
                                dbc.CardBody(
                                    [

                                        html.H2(f"{temp}  °C"),
                                        html.Small(f"Temperature at {loc}")
                                    ]
                                ),
                                width=10,
                            ),
                        ],

                        style={"border-radius": 20,
                               "background-color": "#86b7fe", "color": "white"}

                    ),
                    className="mb-3",
                    style={"maxWidth": "340px"},
                ),
                className='six columns', lg=5, xl=4, sm=8),  # First card Ends (first row first column card wise)



            dbc.Col(  # Second card starts (first row second column card wise)
                dbc.Card(
                    dbc.Row(
                        [
                            html.H1("Humidity", className="card-title"),
                            dbc.Col(
                                dbc.CardImg(
                                    src="assets\icons8-light-snow.gif",
                                    className="img-fluid rounded-start",
                                ),
                                width=4,
                            ),
                            dbc.Col(
                                dbc.CardBody(
                                    [

                                        html.H2(f"{hum}  %"),
                                        html.Small(f"{loc}({cnt})")
                                    ]
                                ),
                                width=10,
                            ),
                        ],

                        style={"border-radius": 20,
                               "background-color": "#86b7fe", "color": "white"}

                    ),
                    className="mb-3",
                    style={"maxWidth": "340px"},

                ),
                className='six columns',
                lg=5, xl=4, sm=8, ),  # Second card Ends (first row second column card wise)
            # Thired card:
            dbc.Col(  # Thired  card starts (first row Thired  column card wise)
                dbc.Card(
                    dbc.Row(
                        [
                            html.H1("Wind Speed", className="card-title"),
                            dbc.Col(
                                dbc.CardImg(
                                    src="assets\icons8-wind-turbine.gif",
                                    className="img-fluid rounded-start",
                                ),
                                width=4,
                            style={"leftmargin":"30px",}),
                            dbc.Col(
                                dbc.CardBody(
                                    [

                                        html.H2(f"{ws} km/h"),
                                        html.Small(f"{loc}({cnt})")
                                    ]
                                ),
                                width=10,
                            ),
                        ],

                        style={"border-radius": 20,
                               "background-color": "#86b7fe", "color": "white"}

                    ),
                    className="mb-3",
                    style={"maxWidth": "340px"},

                ),
                className='six columns',
                lg=5, xl=4, sm=8, ),  # Thired  card ends (first row Thired  column card wise)



        ])  # FIRST ROW ENDS


        
        ])
#second row

# @app.callback(
#     Output("card2", "children"),
#     [Input("print-button", "n_clicks")],
#     [State("input-field", "value")],
# )
# def make_card(n_clicks, input_txt):
#     if n_clicks and input_txt:  # Check if n_clicks and input have values
#         loc = str(input_txt).capitalize()
#         co = ai.get_co(loc)
#         return dbc. Container([dbc.Row([
#             dbc.Col(  # First card starts (first row first column card wise)
#                 dbc.Card(
#                     dbc.Row(
#                         [
#                             html.H1("Weather", className="card-title"),
#                             dbc.Col(
#                                 dbc.CardImg(
#                                     src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu3.webp",
#                                     className="img-fluid rounded-start",
#                                 ),
#                                 width=4,
#                             ),
#                             dbc.Col(
#                                 dbc.CardBody(
#                                     [

#                                         html.H2(f"{co}  CO"),
#                                         html.Small(f"Temperature at {loc}")
#                                     ]
#                                 ),
#                                 width=8,
#                             ),
#                         ],

#                         style={"border-radius": 20,
#                                "background-color": "#86b7fe", "color": "white"}

#                     ),
#                     className="mb-3",
#                     style={"maxWidth": "240px"},
#                 ),
#                 className='six columns', lg=5, xl=4, sm=8),  # First card Ends (first row first column card wise)



#             dbc.Col(  # Second card starts (first row second column card wise)
#                 dbc.Card(
#                     dbc.Row(
#                         [
#                             html.H1("Weather", className="card-title"),
#                             dbc.Col(
#                                 dbc.CardImg(
#                                     src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu3.webp",
#                                     className="img-fluid rounded-start",
#                                 ),
#                                 width=4,
#                             ),
#                             dbc.Col(
#                                 dbc.CardBody(
#                                     [

#                                         html.H2(f"{co}  CO"),
#                                         html.Small(f"Temperature at {loc}")
#                                     ]
#                                 ),
#                                 width=8,
#                             ),
#                         ],

#                         style={"border-radius": 20,
#                                "background-color": "#86b7fe", "color": "white"}

#                     ),
#                     className="mb-3",
#                     style={"maxWidth": "240px"},

#                 ),
#                 className='six columns',
#                 lg=5, xl=4, sm=8, ),  # Second card Ends (first row second column card wise)
#             # Thired card:
#             dbc.Col(  # Thired  card starts (first row Thired  column card wise)
#                 dbc.Card(
#                     dbc.Row(
#                         [
#                             html.H1("Weather", className="card-title"),
#                             dbc.Col(
#                                 dbc.CardImg(
#                                     src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu3.webp",
#                                     className="img-fluid rounded-start",
#                                 ),
#                                 width=4,
#                             ),
#                             dbc.Col(
#                                 dbc.CardBody(
#                                     [

#                                         html.H2(f"{co}  CO"),
#                                         html.Small(f"Temperature at {loc}")
#                                     ]
#                                 ),
#                                 width=8,
#                             ),
#                         ],

#                         style={"border-radius": 20,
#                                "background-color": "#86b7fe", "color": "white"}

#                     ),
#                     className="mb-3",
#                     style={"maxWidth": "240px"},

#                 ),
#                 className='six columns',
#                 lg=5, xl=4, sm=8, ),  # Thired  card ends (first row Thired  column card wise)



#         ])  # SECOND ROW ENDS


        
#         ])
#     return None
# #third row


# @app.callback(
#     Output("card3", "children"),
#     [Input("print-button", "n_clicks")],
#     [State("input-field", "value")],
# )
# def make_card(n_clicks, input_txt):
#     if n_clicks and input_txt:  # Check if n_clicks and input have values
#         loc = str(input_txt).capitalize()
#         co = ai.get_co(loc)
#         return dbc. Container([dbc.Row([
#             dbc.Col(  # First card starts (first row first column card wise)
#                 dbc.Card(
#                     dbc.Row(
#                         [
#                             html.H1("Weather", className="card-title"),
#                             dbc.Col(
#                                 dbc.CardImg(
#                                     src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu3.webp",
#                                     className="img-fluid rounded-start",
#                                 ),
#                                 width=4,
#                             ),
#                             dbc.Col(
#                                 dbc.CardBody(
#                                     [

#                                         html.H2(f"{co}  CO"),
#                                         html.Small(f"Temperature at {loc}")
#                                     ]
#                                 ),
#                                 width=8,
#                             ),
#                         ],

#                         style={"border-radius": 20,
#                                "background-color": "#86b7fe", "color": "white"}

#                     ),
#                     className="mb-3",
#                     style={"maxWidth": "240px"},
#                 ),
#                 className='six columns', lg=5, xl=4, sm=8),  # First card Ends (first row first column card wise)



#             dbc.Col(  # Second card starts (first row second column card wise)
#                 dbc.Card(
#                     dbc.Row(
#                         [
#                             html.H1("Weather", className="card-title"),
#                             dbc.Col(
#                                 dbc.CardImg(
#                                     src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu3.webp",
#                                     className="img-fluid rounded-start",
#                                 ),
#                                 width=4,
#                             ),
#                             dbc.Col(
#                                 dbc.CardBody(
#                                     [

#                                         html.H2(f"{co}  CO"),
#                                         html.Small(f"Temperature at {loc}")
#                                     ]
#                                 ),
#                                 width=8,
#                             ),
#                         ],

#                         style={"border-radius": 20,
#                                "background-color": "#86b7fe", "color": "white"}

#                     ),
#                     className="mb-3",
#                     style={"maxWidth": "240px"},

#                 ),
#                 className='six columns',
#                 lg=5, xl=4, sm=8, ),  # Second card Ends (first row second column card wise)
#             # Thired card:
#             dbc.Col(  # Thired  card starts (first row Thired  column card wise)
#                 dbc.Card(
#                     dbc.Row(
#                         [
#                             html.H1("Weather", className="card-title"),
#                             dbc.Col(
#                                 dbc.CardImg(
#                                     src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu3.webp",
#                                     className="img-fluid rounded-start",
#                                 ),
#                                 width=4,
#                             ),
#                             dbc.Col(
#                                 dbc.CardBody(
#                                     [

#                                         html.H2(f"{co}  CO"),
#                                         html.Small(f"Temperature at {loc}")
#                                     ]
#                                 ),
#                                 width=8,
#                             ),
#                         ],

#                         style={"border-radius": 20,
#                                "background-color": "#86b7fe", "color": "white"}

#                     ),
#                     className="mb-3",
#                     style={"maxWidth": "240px"},

#                 ),
#                 className='six columns',
#                 lg=5, xl=4, sm=8, ),  # Thired  card ends (first row Thired  column card wise)



#         ])  # third ROW ENDS


        
#         ])
#     return None
# #fourth row starts

# @app.callback(
#     Output("card4", "children"),
#     [Input("print-button", "n_clicks")],
#     [State("input-field", "value")],
# )
# def make_card(n_clicks, input_txt):
#     if n_clicks and input_txt:  # Check if n_clicks and input have values
#         loc = str(input_txt).capitalize()
#         co = ai.get_co(loc)
#         return dbc. Container([dbc.Row([
#             dbc.Col(  # First card starts (first row first column card wise)
#                 dbc.Card(
#                     dbc.Row(
#                         [
#                             html.H1("Weather", className="card-title"),
#                             dbc.Col(
#                                 dbc.CardImg(
#                                     src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu3.webp",
#                                     className="img-fluid rounded-start",
#                                 ),
#                                 width=4,
#                             ),
#                             dbc.Col(
#                                 dbc.CardBody(
#                                     [

#                                         html.H2(f"{co}  CO"),
#                                         html.Small(f"Temperature at {loc}")
#                                     ]
#                                 ),
#                                 width=8,
#                             ),
#                         ],

#                         style={"border-radius": 20,
#                                "background-color": "#86b7fe", "color": "white"}

#                     ),
#                     className="mb-3",
#                     style={"maxWidth": "240px"},
#                 ),
#                 className='six columns', lg=5, xl=4, sm=8),  # First card Ends (first row first column card wise)



#             dbc.Col(  # Second card starts (first row second column card wise)
#                 dbc.Card(
#                     dbc.Row(
#                         [
#                             html.H1("Weather", className="card-title"),
#                             dbc.Col(
#                                 dbc.CardImg(
#                                     src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu3.webp",
#                                     className="img-fluid rounded-start",
#                                 ),
#                                 width=4,
#                             ),
#                             dbc.Col(
#                                 dbc.CardBody(
#                                     [

#                                         html.H2(f"{co}  CO"),
#                                         html.Small(f"Temperature at {loc}")
#                                     ]
#                                 ),
#                                 width=8,
#                             ),
#                         ],

#                         style={"border-radius": 20,
#                                "background-color": "#86b7fe", "color": "white"}

#                     ),
#                     className="mb-3",
#                     style={"maxWidth": "240px"},

#                 ),
#                 className='six columns',
#                 lg=5, xl=4, sm=8, ),  # Second card Ends (first row second column card wise)
#             # Thired card:
#             dbc.Col(  # Thired  card starts (first row Thired  column card wise)
#                 dbc.Card(
#                     dbc.Row(
#                         [
#                             html.H1("Weather", className="card-title"),
#                             dbc.Col(
#                                 dbc.CardImg(
#                                     src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu3.webp",
#                                     className="img-fluid rounded-start",
#                                 ),
#                                 width=4,
#                             ),
#                             dbc.Col(
#                                 dbc.CardBody(
#                                     [

#                                         html.H2(f"{co}  CO"),
#                                         html.Small(f"Temperature at {loc}")
#                                     ]
#                                 ),
#                                 width=8,
#                             ),
#                         ],

#                         style={"border-radius": 20,
#                                "background-color": "#86b7fe", "color": "white"}

#                     ),
#                     className="mb-3",
#                     style={"maxWidth": "240px"},

#                 ),
#                 className='six columns',
#                 lg=5, xl=4, sm=8, ),  # Thired  card ends (first row Thired  column card wise)



#         ])  # FOURTH ROW ENDS


        
#         ])
#     return None




if __name__ == "__main__":
    app.run_server(debug=True)
