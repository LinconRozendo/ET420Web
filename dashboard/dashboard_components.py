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
                "Componentes",
                id='h1Title'
            ),
            html.H2(
                "Explore de forma concisa o funcionamento dos componentes fundamentais do Acumulador de Gelo e Refrigeração ET 420\
                     nesta seção. Descubra informações essenciais sobre os componentes presentes na bancada de refrigeração e seu papel no\
                         sistema.",               
                id='h2ComponentesIntro',
            ),
            html.H1(
                "Bomba de Circulação",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "As bombas de circulação são dispositivos fundamentais para movimentar líquidos ou gases em sistemas fechados, gerando\
                     fluxo e facilitando a circulação do fluido. Elas desempenham um papel essencial em uma variedade de aplicações, como\
                         sistemas de aquecimento, ventilação e ar condicionado, refrigeração, abastecimento de água em residências e edifícios,\
                             sistemas de irrigação agrícola, entre outros.",               
                    id='h2ModoCarga',
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/bomba_circulacao.png",
                                id='components#fig',
                            ),
                    html.H5(
                                ["Bomba de Circulação."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Essas bombas operam convertendo energia mecânica em energia hidráulica, gerando pressão que impulsiona o fluido através\
                         de tubulações ou canais específicos. Existem diversos tipos de bombas de circulação, incluindo bombas centrífugas,\
                             de deslocamento positivo e de fluxo axial, cada uma com suas características e aplicações particulares.",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "Na bancada ET 420, encontramos as seguintes bombas: ",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "P1: Circula o fluido que passa pela torre de resfriamento seca e pelo estágio intermediário;",               
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "P2: Circula a mistura água-propileno glicol que passa pelo tanque de gelo e pelo sistema de resfriamento;",                
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "P3: Circular o fluido que passa antes do estágio intermediário e pelo trocador de calor 𝑊7;",                
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "P4: Circular a água que passa pela torre de resfriamento úmida.",                
                    id='h2ModoCargaList',
                )
            ], id='components#fig'),      
            #########################################
            html.H1(
                "Compressor",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "O compressor é um dispositivo projetado para aumentar a pressão de um fluido, seja líquido ou gás, operando pela\
                         redução do volume do fluido. Isso é alcançado através da remoção de partículas de ar ou gás para aumentar sua\
                             densidade e, consequentemente, sua pressão. Os compressores são amplamente utilizados em uma variedade de\
                                 aplicações industriais, comerciais e domésticas, incluindo compressores de ar em ferramentas pneumáticas,\
                                     compressores de gás em processos industriais e sistemas de refrigeração.",               
                    id='h2ModoCarga',
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/compressor.png",
                                id='components#fig',
                            ),
                    html.H5(
                                ["Compressor."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Na bancada ET 420, um compressor de pistão acionado eletricamente (V) é utilizado para comprimir o fluido de trabalho\
                         vaporizado. Esta unidade é totalmente hermética, com o motor elétrico e o compressor alojados em um invólucro soldado\
                             à prova de gás.",               
                    id='h2ModoCarga',
                ),
            ], id='components#fig'),  
            ############################################################
            html.H1(
                "Condensador",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "O condensador desempenha um papel crucial nos sistemas de ar condicionado e refrigeradores, removendo calor do\
                         sistema. Ele recebe o refrigerante na forma de vapor de alta pressão e alta temperatura, proveniente do compressor,\
                             e tem como objetivo condensar esse vapor refrigerante de volta ao estado líquido, liberando calor para o ambiente.\
                                 Essencial para o funcionamento eficiente dos sistemas de refrigeração, o condensador é responsável por remover\
                                     o calor do refrigerante, permitindo que o ciclo de refrigeração prossiga.",               
                    id='h2ModoCarga',
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/Condensador.jpg",
                                id='components#fig',
                            ),
                    html.H5(
                                ["Condensador."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Existem diferentes tipos de condensadores usados em sistemas de refrigeração:",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "Condensador a ar: o calor do refrigerante é transferido para o ar ambiente, resfriando-o sobre as bobinas do condensador;",               
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "Condensador a água: a água é usada como meio de resfriamento, resfriando o refrigerante que circula dentro do condensador;",                
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "Condensador evaporativo: o processo de evaporação da água é utilizado para resfriar o refrigerante, evaporando a água pulverizada dentro do condensador.",
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "Na bancada ET 420, o fluido de trabalho vaporizado, comprimido e aquecido no processo, é resfriado e condensado em um\
                         trocador de calor de feixe de tubos.",               
                    id='h2ModoCarga',
                ),
            ], id='components#fig'),
            #########################################################################
            html.H1(
                "Depósito de Gelo",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "A unidade de armazenamento de gelo desempenha um papel crucial na manutenção de temperaturas específicas, mesmo\
                         em situações de falha no sistema de refrigeração. Além disso, atua como componente estratégico para reduzir a\
                             carga máxima no sistema, armazenando eficientemente energia de resfriamento. Na configuração da bancada, a\
                                 refrigeração do armazém de gelo é mantida por meio de um trocador de calor, onde o refrigerante é resfriado\
                                     durante o processo de refrigeração.",               
                    id='h2ModoCarga',
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/deposito de gelo.webp",
                                id='components#fig',
                            ),
                    html.H5(
                                ["Depósito de Gelo."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Ao fornecer energia de resfriamento para congelar a água, a unidade utiliza um tubo em espiral por onde flui a mistura de\
                         glicol-água como meio de armazenamento. Diferentemente do método de vaporização direta, onde o refrigerante passa\
                             diretamente pelo tubo em espiral, a vaporização ocorre de maneira indireta. Durante o processo de descarregamento,\
                                 a transferência de calor se dá diretamente do gelo para a mistura de glicol-água que flui pelo tubo em espiral.\
                                     Devido à má condução térmica do gelo, o desempenho diminui com o aumento da espessura do gelo, resultando\
                                         em um certo grau de autorregulação contra o congelamento completo.",               
                    id='h2ModoCarga',
                ),
            ], id='components#fig'),
            ########################################################################
            html.H1(
                "Evaporador",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "No ciclo de refrigeração, o evaporador é um dos quatro principais componentes do sistema, junto com o compressor,\
                         condensador e válvula de expansão. Sua função é absorver o calor do ambiente a ser refrigerado, seja uma sala,\
                             compartimento de um refrigerador doméstico ou uma seção de um sistema de ar condicionado.",               
                    id='h2ModoCarga',
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/evaporador.png",
                                id='components#fig',
                            ),
                    html.H5(
                                ["Evaporador."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "O processo básico de funcionamento do evaporador em um ciclo de refrigeração é o seguinte:",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "Recebimento de refrigerante líquido: o evaporador recebe refrigerante líquido de baixa pressão e baixa temperatura da\
                         válvula de expansão, após passar pelo condensador onde liberou calor para o ambiente externo;",               
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "Absorção de calor: o refrigerante líquido entra no evaporador e entra em contato direto com o ambiente a ser resfriado.\
                         À medida que circula pelo evaporador, absorve o calor do ambiente, causando sua evaporação;",                
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "Mudança de estado: durante a absorção de calor, o refrigerante líquido muda de estado para vapor de baixa pressão,\
                         sendo aspirado de volta para o compressor;",
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "Retorno ao compressor: o vapor refrigerante de baixa pressão é aspirado pelo compressor, onde é comprimido para aumentar\
                         sua pressão e temperatura, reiniciando o ciclo.",
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "O evaporador é geralmente um trocador de calor do tipo serpentina ou aletado, projetado para maximizar a transferência\
                         de calor entre o refrigerante e o ar ou líquido que está sendo resfriado. É uma peça essencial para o funcionamento\
                             eficiente do sistema de refrigeração ou ar condicionado, pois é onde ocorre a remoção eficaz do calor do ambiente\
                                 que está sendo refrigerado.",               
                    id='h2ModoCarga',
                ),
            ], id='components#fig'),
            ####################################################################
            html.H1(
                "Rotâmetro",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "O rotâmetro, conhecido como medidor de vazão de área variável, é um dispositivo utilizado para medir o fluxo de um\
                         fluido em um sistema. Ele é composto por um tubo transparente vertical com uma área de seção transversal variável,\
                             onde o fluido entra e causa o deslocamento de um flutuador ou esfera dentro do tubo. A altura do flutuador ou\
                                 esfera é proporcional ao fluxo do fluido.",               
                    id='h2ModoCarga',
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/rotometro.png",
                                id='components#fig',
                            ),
                    html.H5(
                                ["Rotâmetros."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Sua principal característica é a capacidade de indicar visualmente a taxa de fluxo, pois o flutuador ou esfera se movem\
                         para cima ou para baixo conforme o fluxo varia. Geralmente, uma escala graduada ao longo do tubo permite que o operador\
                             leia a taxa de fluxo diretamente.",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "Os rotâmetros são utilizados em uma variedade de aplicações industriais, laboratoriais e de processos, onde a medição\
                         precisa do fluxo de líquidos ou gases é essencial. No entanto, é importante notar que eles têm limitações em termos\
                             de precisão, especialmente em condições de fluxo turbulento ou pulsante.",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "Na bancada ET 420, os seguintes rotâmetros são utilizados:",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "F1: Medição da vazão do fluido refrigerante R134A no ciclo de refrigeração;",               
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "F2: Medição da vazão da mistura água-propilenoglicol depois do estágio intermediário 𝐵2 que vai para a torre de resfriamento seca;",                
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "F3: Medição da vazão da mistura água-propilenoglicol que passa pelo trocador de calor 𝑊6;",
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "F4: Medição da vazão da mistura água-propilenoglicol antes do estágio intermediário, fluido que passa pelo trocador de calor de casco e tubo 𝑊7;",
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "F5: Medição da vazão da mistura água-propilenoglicol depois do estágio intermediário que vai para a torre de resfriamento úmida.",
                    id='h2ModoCargaList',
                ),
            ], id='components#fig'),
            #########################################################################
            html.H1(
                "Torre de Resfriamento",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "As torres de resfriamento desempenham um papel fundamental na dissipação de calor da água em diversos sistemas,\
                         como usinas de geração de energia, sistemas de refrigeração e trocadores de calor. Elas são projetadas para resfriar\
                             a água de forma eficiente, permitindo sua reutilização e proporcionando benefícios ambientais e econômicos.",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "Na torre de resfriamento, a água quente entra na parte superior e percorre a estrutura, trocando calor e massa com o ar.\
                         Isso resulta na evaporação parcial da água, o que proporciona o resfriamento desejado. Um ventilador localizado no\
                             topo da torre remove o ar saturado, contribuindo para o processo de resfriamento. A eficiência da transferência\
                                 de calor depende da diferença de temperatura entre a água e o ar ambiente.",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "A configuração da bancada permite a integração de torres de resfriamento úmido ou a seco no circuito de estágio\
                         intermediário. Essas torres têm a capacidade de tanto aquecer quanto retirar calor da mistura utilizada no sistema,\
                             oferecendo flexibilidade operacional.",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "Torre de Resfriamento a Seco",
                    id='h1NomeComponentesTorres'
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/tore_seca (1).png",
                                id='components#fig',
                            ),
                    html.H5(
                                ["Torre de Resfriamento a Seco."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "As torres de resfriamento a seco operam em circuito fechado, isolando o fluido de resfriamento do ar ambiente.\
                         A transferência de calor ocorre por convecção, sem envolver evaporação.",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "Torre de Resfriamento Úmido",
                    id='h1NomeComponentesTorres'
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/torre_umida.png",
                                id='components#fig',
                            ),
                    html.H5(
                                ["Torre de Resfriamento Úmido."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Já as torres de resfriamento úmido operam em um circuito aberto, permitindo que a água quente seja resfriada abaixo\
                         da temperatura de bulbo seco do ar ambiente, especialmente em condições de ar seco.",               
                    id='h2ModoCarga',
                ),
            ], id='components#fig'), 
            ###########################################################################
            html.H1(
                "Válvula de Expansão",
                id='h1NomeComponentes'
            ),
            html.Div([
                html.H2(
                    "A válvula de expansão desempenha um papel fundamental no ciclo de refrigeração, regulando o fluxo de refrigerante líquido\
                         para o evaporador, onde ocorre a absorção de calor do ambiente a ser resfriado. Sua função é controlar a taxa de fluxo\
                             de refrigerante líquido que entra no evaporador, mantendo pressão e temperatura adequadas para otimizar a \
                                transferência de calor. Isso é essencial para garantir a eficiência do ciclo de refrigeração.",               
                    id='h2ModoCarga',
                ),
                html.Div([
                    html.Img(
                                src="./assets/images/valvula.png",
                                id='components#fig',
                            ),
                    html.H5(
                                ["Válvula de Expansão."], 
                                className="legendaImg",
                                style={
                                    "text-align": "center",
                                },
                            ),
                ], id='ImgComponentes'),
                html.H2(
                    "Existem diferentes tipos de válvulas de expansão:",               
                    id='h2ModoCarga',
                ),
                html.H2(
                    "Válvula de expansão termostática (TXV): controlada pela temperatura do refrigerante no evaporador, ajusta o fluxo de \
                        refrigerante conforme necessário.",               
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "Válvula de expansão eletrônica (EEV): controlada eletronicamente, ajusta continuamente o fluxo com base em dados de\
                         temperatura e pressão do sistema.",                
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "Válvula de expansão manual: ajustada manualmente para controlar o fluxo de refrigerante, sendo menos comum\
                         em sistemas modernos.",
                    id='h2ModoCargaList',
                ),
                html.H2(
                    "Na bancada de refrigerção, é utilizada uma válvula de expansão termostática que regula o fluxo com base na temperatura\
                         de saída do evaporador, medida por um sensor de temperatura. Isso evita que o refrigerante não vaporizado entre no\
                             compressor, prevenindo danos ao sistema. É importante observar que, nos diagramas da bancada, várias válvulas com\
                                 funções distintas são representadas, mas na bancada ET 420 há apenas uma válvula de expansão no circuito de\
                                     refrigeração, indicada como V8.",
                    id='h2ModoCarga',
                ),
            ], id='components#fig'),
            #####################################################################
            html.Br(),
            html.H2(
                    "Ficou com dúvida sobre algum componente ou sobre seu funcionamento?  Deseja entender melhor as configurações da bancada de refrigeração?",               
                    id='h2ModoCarga',
            ),
            html.H2(
                    "Para mais informações referente aos componentes apresentados e sobre a Bancada de Refrigeração ET 420. \nVisite: ",               
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


@app.callback(Output('page-content', 'children', allow_duplicate=True),
                Input('buttonHome', 'n_clicks'),
                prevent_initial_call = True)
def display_page(clicks):
    
    if clicks > 0:
        pyautogui.press('f5')
    else:
        raise PreventUpdate