import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import dash_trich_components as dtc
from flask import Flask
from app import app
import pyautogui




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
        html.Div([
            dbc.Button("Home", color="primary", size="lg", className="me-1", id='buttonHome', n_clicks=0),
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
            html.H1(
                "Sobre Nós",
                id='h1Title'
            ),
            html.H2(
                "Bem-vindo à nossa página 'Sobre nós'! Somos estudantes do curso de Engenharia de Energias Renováveis da Universidade Federal da Paraíba (UFPB) e estamos \
                 empolgados em compartilhar informações sobre nosso projeto para a disciplina de Máquinas Térmicas. Nesta página, você \
                     encontrará detalhes sobre nossa equipe e o propósito do projeto.",               
                id='h2ComponentesIntro',
            ),
            html.H1(
                "Máquinas Térmicas",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "A disciplina de Máquinas Térmicas é ministrada pelo Dr. Adriano da Silva Marques, um profissional com ampla experiência\
                         no setor industrial de Engenharia Mecânica. Com passagens por empresas renomadas como Petrobras e Ford, o Dr. Marques\
                             traz consigo um conhecimento prático e teórico valioso para os alunos. Recentemente, ele se uniu ao corpo docente\
                                 do Centro de Energias Alternativas e Renováveis da UFPB, trazendo sua expertise para enriquecer o ensino e\
                                     contribuir para o desenvolvimento acadêmico dos estudantes. Recentemente o Dr. Adriano da Silva Marques\
                                         passou a ministrar a disciplina de Máquinas Térmicas, proporcionando aos alunos uma visão abrangente\
                                             e atualizada sobre o tema.",               
                    id='h2ModoCarga',
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/adriano.png",
                                id='components#figEquipe',
                            ),
                    html.H5(
                                ["Dr. Adriano da Silva Marques."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                #########################################
                html.H1(
                    "Projeto",
                    id='h1NomeComponentes'
                ),
                html.H2(
                    "Como primeira atividade da disciplina de Máquinas Térmicas, os alunos receberam a tarefa de criar um relatório detalhado\
                         sobre a Bancada de Refrigeração ET 420, abordando tópicos como o guia prático de uso do equipamento, a identificação\
                             objetiva dos defeitos, um orçamento detalhado para reparos e melhorias, e a descrição das soluções propostas.\
                                 Empenhados em agregar valor ao projeto, a equipe de alunos percebeu a oportunidade de desenvolver uma\
                                     aplicação web para consolidar as informações coletadas ao longo do desenvolvimento do relatório sobre\
                                         a bancada. Essa iniciativa demonstra o comprometimento dos alunos em explorar recursos tecnológicos\
                                             para enriquecer a experiência de aprendizado e facilitar o acesso às informações relevantes para\
                                                 a disciplina.",               
                    id='h2ModoCarga',
                ),
            ], id='components#fig'),      
            #########################################
            html.H1(
                "Equipe de Desenvolvimento",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "A nossa equipe é composta pelo seguintes graduandos do curso de Engenharia de Energias Renováveis da UFPB:",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "Júlia Alves Santos",
                    id='h1NomeComponentesTorres'
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/julia_a.jpg",
                                id='components#figEquipe',
                            ),
                    html.H5(
                                ["Júlia Alves Santos."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Júlia Alves Santos é integrante do grupo de pesquisadores da Unidade Embrapii no Centro de Energias Alternativas\
                         e Renováveis da UFPB, e também contribui para o projeto Multi-Mapa PB. Suas áreas de atuação como pesquisadora\
                             englobam Ciência de Dados, Georreferenciamento e Termodinâmica, demonstrando um perfil multidisciplinar e\
                                 engajado na busca por soluções inovadoras e sustentáveis.",               
                    id='h2ModoCarga',
                ),
            ], id='components#fig'),
            #####################################################################
            html.H2(
                    "Júlia de Sousa Ribeiro",
                    id='h1NomeComponentesTorres'
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/julia_r.jpg",
                                id='components#figEquipe',
                            ),
                    html.H5(
                                ["Júlia de Sousa Ribeiro."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Júlia de Sousa Ribeiro é bolsista do Projeto de Extensão 'Paraíba Solar: A Importância da Energia Solar Fotovoltaica para\
                         o Nordeste Brasileiro'. Suas áreas de atuação como pesquisadora incluem Energias Renováveis e Energia Fotovoltaica,\
                             refletindo seu comprometimento com a pesquisa e o desenvolvimento de soluções sustentáveis na área de energia.",               
                    id='h2ModoCarga',
                ),
            #####################################################################
            html.H2(
                    "Lincon Rozendo da Silva",
                    id='h1NomeComponentesTorres'
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/lincon.jpeg",
                                id='components#figEquipeLincon',
                            ),
                    html.H5(
                                ["Lincon Rozendo da Silva."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Lincon Rozendo da Silva é bolsista PIBIC no Projeto de 'Otimização de Sistemas de Abastecimento de Água Utilizando\
                         Técnicas de Inteligência Artificial e Computação em Nuvem'. Além disso, é bolsista de Desenvolvimento Tecnológico\
                             no Projeto 'Otimização de Sistemas de Energias Renováveis com Armazenamento de Alto Desempenho' e colabora\
                                 com o Projeto Multi-Mapa PB. Suas áreas de atuação como pesquisador abrangem Ciência de Dados, Inteligência\
                                     Computacional e Georreferenciamento, refletindo seu engajamento em pesquisas interdisciplinares\
                                         e inovadoras na área de tecnologia e energia.",               
                    id='h2ModoCarga',
                ),
            #####################################################################
            html.H2(
                    "Luan Txai Costa Santiago",
                    id='h1NomeComponentesTorres'
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/txai.jpg",
                                id='components#figEquipeLincon',
                            ),
                    html.H5(
                                ["Luan Txai Costa Santiago."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Luan Txai Costa Santiago participou ativamente da pesquisa que culminou no artigo 'As potencialidades energéticas\
                         do assentamento Dona Antônia'. O estudo concentra-se em apresentar as potencialidades energéticas de um assentamento,\
                             visando seu aproveitamento para consumo interno e possível venda à concessionária de energia, como forma de\
                                 incrementar a renda das famílias assentadas. Suas áreas de atuação incluem Energias Renováveis,\
                                     Sustentabilidade e Desenvolvimento Comunitário.",               
                    id='h2ModoCarga',
                ),
            #####################################################################
            html.H2(
                    "Lucas Dantas de Almeida",
                    id='h1NomeComponentesTorres'
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/lucas.jpg",
                                id='components#figEquipeLincon',
                            ),
                    html.H5(
                                ["Lucas Dantas de Almeida."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Lucas Dantas está atualmente engajado em pesquisa na área de análise de dados, com foco principal na investigação\
                         das influências de diversas bases de dados de irradiação solar na geração de energia elétrica por sistemas\
                             fotovoltaicos. Suas áreas de atuação incluem Análise de Dados, Energias Renováveis e Sistemas Fotovoltaicos.",               
                    id='h2ModoCarga',
                ),
            ###########################################################################
            html.H2(
                    "Yago Dantas Evagelista",
                    id='h1NomeComponentesTorres'
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/yago.jpg",
                                id='components#figEquipeLincon',
                            ),
                    html.H5(
                                ["Yago Dantas Evagelista."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Yago Dantas Evangelista está atualmente engajado em pesquisas na área de BESS (Battery Energy Storage System), com o\
                         objetivo de investigar e compreender os impactos desses sistemas nos transitórios que podem ocorrer nos sistemas\
                             elétricos. Seu foco recai especialmente em sistemas que são abastecidos por fontes renováveis de energia,\
                                 refletindo seu interesse na integração eficiente e sustentável de tecnologias de armazenamento de energia\
                                     em redes elétricas baseadas em energias renováveis.",               
                    id='h2ModoCarga',
                ),
            ######################################################################
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
    ],   id='page-content2'),
])


@app.callback(Output('page-content2', 'children'),
                Input('buttonHome', 'n_clicks'),
                prevent_initial_call = True)
def display_page(clicks):

    if clicks > 0:
        pyautogui.press('f5')
    else:
        raise PreventUpdate


