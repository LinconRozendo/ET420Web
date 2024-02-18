# dash inicial
# link de exibição ao rodar = http://127.0.0.1:8050/

from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_trich_components as dtc
from flask import Flask
from app import app
from dash.exceptions import PreventUpdate
from dashboard import dashboard_carga, dashboard_descarga, dashboard_bypass, dashboard_components, dashboard_app, dashboard_equipe
import os

os.environ['DISPLAY'] = ':0'

#server = Flask(__name__)
server = app.server


app.layout = html.Div([
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
        html.Div([
            dbc.Button("Ciclos", color="primary", size="lg", className="me-1", id='button1', n_clicks=0),
            dbc.Button("Componentes", color="primary", size="lg", className="me-1", id='button2', n_clicks=0),
            dbc.Button("Aplicações", color="primary", size="lg", className="me-1", id='button3', n_clicks=0),
            dbc.Button("Sobre nós", color="primary", size="lg", className="me-1", id='button4', n_clicks=0),
        ], style={'border-bottom': '3px blue solid',
                    'width': '100%',
                    'float': 'left',
                    'margin-bottom': '20px',
                    'height': '80px',
                    'border-radius': '15px',
                    'background': 'slategray'}),
        ########################
        #dashcards que redirecionam para os dash indicados  
        html.Div([
            html.Div([
                # dashcard do dash presentation
                html.Img(
                    src="./assets/images/bancada_et420.png",
                    id='home#fig1',
                ),
            ], id='divImageBancada'),
            html.Div([
                dbc.Col(
                    html.Div(
                        [
                            html.H2("Acumulador de Gelo e Refrigeração - ET 420", className="display-3"),
                            html.Hr(className="my-2"),
                            html.H3(
                                'O Acumulador de Gelo e Refrigeração ET 420 desempenha um papel fundamental no estudo prático de sistemas \
                                de refrigeração, bem como em outras investigações termodinâmicas relacionadas à transferência de calor. \
                                Esta bancada de refrigeração é composta por uma estrutura principal que integra uma unidade de armazenamento de gelo, um \
                                sistema de refrigeração e um circuito contendo uma mistura de glicol-água. Além disso, inclui uma torre de \
                                resfriamento seco e uma torre de resfriamento úmido. A bancada é parte integrante do conjunto de equipamentos \
                                do Laboratório de Refrigeração por Adsorção (LABRADS), sediado no Centro de Energias Alternativas e Renováveis \
                                (CEAR) da Universidade Federal da Paraíba (UFPB).',
                                id='txtBancada' 
                            ),
                            dbc.Button("LABRADS", color="light", outline=True, id='buttonLABRADS', href='http://plone.ufpb.br/labrads'),                  
                        ],
                        className="h-100 p-5 text-white bg-dark rounded-3",
                    ),
                    md=6,
                ),
            ], id="page-content2"),            
            html.H2(
                "ET 420 Ice Stores in Refrigeration",
                id='h2NomeBancada',
            ),
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
                    'margin-top': '80px',
                    'border-radius': '8px',
                    'background': 'lightgray'}),
    ],   id='page-content'),
])

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
                    "Bancada de Refrigeração",
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
        html.Div([
            dbc.Button("Ciclos", color="primary", size="lg", className="me-1", id='button1', n_clicks=0),
            dbc.Button("Componentes", color="success", size="lg", className="me-1", id='button2', n_clicks=0),
            dbc.Button("Aplicações", color="danger", size="lg", className="me-1", id='button3', n_clicks=0),
        ], style={'border-bottom': '3px blue solid',
                    'width': '100%',
                    'float': 'left',
                    'margin-bottom': '20px',
                    'height': '80px',
                    'border-radius': '15px',
                    'background': 'linear-gradient(45deg, black, transparent)'}),
        ########################
        #dashcards que redirecionam para os dash indicados  
        html.Div([
            html.Div([
                # dashcard do dash presentation
                html.Img(
                    src="./assets/images/img1.png",
                    id='home#fig1',
                ),
            ], id='divImageBancada'),
            html.Div([
                dbc.Col(
                    html.Div(
                        [
                            html.H2("Acumulador de Gelo e Refrigeração - ET 420", className="display-3"),
                            html.Hr(className="my-2"),
                            html.H3(
                                'O Acumulador de Gelo e Refrigeração ET 420 desempenha um papel fundamental no estudo prático de sistemas \
                                de refrigeração, bem como em outras investigações termodinâmicas relacionadas à transferência de calor. \
                                Esta bancada de refrigeração é composta por uma estrutura principal que integra uma unidade de armazenamento de gelo, um \
                                sistema de refrigeração e um circuito contendo uma mistura de glicol-água. Além disso, inclui uma torre de \
                                resfriamento seco e uma torre de resfriamento úmido. A bancada é parte integrante do conjunto de equipamentos \
                                do Laboratório de Refrigeração por Adsorção (LABRADS), sediado no Centro de Energias Alternativas e Renováveis \
                                (CEAR) da Universidade Federal da Paraíba (UFPB).',
                                id='txtBancada' 
                            ),
                            dbc.Button("LABRADS", color="light", outline=True, id='buttonLABRADS', href='http://plone.ufpb.br/labrads'),                  
                        ],
                        className="h-100 p-5 text-white bg-dark rounded-3",
                    ),
                    md=6,
                ),
            ], id="page-content2"),            
            html.H2(
                "ET 420 Ice Stores in Refrigeration",
                id='h2NomeBancada',
            ),
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
                    'margin-top': '80px',
                    'border-radius': '8px',
                    'background': 'lightgray'}),
    ],   id='page-content'),
], id='layout_index')



# callback destinada ao redirecionamento entre os dash via layout de cada dash
@app.callback(Output('page-content', 'children'),
                Input('url', 'pathname'),
                prevent_initial_call = True)
def display_page(pathname):
    
    if pathname == '/modo_carga':
        return dashboard_carga.layout
    elif pathname == '/modo_descarga':
        return dashboard_descarga.layout
    elif pathname == '/modo_bypass':
        return dashboard_bypass.layout
    else:
        raise PreventUpdate
   
 

@app.callback(Output('page-content2', 'children', allow_duplicate=True),
            Input('button1', 'n_clicks'),
            prevent_initial_call = True)
def display_page(clicks):
    
    if clicks > 0:

        return html.Div([
                dtc.Card(
                id='card1',
                openNewTab = False,
                link='/modo_carga',
                image='./assets/images/carga.jpg',
                title='Modo Operacional - Carga',
                description='Descubra o funcionamento do modo operacional de carga da bancada de refrigeração ET 420 através de\
                     um diagrama ilustrativo e informações essenciais. Explore os elementos fundamentais da bancada.\
                        Este card oferece uma visão concisa sobre o modo de operação, proporcionando insights sobre sua aplicação\
                             prática e seu papel na bancada',
                badges=['Máquinas Térmicas', 'Bancada de Refrigeração', 'CEAR'],
                git='https://github.com/LinconRozendo',
                dark=True,
            ),
            # dashcard do dash global
            dtc.Card(
                id='card2',
                openNewTab = False,
                link='/modo_descarga',
                image='./assets/images/mododescarga.jpg',
                title='Modo Operacional - Descarga',
                description='Descubra os segredos por trás do modo operacional de descarga da bancada de refrigeração ET 420. Contendo\
                     um diagrama simplificado, oferece-se uma visão direta dos processos envolvidos na liberação controlada de\
                         calor após o ciclo de refrigeração. Explore como a bancada gerencia eficientemente o processo de descarga.',
                badges=['Máquinas Térmicas', 'Bancada de Refrigeração', 'CEAR'],
                git='https://github.com/LinconRozendo',
                dark=True,
            ),
            # dashcard do dash estacao
            dtc.Card(
                id='card3',
                openNewTab = False,
                link='/modo_bypass',
                image='./assets/images/bypass.jpg',
                title='Modo Operacional - ByPass',
                description='Descubra os aspectos do modo operacional Bypass da bancada de refrigeração ET 420 através de um diagrama explicativo.\
                    O diagrama oferece uma compreensão inicial de como o sistema de Bypass direciona o fluxo de ar para controlar a temperatura em \
                        situações específicas. Explore como a bancada utiliza o modo Bypass.',
                badges=['Máquinas Térmicas', 'Bancada de Refrigeração', 'CEAR'],
                git='https://github.com/LinconRozendo',
                dark=True,
            ),
        ], id="page-content2"), 
    else:
        raise PreventUpdate


@app.callback(Output('page-content', 'children', allow_duplicate=True),
            Input('button2', 'n_clicks'),
            Input('button3', 'n_clicks'),
            Input('button4', 'n_clicks'),
            prevent_initial_call = True)
def display_page(clicks, clicks2, clicks3):

    if clicks > 0:
        return dashboard_components.layout
    elif clicks2 > 0:
        return dashboard_app.layout
    elif clicks3 > 0:
        return dashboard_equipe.layout
    else:
        raise PreventUpdate



if __name__ == '__main__':
    app.title = "BANCADA DE REFRIGERAÇÃO"
    app.update_title = None
    app.run_server(debug=True)
    app.config.suppress_callback_exceptions = True




    