import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_trich_components as dtc
from flask import Flask
from app import app
import pyautogui
from dash.exceptions import PreventUpdate



layout = html.Div([
    html.Div([
        #cabeçalho
        html.Div([
            html.Img(
                src="./assets/images/logo_cear (1).png",
                id='dash_press_logo5_station',
                className="risk-reward",
            ),
            html.Div([
                html.H2(
                    "Bancada de Refrigeração ET 420",
                    id='dash_press_txt1_station',
                    className="subtitle padded",
                ),
            ], id='divTitleBancada'),
            html.Img(
                src="./assets/images/logo_ufpb.png",
                id='dash_press_logo6_station',
            )
        ], style={'border-bottom': '5px blue solid',
                    'width': '100%',
                    'border-radius': '17px',
                    'background-color': 'lightgray'}, id='menuFlona'),
        ########################
        ########################
        #dashcards que redirecionam para os dash indicados  
        html.Div([
            html.Div([
                dbc.Col(
                    html.Div(
                        [
                            html.H2("Modo Operacional - Descarga", className="display-3", id='jumbotronTitleModoCarga'),
                            html.Hr(className="my-2"),
                            html.Img(
                                src="./assets/images/mododescarga.jpg",
                                id='carga#fig1',
                            ),                  
                        ],
                        className="jumbotronModoCarga",
                    ),
                    md=6
                ),
            ], id="page-content2"),            
            html.H2(
                "O modo de descarga em um sistema de refrigeração é acionado em momentos de alta demanda térmica, quando a necessidade\
                     de resfriamento é mais intensa. Ao liberar a energia térmica armazenada no gelo, o sistema proporciona resfriamento\
                         adicional para lidar com os picos de carga, reduzindo a dependência exclusiva do funcionamento do compressor. Além\
                             disso, desligar temporariamente o compressor durante o modo de descarga resulta em economia significativa de\
                                 energia elétrica.",               
                id='h2ModoCarga',
            ),
            html.H2(
                "Essa estratégia não apenas alivia a carga do compressor em períodos de alta demanda, mas também contribui para uma operação\
                     mais eficiente e econômica do sistema de refrigeração. Além disso, o modo de descarga pode ser uma prática ecologicamente\
                         sustentável, especialmente se implementada durante o dia, quando a demanda por eletricidade é geralmente maior e a\
                             geração de energia pode ter um impacto ambiental mais significativo.",               
                id='h2ModoCarga',
            ),
            html.H2(
                "Assim, o modo de descarga não só atende às necessidades operacionais do sistema de refrigeração, mas também oferece\
                     benefícios econômicos e ambientais, tornando-se uma escolha estratégica para os operadores.",               
                id='h2ModoCarga',
            ),
            html.Br(),
            html.Br(),
            html.H2(
                    "Para mais informações referente ao Modo Operacional de Descarga e sobre a Bancada de Refrigeração ET 420. \nVisite: ",               
                    id='h2ModoCarga',
            ),
            html.A("Manual de Uso - Acumulador de Gelo e Refrigeração ET 420", href='https://plot.ly', target="_blank", id='linkModoCarga'),
        ], style={'width': '100%'}, id='layout_index_cards'),
        #seção logos
        # #logomarcas
        html.Div([
            html.Div([
                html.H2(
                    "Dashboard desenvolvido para a atividade 1 da disciplina de Máquinas Térmicas.",
                    id='dash_press_txt2_station',
                    className="subtitle padded",
                ),
            ])          
        ], style={'border-top': '5px blue solid',
                    'width': '100%',
                    'float': 'left',
                    'margin-top': '40px',
                    'border-radius': '8px',
                    'background': 'lightgray'}),
    ],   id='page-content'),
])
