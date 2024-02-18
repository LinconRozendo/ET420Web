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
import os

os.environ['DISPLAY'] = ':0'




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
                            html.H2("Modo Operacional - Carga", className="display-3", id='jumbotronTitleModoCarga'),
                            html.Hr(className="my-2"),
                            html.Img(
                                src="./assets/images/carga.jpg",
                                id='carga#fig1',
                            ),                  
                        ],
                        className="jumbotronModoCarga",
                    ),
                    md=6
                ),
            ], id="page-content2"),            
            html.H2(
                "O modo de carga é uma etapa crucial no processo de resfriamento da água armazenada até que atinja o ponto de\
                     congelamento, utilizando a mistura de glicol/água. Essa estratégia se mostra particularmente vantajosa durante\
                         os períodos de baixa demanda por refrigeração ou durante as horas em que a eletricidade é mais barata, geralmente\
                             à noite.",               
                id='h2ModoCarga',
            ),
            html.H2(
                "O encerramento do modo de carga ocorre tipicamente quando a temperatura T8 na saída do armazenamento de gelo cai abaixo\
                de -3°C, indicando uma diferença de temperatura inadequada entre a entrada e a saída do sistema.",               
                id='h2ModoCarga',
            ),
            html.H2(
                "Para otimizar o processo de carga, é recomendável ativar ambas as torres de resfriamento externas. Caso contrário,\
                     a temperatura da mistura de glicol/água pode aumentar, comprometendo a capacidade de resfriamento do sistema. Essa\
                         abordagem visa garantir uma carga rápida e eficiente do armazenamento de gelo, assegurando a disponibilidade de\
                             refrigeração quando necessária, além de promover a eficiência energética do sistema como um todo.",               
                id='h2ModoCarga',
            ),
            html.Br(),
            html.Br(),
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


