import dash
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import airqualityapi as ai

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])





app.layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col(
             html.H1("Weather Monitoring"),),
            dbc.Col([
                html.H1("Developer"),
                    html.A(
                         
                        html.Img(
                            src="https://cdn3.iconfinder.com/data/icons/free-social-icons/67/linkedin_circle_color-512.png",  # LinkedIn logo image URL
                            height=40,  # Adjust the height as needed
                            className="me-2",  # Margin between the logo and input field
                        ),
                        href="https://www.linkedin.com/",  # LinkedIn profile URL
                        target="_blank",  # Open link in a new tab
                    ),
         ] )
    ]),
        
       
        dbc.Input(id="input-field", type="text", placeholder="Enter text..."),
        dbc.Button("Print Text", id="print-button", color="primary", className="mt-2"),
        html.Div(id="card", style=dict(width="50%", backgroundImage="url('background.jpg')", backgroundSize="cover"), className="mt-3"),
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
        return  dbc.Card(
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
       
        style={"border-radius":20,"background-color": "#86b7fe", "color": "white"}
        
    ),
    className="mb-3",
    style={"maxWidth": "340px"},
)
    return None

if __name__ == "__main__":
    app.run_server(debug=True)
