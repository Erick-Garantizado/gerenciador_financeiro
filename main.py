import PySimpleGUI as sg
import sqlite3


MES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
       'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
DIA = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']

banco = sqlite3.connect('conta_teste.db')
cursor = banco.cursor()

sg.theme('dark2')

# Layout de inserção
layout_insercao =  [
    [sg.T('')],
    [sg.T("Nome da conta:"), sg.In(key="-NOME_INSERCAO-")],
    [sg.T("Valor:"), sg.In(key="-VALOR_INSERCAO-", pad=((63),(0)))],
    [sg.T("Vencimento:"), sg.In(key="-DATA_INSERCAO-", pad=((24),(0))),
    sg.CalendarButton(' ... ', format='%d/%m/%Y', month_names=MES, day_abbreviations=DIA, image_filename='img/calendario.png')],
    [sg.T("Parcelas:"), sg.Spin([i for i in range(0,100)], key="-PARCELAS-", pad=((42),(0)), size=(5,1))],
    [sg.T("Juros:"), sg.Spin([i for i in range(0,100)], key="-JUROS-", pad=((62),(0)), size=(5,1))],
    [sg.T("Observações:"), sg.I(key="-OBS-", pad=((18),(0)))],
    [sg.T("_"*110)],
    [sg.T('')],
    [sg.B("Salvar")]
]

# Layout de consulta
layout_consulta = [
    [sg.T('')],
    [sg.T("Nome da conta:"), sg.In(key="-NOME_CONSULTA-")],
    [sg.T("Valor:"), sg.In(key="-VALOR_CONSULTA-", pad=((63),(0)))],
    [sg.T("Vencimento:"), sg.In(key="-DATA_CONSULTA-", pad=((24),(0))),
    sg.CalendarButton(' ... ', format='%d/%m/%Y', month_names=MES, day_abbreviations=DIA, image_filename='img/calendario.png')],
    [sg.T('')],
    [sg.B("Consultar"), sg.B("Consultar tudo")],
    [sg.T("_"*110)],   
    [sg.T('Nome da conta', pad=((50,0),(0))), sg.T('Detalhes', pad=((375,0),(40,0)))],
    [sg.Listbox('', k="-LISTA_CONSULTA-", size=(20,10), pad=((25,0),(0))),
    sg.B("Detalhes"),
    sg.Text('N°:\nNome:\nValor:\nQtd. parcelas:\nJuros (%):\nVencimento:\nObservação:\t',pad=((100,0),(0,0)), font='Helvetica 11'),
    sg.Listbox('', k='-LISTA_DETALHE-', size=(20,7), pad=((0),(2,0)))],
]

# Layout de exclusão
layout_exclusao = [
    [sg.T('')],
    [sg.T("Nome da conta:"), sg.In(k='-NOME_EXCLUSAO-')],
    [sg.T("Valor:"), sg.In(k='-VALOR_EXCLUSAO-', pad=((63),(0)))],
    [sg.T("Vencimento:"), sg.In(k='-DATA_EXCLUSAO-', pad=((24),(0))), 
    sg.CalendarButton(' ... ', format='%d/%m/%Y', month_names=MES, day_abbreviations=DIA, image_filename='img/calendario.png')],
    [sg.T('')],
    [sg.B("Pesquisar")],
    [sg.T('')],
    [sg.Listbox('', k="-LISTA_EXCLUSAO-", size=(20,10)),
    sg.T("Num. de ID:"), sg.In(size=(5, 1), k='-ID-'),
    sg.B("Excluir")]
]

# Tabs
layout = [
        [sg.TabGroup([
            [sg.Tab('Inserir', layout_insercao), 
             sg.Tab('Consulta', layout_consulta), 
             sg.Tab('Exclusão', layout_exclusao)]
        ], size=(680,500), pad=((500,0),(0)))
    ]
]

# Funções de listagem
def listagem(chave):
    lista = list()
    for x in resultado:
        lista.append(f"{x[1]}")
    window[chave].Update(lista)

def listagem_detalhe(chave):
    lista = list()
    # laço for listando as tuplas dentro da lista 'resultado'
    for x in resultado:
        # laço for listando os itens dentro de cada tupla
        for y in x:
            # se tipo do item é float
            if type(y) == type(0.0) :
                lista.append(f'R$ {y:.2f}'.replace('.',','))                
            else:
                lista.append(y)
    window[chave].Update(tuple(lista))
    
window = sg.Window('Gerenciador financeiro', layout, size=(700, 550))

# Loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    # Botão salvar
    if event == "Salvar":
        if str(values["-VALOR_INSERCAO-"]).isalpha():
            sg.popup_ok("Digite apenas o valor !")
        if values["-NOME_INSERCAO-"] == '' or values["-VALOR_INSERCAO-"] == '' or values["-DATA_INSERCAO-"] == '':
            sg.popup_ok("Os campos nome, valor e data nao podem estar vazios para essa operação!")
        else:
            try:
                cursor.execute(
                    f"""INSERT INTO conta (nome, valor, parcela, juros, data, observacao) """
                    f"""VALUES ('{values["-NOME_INSERCAO-"]}', '{values["-VALOR_INSERCAO-"]}', '{values["-PARCELAS-"]}',"""
                    f"""'{values["-JUROS-"]}', '{values["-DATA_INSERCAO-"]}', '{values["-OBS-"]}')"""
                )
            except Exception as e:
                sg.popup_error(f"Falha ao tentar salvar os dados.\nErro: [{e}]")
            else:
                sg.popup_ok("Conta salva!")
                banco.commit()   
    # Botão consultar
    elif event == "Consultar":
        try:
            cursor.execute(f"""SELECT * FROM conta WHERE nome='{values["-NOME_CONSULTA-"]}' or valor='{values["-VALOR_CONSULTA-"]}' or data='{values["-DATA_CONSULTA-"]}'""")
        except Exception as e:
            sg.popup_error(f"Erro: [{e}]")
        else:
            resultado = cursor.fetchall()            
            if resultado != []:
                listagem('-LISTA_CONSULTA-')
            else:
                sg.popup_ok("Sem resultados!")
                window.find_element('-LISTA_CONSULTA-').Update('')
    # Botão consultar tudo
    elif event == "Consultar tudo":
        try:
            cursor.execute(f"""SELECT * FROM conta""")
        except Exception as e:
            sg.popup_error(f"Erro: [{e}]")
        else:
            resultado = cursor.fetchall()
            if resultado != []:                
                listagem('-LISTA_CONSULTA-')
            else:                
                window.find_element('-LISTA_CONSULTA-').Update(["sem resultado"])
    # Botão detalhes
    elif event == "Detalhes":
        consultar_nome = values['-LISTA_CONSULTA-']
        try:
            cursor.execute(f"""SELECT * FROM conta WHERE nome= "{consultar_nome[0]}";""")
        except Exception as e:
            sg.popup_error(f"Erro: [{e}]")
        else:
            resultado = cursor.fetchall()           
            if len(resultado) > 0:
                listagem_detalhe('-LISTA_DETALHE-')
    # Botão pesquisar
    elif event == "Pesquisar":
        cursor.execute(f"SELECT * FROM conta WHERE nome='{values['-NOME_EXCLUSAO-']}' or valor='{values['-VALOR_EXCLUSAO-']}' or data='{values['-DATA_EXCLUSAO-']}'")
        resultado = cursor.fetchall()
        lista = list()
        for x in resultado:
            lista.append(f"\t {x[0]} | {x[1]}")
        window['-LISTA_EXCLUSAO-'].Update(lista)
    # Botão excluir
    elif event == "Excluir":
        cursor.execute(f"SELECT * FROM conta WHERE id='{values['-ID-']}'")
        resultado = cursor.fetchall()
        if resultado != []:
            PERGUNTA = f"Você tem certeza que quer excluir a conta de nome [{resultado[0][1]}] e valor [{resultado[0][2]}]"
            resposta = sg.popup_yes_no(PERGUNTA, title='')
            if resposta == "Yes":
                cursor.execute(f"DELETE FROM conta WHERE id='{values['-ID-']}'")
                banco.commit()
                sg.popup_ok("Conta excluida!")
        else:
            sg.popup_ok("Sem resultados!")
    