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
                "Aplicações",
                id='h1Title'
            ),
            html.H2(
                "Bem-vindo à nossa página dedicada a explorar as aplicações diversificadas dos sistemas de refrigeração. Aqui, você\
                     encontrará uma variedade de informações sobre como os sistemas de refrigeração são utilizados em diferentes setores,\
                         desde a indústria alimentícia até a comunidade universitária. Explore conosco as inúmeras maneiras pelas quais a refrigeração\
                             impacta nosso dia-a-dia e impulsiona avanços em várias áreas.",               
                id='h2ComponentesIntro',
            ),
            html.H1(
                "LABRADS - CEAR/UFPB",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "No contexto do Laboratório de Refrigeração por Adsorção (LABRADS), a presença de um sistema de refrigeração é essencial\
                         para apoiar tanto a pesquisa científica quanto o ensino prático e laboratorial. Os laboratórios desempenham um papel\
                             crucial na formação dos alunos, proporcionando experiências tangíveis em ciências naturais e exatas. Com um\
                                 sistema de refrigeração adequado, o LABRADS possibilita realizar experimentos que não apenas ilustram os conceitos\
                                     teóricos, mas também promovem uma aprendizagem prática e eficaz.",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "Além disso, o LABRADS representa centro de pesquisa avançada e inovação, nos quais são conduzidos\
                         estudos pioneiros em diversas áreas. Um sistema de refrigeração confiável é essencial para sustentar a realização\
                             de experimentos complexos e a busca por descobertas científicas inovadoras. Ao manter condições controladas de\
                                 temperatura, o sistema de refrigeração permite que os pesquisadores conduzam seus estudos com precisão e\
                                     confiabilidade, contribuindo para o avanço do conhecimento científico e tecnológico.",               
                    id='h2ModoCarga',
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/bancada_et420.png",
                                id='components#figBancada',
                            ),
                    html.H5(
                                ["Bancada de Refrigeração ET 420."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "A bancada de estudo ET 420 é essencial para a aprendizagem prática de sistemas de refrigeração e estudos termodinâmicos\
                         sobre troca de calor. Com seus componentes específicos, como compressor e evaporador, os alunos exploram conceitos\
                             teóricos na prática, adquirindo compreensão profunda dos processos de refrigeração e preparando-se para desafios\
                                 reais na indústria e na pesquisa acadêmica.",               
                    id='h2ModoCarga',
                ),
            ], id='components#fig'),      
            #########################################
            html.H1(
                "Refrigeração Doméstica",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "A refrigeração doméstica, embora abrangendo principalmente a produção de refrigeradores e freezers para uso residencial,\
                         desempenha um papel essencial no cotidiano das pessoas. Além dos equipamentos tradicionais, inclui também sistemas de\
                             ar condicionado voltados para residências, proporcionando conforto térmico durante os períodos de calor intenso.\
                                 Esses dispositivos são projetados para atender às necessidades específicas dos lares, garantindo a conservação\
                                     adequada de alimentos e a criação de ambientes internos confortáveis.",               
                    id='h2ModoCarga',
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/refrigeracao_domestica.webp",
                                id='components#figBancada',
                            ),
                    html.H5(
                                ["Refrigerador doméstico."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Com o crescente número de unidades em funcionamento em domicílios ao redor do mundo, a refrigeração doméstica se\
                         destaca como uma parte significativa da indústria de refrigeração. As unidades destinadas ao uso doméstico são\
                             geralmente compactas e hermeticamente fechadas, apresentando potências nominais entre 1/20 e 1/2 CV. Essa\
                                 característica permite que operem de forma eficiente e silenciosa, atendendo às demandas dos consumidores\
                                     por praticidade e economia de energia. Dessa forma, a refrigeração residencial não apenas representa\
                                         uma parcela importante da indústria, mas também desempenha um papel vital na qualidade de vida e no\
                                             conforto dos lares modernos.",               
                    id='h2ModoCarga',
                ),
            ], id='components#fig'),
            #####################################################################
            html.H1(
                "Refrigeração Doméstica",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "A refrigeração comercial é uma área abrangente que engloba o projeto, a instalação e a manutenção de uma variedade de\
                         instalações refrigeradas. Essas instalações são amplamente utilizadas por lojas comerciais, restaurantes, hotéis\
                             e em locais de armazenamento, exposição, beneficiamento e distribuição de mercadorias perecíveis de todos os\
                                 tipos. Além disso, a refrigeração comercial desempenha um papel crucial na preservação da qualidade e da\
                                     segurança dos produtos alimentícios ao longo de toda a cadeia de suprimentos, desde a produção até o\
                                         consumo final.",               
                    id='h2ModoCarga',
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/refrigeracao_comercial.webp",
                                id='components#figBancada',
                            ),
                    html.H5(
                                ["Refrigeradores comerciais."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Os sistemas de refrigeração comercial são projetados para atender às exigências específicas de cada aplicação, levando\
                         em consideração fatores como o volume de produtos a serem refrigerados, as condições ambientais e as regulamentações\
                             sanitárias. Eles variam desde pequenos freezers em supermercados até grandes câmaras frigoríficas em centros de\
                                 distribuição de alimentos. Além disso, a refrigeração comercial está em constante evolução, incorporando\
                                     tecnologias mais eficientes e sustentáveis, como sistemas de refrigeração de baixo impacto ambiental\
                                         e dispositivos de monitoramento remoto para garantir o controle preciso da temperatura e a eficiência\
                                             energética.",               
                    id='h2ModoCarga',
                ),
            ], id='components#fig'),
            ######################################################################
            html.H1(
                "Refrigeração Industrial",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "A refrigeração industrial, muitas vezes confundida com a refrigeração comercial, abrange uma gama diversificada de\
                         aplicações que são distintas em tamanho e complexidade. Enquanto as aplicações comerciais geralmente atendem a\
                             estabelecimentos de varejo, restaurantes e hotéis, as aplicações industriais são predominantemente encontradas\
                                 em grandes instalações de processamento de alimentos, como fábricas de gelo, instalações de empacotamento\
                                     de produtos alimentícios, cervejarias e fábricas de laticínios.",               
                    id='h2ModoCarga',
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/refrigeracao_industrial.jpg",
                                id='components#figBancada',
                            ),
                    html.H5(
                                ["Sistema de refrigeração industrial."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Além disso, a refrigeração industrial se estende para além do setor alimentício e abrange uma variedade de indústrias,\
                         como refinarias de óleo, fábricas de produtos químicos e instalações de fabricação de produtos de borracha. Além das\
                             aplicações convencionais, a refrigeração industrial também desempenha um papel importante na indústria da\
                                 construção, onde técnicas de congelamento do solo são empregadas em escavações e o resfriamento de grandes\
                                     massas de concreto é essencial para controlar a reação exotérmica durante o processo de cura.",               
                    id='h2ModoCarga',
                ),
            ], id='components#fig'),
            #######################################################################
            html.H1(
                "Refrigeração Marítima e de Transporte",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "A refrigeração marítima desempenha um papel crucial na preservação de alimentos e produtos perecíveis durante o transporte marítimo.\
                         Ela abrange uma variedade de aplicações, desde barcos de pesca até grandes navios de transporte de carga refrigerada. Esses\
                             sistemas de refrigeração garantem que os alimentos e mercadorias permaneçam frescos e seguros durante as viagens marítimas,\
                                 atendendo às demandas da indústria pesqueira, do comércio internacional e da logística de suprimentos.",               
                    id='h2ModoCarga',
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/refrigeracao_transporte.jpeg",
                                id='components#figBancada',
                            ),
                    html.H5(
                                ["Equipamento de transporte comercial com refrigeração."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Por outro lado, a refrigeração de transporte é essencial para manter a integridade e a qualidade dos produtos durante\
                         o transporte terrestre. Esses sistemas são aplicados em caminhões e vagões ferroviários refrigerados, tanto para\
                             viagens de longa distância quanto para entregas locais. Ao controlar a temperatura e a umidade, a refrigeração\
                                 de transporte assegura que os alimentos e produtos sensíveis permaneçam em condições ideais, desde a origem\
                                     até o destino final, garantindo a qualidade e a segurança dos produtos ao longo da cadeia de suprimentos.",               
                    id='h2ModoCarga',
                ),
            ], id='components#fig'),
            ########################################################################
            html.Br(),
            html.H2(
                    "Para mais informações referente ao conteúdo apresentado e sobre a Bancada de Refrigeração ET 420. \nVisite: ",               
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
    ],   id='page-content1'),
])


@app.callback(Output('page-content1', 'children', allow_duplicate=True),
                Input('buttonHome', 'n_clicks'),
                prevent_initial_call = True)
def display_page(clicks):

    if clicks > 0:
        pyautogui.press('f5')
    else:
        raise PreventUpdate


