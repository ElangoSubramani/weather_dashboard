import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        html.H1("Enter Some Text"),
        dbc.Input(id="input-field", type="text", placeholder="Enter text..."),
        dbc.Button("Search", id="print-button", color="primary", className="mt-2"),
        html.Div(id="output-text", className="mt-3"),
    ],
    className="mt-4",
    fluid=True,
)

# Define callback to update the output based on input
@app.callback(
    Output("output-text", "children"),
    [Input("print-button", "n_clicks")],
    [State("input-field", "value")],
)
def print_text(n_clicks, input_value):
    if n_clicks is not None and n_clicks > 0:
        if input_value is not None:
            return html.H3(f"You entered: {input_value}")
        else:
            return html.H3("Enter some text in the input field.")
    return ""  

if __name__ == "__main__":
    app.run_server(debug=True)
