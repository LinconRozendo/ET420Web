import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_trich_components as dtc
from flask import Flask
from app import app
import os

os.environ['DISPLAY'] = ':0'



layout = html.Div([
    dcc.Location(id='url', refresh=False),
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
                            html.H2("Modo Operacional - Bypass", className="display-3", id='jumbotronTitleModoCarga'),
                            html.Hr(className="my-2"),
                            html.Img(
                                src="./assets/images/bypass.jpg",
                                id='carga#fig1',
                            ),                  
                        ],
                        className="jumbotronModoCarga",
                    ),
                    md=6
                ),
            ], id="page-content2"),            
            html.H2(
                "O modo Bypass é uma função dinâmica que opera em diferentes níveis de carga de trabalho. Em situações de baixa demanda\
                     por refrigeração, o sistema pode dispensar o uso do armazenamento de gelo, já que a capacidade de resfriamento do\
                         evaporador é suficiente para atender às necessidades de refrigeração.",               
                id='h2ModoCarga',
            ),
            html.H2(
                "Entretanto, quando a demanda por refrigeração aumenta, indicada pelo aumento da temperatura T5 na etapa intermediária,\
                     a operação exclusiva do evaporador torna-se insuficiente. Isso sinaliza uma sobrecarga no sistema e a necessidade de\
                         mais capacidade de resfriamento. Para garantir sua eficácia, é necessário adicionar pelo menos uma torre de\
                             resfriamento adicional. Isso auxilia na redução da temperatura na etapa intermediária e mantém o sistema\
                                 operando dentro das condições ideais.",               
                id='h2ModoCarga',
            ),
            html.H2(
                "Essa abordagem não apenas otimiza o desempenho do sistema de refrigeração, mas também assegura que as demandas de resfriamento\
                     sejam atendidas de forma eficiente e confiável, promovendo uma operação mais estável e econômica.",               
                id='h2ModoCarga',
            ),
            html.H2(
                    "Para mais informações referente ao Modo Operacional de Carga e sobre a Bancada de Refrigeração ET 420. \nVisite: ",               
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
