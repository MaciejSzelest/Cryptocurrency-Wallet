from binance_API import Data
import pandas as pd
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output

# Parameters ###########################################################################################################

price_list = ['ADA', 'BTC', 'ETH', 'SOL']
trade_list = ['ADAUSDT', 'BTCUSDT', 'ETHUSDT', 'SOLUSDT']

# Data Sourcing ########################################################################################################

account_tab = Data.get_account_details()
account_value_tab = Data.get_account_value(price_list)
for trade in trade_list:
    if trade == 'ADAUSDT':
        ada_tab = Data.get_orders(trade)
    elif trade == 'BTCUSDT':
        btc_tab = Data.get_orders(trade)
    elif trade == 'ETHUSDT':
        eth_tab = Data.get_orders(trade)
    elif trade == 'SOLUSDT':
        sol_tab = Data.get_orders(trade)
total_tab = Data.get_total(ada_tab, btc_tab, eth_tab, sol_tab)

# Data Analytics #######################################################################################################

account_fig = px.pie(values=account_tab.amount, names=account_tab.asset, template='plotly_dark',
                     color_discrete_sequence=px.colors.qualitative.Antique
                     ).update_layout(
    {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
     'paper_bgcolor': 'rgba(0, 0, 0, 0)',
     'showlegend': True,
     'legend': dict(orientation="h", yanchor= 'bottom', y=-0.2, xanchor='center', x=0.5)})

account_price_fig = px.bar(account_value_tab, x="asset", y="value", hover_data=['amount', 'price'],
                           color="asset", barmode="group", template='plotly_dark',
                           color_discrete_sequence=px.colors.qualitative.Antique).update_layout(
    {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
     'paper_bgcolor': 'rgba(0, 0, 0, 0)',
     'showlegend': False})

ada_fig = px.bar(ada_tab, x='amount', y='PNL', color='asset', template='plotly_dark', height=400,
                 color_discrete_sequence=px.colors.qualitative.Antique).update_layout(
    {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
     'paper_bgcolor': 'rgba(0, 0, 0, 0)',
     'showlegend': False})

btc_fig = px.bar(btc_tab, x='amount', y='PNL', color='asset', template='plotly_dark', height=400,
                  color_discrete_sequence=px.colors.qualitative.Antique).update_layout(
    {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
     'paper_bgcolor': 'rgba(0, 0, 0, 0)',
     'showlegend': False})

eth_fig = px.bar(eth_tab, x='amount', y='PNL', color='asset', template='plotly_dark', height=400,
                  color_discrete_sequence=px.colors.qualitative.Antique).update_layout(
    {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
     'paper_bgcolor': 'rgba(0, 0, 0, 0)',
     'showlegend': False})
sol_fig = px.bar(sol_tab, x='amount', y='PNL', color='asset', template='plotly_dark', height=400,
                 color_discrete_sequence=px.colors.qualitative.Antique).update_layout(
    {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
     'paper_bgcolor': 'rgba(0, 0, 0, 0)',
     'showlegend': False})

total_amt_fig = px.bar(total_tab, x='asset', y='PNL', color='asset', template='plotly_dark',
                       color_discrete_sequence=px.colors.qualitative.Antique).update_layout(
    {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
     'paper_bgcolor': 'rgba(0, 0, 0, 0)',
     'showlegend': False})

crypto_fame = [ada_tab, btc_tab, eth_tab, sol_tab]
crypto = pd.concat(crypto_fame)

crypto_fig = px.scatter(crypto, x='amount', y='PNL', color='asset', template='plotly_dark', height=400,
                        color_discrete_sequence=px.colors.qualitative.Antique).update_layout(
    {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
     'paper_bgcolor': 'rgba(0, 0, 0, 0)',
     'showlegend': True,
     'legend': dict(orientation="h", yanchor= 'bottom', y=-0.3, xanchor='center', x=0.5)
     })

price_fig = px.scatter(crypto, x='price', y='PNL', color='asset', template='plotly_dark', height=400,
                       color_discrete_sequence=px.colors.qualitative.Antique).update_layout(
    {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
     'paper_bgcolor': 'rgba(0, 0, 0, 0)',
     'showlegend': True,
     'legend': dict(orientation="h", yanchor= 'bottom', y=-0.3, xanchor='center', x=0.5)
     })

wallet_amount_txt = f'WALLET BALANCE: {round(account_value_tab["value"].sum(), 2)} USDT'
wallet_pnl_txt = f'WALLET PROFIT/LOSS: {round(total_tab["PNL"].sum(), 2)} USDT'
roe = f'ROE: {round(((total_tab["PNL"].sum()) / (account_value_tab["value"].sum())*100),2)} %'
ada_txt = f'ADA PROFIT/LOSS: {round(ada_tab["PNL"].sum(), 2)} USDT'
btc_txt = f'BTC PROFIT/LOSS: {round(btc_tab["PNL"].sum(), 2)} USDT'
eth_txt = f'ETH PROFIT/LOSS: {round(eth_tab["PNL"].sum(), 2)} USDT'
sol_txt = f'SOL PROFIT/LOSS: {round(sol_tab["PNL"].sum(), 2)} USDT'


# Dash App Layout ######################################################################################################

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

navbar = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(
                            src=app.get_asset_url("logo.png"), height="130px"
                        ),
                        width=3,
                    ),
                    dbc.Col(
                        [
                            html.Label("CRYPTOCURRENCY WALLET", id="label1"),
                            html.Label("WEB-BASED ONLINE WALLET IN CONNECTION WITH BINANCE API FOR LONG-TERM INVESTMENT",
                                       className="label2",
                                       ),
                            html.Br(),
                            html.Label("OPEN-SOURCE WALLET PROJECT WITH DATA ANALYTICS, FOR FOUR SELECTED CRYPTOCURRENCIES",
                                       className="label2",
                                       style={"margin-bottom": ".34rem"},
                                       ),
                        ],
                        width=8,
                    ),
                ],
                align="between",
                no_gutters=True,
            ),
        ),
    ],
)

card_tab_1 = dbc.Card(
    [
        dbc.FormGroup(
            [
                html.Label(wallet_amount_txt),
                html.Br(),
                dcc.Graph(id='account_price_fig', config={'displayModeBar': False}, animate=True, figure=account_price_fig),
            ]
        ),
    ],
    body=True,
    className="card_tabs",
)

card_tab_2 = dbc.Card(
    [
        dbc.FormGroup(
            [
                html.Label(wallet_pnl_txt),
                html.Br(),
                dcc.Graph(id='total_amt_fig', config={'displayModeBar': False}, animate=True, figure=total_amt_fig),

            ]
        ),
    ],
    body=True,
    className="card_tabs",
)

cards_1 = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div("TGC AMOUNT/PNL SCATTER", className="cards"),
                    html.Div(id="P_position1", className="card_info1"),
                    dcc.Graph(id='crypto_fig', config={'displayModeBar': False}, animate=True, figure=crypto_fig),
                ]
            ),
            className="card_attributes",
        ),
    ]
)
cards_2 = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div("TGC PRICE/PNL SCATTER", className="cards"),
                    html.Div(id="P_foot2", className="card_info2"),
                    dcc.Graph(id='price_fig', config={'displayModeBar': False}, animate=True, figure=price_fig),
                ]
            ),
            className="card_attributes",
        ),
    ]
)
cards_3 = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(ada_txt, className="cards"),
                    dcc.Graph(id='ada_fig', config={'displayModeBar': False}, animate=True, figure=ada_fig),
                ]
            ),
            className="card_attributes",
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(btc_txt, className="cards"),
                    dcc.Graph(id='btc_fig', config={'displayModeBar': False}, animate=True, figure=btc_fig),
                ]
            ),
            className="card_attributes",
        ),
    ]
)
cards_4 = dbc.CardDeck(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(eth_txt, className="cards"),
                    dcc.Graph(id='eth_fig', config={'displayModeBar': False}, animate=True, figure=eth_fig),
                ]
            ),
            className="card_attributes",
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.Div(sol_txt, className="cards"),
                    dcc.Graph(id='sol_fig', config={'displayModeBar': False}, animate=True, figure=sol_fig),
                ]
            ),
            className="card_attributes",
        ),
    ]
)

tab1_content = (
    html.Div(
        [
            dbc.Card(
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        dbc.Row(card_tab_1),  # LEFT
                                    ],
                                    sm=3,
                                ),
                                dbc.Col(
                                    [
                                        html.H1("WALLET OVERVIEW"),
                                        html.H4(roe),
                                        dcc.Graph(id='account_fig', config={'displayModeBar': False}, animate=True, figure=account_fig)
                                    ],
                                    sm=6, align="center"
                                ),
                                dbc.Col(
                                    [
                                        dbc.Row(card_tab_2),  # RIGHT
                                    ],
                                    sm=3,
                                ),
                            ],
                        justify="between",
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        cards_1,
                                        html.Hr(),
                                        cards_3,
                                    ],
                                    sm=6,
                                ),
                                dbc.Col(
                                    [
                                        cards_2,
                                        html.Hr(),
                                        cards_4,
                                    ],
                                    sm=6,
                                ),
                            ]
                        ),
                    ]
                )
            )
        ]
    ),
)
tab2_content = html.Div(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H1("About the project"),
                    html.Hr(),
                    dbc.Row(
                        [
                        dbc.Col(
                            [
                            dbc.Row("- This is open-source cryptocurrencies wallet for the crypto community"),
                            dbc.Row("- Collect four selected cryptocurrencies for long term investment"),
                            dbc.Row("- Unfortunately, project is set to four cryptocurrencies due to binance api limitations"),
                            dbc.Row("- I really would like to create universal online wallet but currently it is not possible"),
                            dbc.Row("- Feel free to align it as much as you would like and good luck with your investments!"),
                            dbc.Row(["- You can check my personal wallet for third generation cryptocurrencies, link to the page >>>",
                            dcc.Link(html.A('CLICK HERE!'),
                                            href="https://tgc-wallet.herokuapp.com/",
                                            target="_blank",
                                            style={'color': 'grey', 'text-decoration': 'none'}),
                                         ]),
                            ],
                        className="card_txt")
                        ],
                    ),
                ]
            ),
        ),
    ]
)

app.layout = dbc.Container(
    [
        navbar,
        dbc.Tabs(
            [
                dbc.Tab(tab1_content, label="Wallet"),
                dbc.Tab(tab2_content, label="About me"),
            ],
        ),
    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run_server(debug=True)