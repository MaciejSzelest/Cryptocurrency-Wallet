import dash_html_components as html
import dash_bootstrap_components as dbc

class Blog:

   def get_posts():
        Posts = html.Div([

            dbc.Card(
                    dbc.CardBody(
                        [
                            html.H1("I 2022: Welcome!"),
                            html.Hr(),
                            dbc.Row(
                                [
                                dbc.Col(
                                    [
                                    dbc.Row("Hello everyone, this is my first post on this project. I decided to also create this small blog, just to let how things are going on. I will reply here once per month to let you know about transactions, but as you know this is a fully transparent project so every transaction will be visible in my wallet. I am fully open to any suggestions so your advice is more than welcome. As you can see my journey starts with quite a loss because, I am losing around -90 usdt, but hey it is just a beginning! I hope this project will be useful for you too :)"),
                                    html.Hr(),
                                    dbc.Row("Invested: for 48 usdt i bought: 11.2 ada, 59 hbar, 20 xrp and 15 iota"),
                                    dbc.Row("Donations: zero so far :)"),
                                    ],
                                className="card_txt")
                                ],
                            ),
                        ]
                    ),
                ),
            ])
        return Posts