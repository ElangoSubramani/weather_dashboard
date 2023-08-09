import dash
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import airqualityapi as ai
import weatherapi as wapi

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


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
        html.Div(id="card",className="cardclass"),
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
        co = ai.get_co(loc)
        return dbc.Row([
            dbc.Col(dbc.Card(
            dbc.Row(
                [
                    html.H1("Weather", className="card-title"),
                    dbc.Col(
                        dbc.CardImg(
                            src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu3.webp",
                            className="img-fluid rounded-start",
                        ),
                        width=4,
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            [

                                html.H2(f"{co}  CO"),
                                html.Small(f"Temperature at {loc}")
                            ]
                        ),
                        width=8,
                    ),
                ],

                style={"border-radius": 20,
                       "background-color": "#86b7fe", "color": "white"}

            ),
            className="mb-3",
            style={"maxWidth": "240px"},
        ),
      className='six columns',lg=5,xl=4,sm=8 ),



            dbc.Col(dbc.Card(
            dbc.Row(
                [
                    html.H1("Weather", className="card-title"),
                    dbc.Col(
                        dbc.CardImg(
                            src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-weather/ilu3.webp",
                            className="img-fluid rounded-start",
                        ),
                        width=4,
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            [

                                html.H2(f"{co}  CO"),
                                html.Small(f"Temperature at {loc}")
                            ]
                        ),
                        width=8,
                    ),
                ],

                style={"border-radius": 20,
                       "background-color": "#86b7fe", "color": "white"}

            ),
            className="mb-3",
            style={"maxWidth": "240px"},
            
        ),
     className='six columns',
      lg=5,xl=4,sm=8, )
        ])
    return None


if __name__ == "__main__":
    app.run_server(debug=True)
