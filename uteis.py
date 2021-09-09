import os
import sqlite3


def existe_banco(arquivo):
    """Verifica se existe o arquivo .db"""
    try:
        a = open(arquivo, "r")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def db_con(db):
    """Conexão com banco de dados"""
    banco = sqlite3.connect(db)
    cursor = banco.cursor()
    return banco, cursor

def criar_banco(arquivo):
    """Cria banco de dados"""
    banco, cursor = db_con(arquivo)

    cursor.execute("CREATE TABLE 'conta' ("
                   "'id'	INTEGER NOT NULL UNIQUE,"
                   "'nome'	TEXT NOT NULL,"
                   "'valor'	REAL NOT NULL,"
                   "'data'	TEXT NOT NULL UNIQUE,"
                   "'parcelas'	INTEGER,"
                   "'juros'	INTEGER,"
                   "'observações'	TEXT,"
                   "PRIMARY KEY('id' AUTOINCREMENT));"
    )
    cursor.close()
    banco.close()

def insercao(db):
    """Fazer cadastro de usuarios"""
    nome = str(input("Nome da conta:")).strip()
    valor = float(input("Valor a pagar:"))
    vencimento = str(input("Data de vencimento:")).strip()
    parcelas = int(input("Qtd. parcelas:"))
    juros = float(input("porcentagem de juros caso vença:"))
    obs = str(input("Anotação sobre a conta: (opcional)")).strip()
    try:
        banco, cursor = db_con(db)
        cursor.execute(f"INSERT INTO conta ('nome', 'valor', 'data', 'parcelas', 'juros', 'observações') "
                       f"VALUES('{nome}','{valor}','{vencimento}','{parcelas}','{juros}','{obs}');")
    except sqlite3.IntegrityError as e:
        color_msg(f"Erro de banco: {e}", 1)
        input("Pressione enter")
    except Exception as e:
        color_msg(f"Erro do tipo: [{e}]", 1)
        input("Pressione enter")
    else:
        banco.commit()
        color_msg("Cadastro feito com sucesso!", 2)
        input("Pressione enter")
    finally:
        cursor.close()
        banco.close()

def consulta_nome(db):
    """Lista as contas do banco por nome."""
    limpaTela()
    nome = str(input("Digite o nome da conta:\n"))
    try:
        banco, cursor = db_con(db)
        cursor.execute(f"SELECT * FROM conta WHERE nome = '{nome}'")
        resultado = cursor.fetchall()
    except Exception as e:
        print(f"Erro: [{e}]")
    else:
        listagem(resultado)
    finally:
        cursor.close()
        banco.close()

def consulta_data(db):
    """Listar as contas do banco por data."""
    os.system("cls")
    data = str(input("Digite a data [xx/xx/xx] :\n"))
    try:
        banco, cursor = db_con(db)
        cursor.execute(f"SELECT * FROM conta WHERE data = '{data}'")
        resultado = cursor.fetchall()
    except Exception as e:
        print(f"Erro: [{e}]")
    else:
        listagem(resultado)
    finally:
        cursor.close()
        banco.close()

def consulta_todos(db):
    """Listar as contas do banco."""
    try:
        banco, cursor = db_con(db)
        cursor.execute("SELECT * FROM conta")
        resultado = cursor.fetchall()
    except Exception as e:
        print(f"Erro! [{e}]")
    else:
        print('+', '-' * 107, '+')
        print(
            f"| {'Índice':^8}|{'id':^4}|{'Conta':^10}|{'Valor':^10}|{'Data':^10}|{'Parcelas':^10}|{'Juros':^7}| {'Observação':^40} |")
        print('+', '-' * 107, '+')
        for x, y in enumerate(resultado):
            print(f"| {x + 1:^8}|{y[0]:>4}|{y[1]:^10}|R$ {y[2]:^7.2f}|{y[3]:^10}|{y[4]:^10}|%{y[5]:^6}| {y[6]:^40} |")
        print('+', '-' * 107, '+')
        input("\nPressione enter")
    finally:
        cursor.close()
        banco.close()

def excluir(db):
    """Exclui dados de uma conta do banco."""
    numero = int(input("Digite o ID da conta a ser excluída. Digite 0 para sair:\n"))
    if numero == 0:
        pass
    else:
        try:
            banco, cursor = db_con(db)
            cursor.execute(f"SELECT * FROM conta WHERE id = '{numero}'")
            resultado = cursor.fetchall()
        except Exception as e:
            print(f"Erro: [{e}]")
        else:
            listagem(resultado)
            escolha = str(input("Tem certeza que quer excluir todos os dados dessa conta? [s/n]\n")).strip().lower()
            if escolha == 's':
                try:
                    cursor.execute(f"DELETE FROM conta WHERE id = '{numero}'")
                except Exception as e:
                    print(f"Erro: [{e}]")
                else:
                    print("Exclusão completa!")
        finally:
            cursor.close()
            banco.close()

def listagem(resultado):
    """laço for para listar a aconsulta no banco de dados."""
    print('+', '-' * 102, '+')
    print(
        f"| {'Índice':^8}|{'Conta':^10}|{'Valor':^10}|{'Data':^10}|{'Parcelas':^10}|{'Juros':^7}| {'Observação':^40} |")
    print('+', '-' * 102, '+')
    for x, y in enumerate(resultado):
        print(f"| {x + 1:^8}|{y[1]:^10}|R$ {y[2]:<7.2f}|{y[3]:^10}|{y[4]:^10}|%{y[5]:^6}| {y[6]:^40} |")
    print('+', '-' * 102, '+')
    input("\nPressione enter")

def color_msg(txt, cor):
    """
    txt = texto a ser exibido
    cor = numero da cor para o texto
    """

    if cor == 1:
        # vermelho
        i = '\033[;31m'

    elif cor == 2:
        # verde
        i = '\033[;32m'

    elif cor == 3:
        # amarelo
        i = '\033[;33m'

    elif cor == 4:
        # azul
        i = '\033[;34m'

    elif cor == 5:
        # lilas/roxo
        i = '\033[;35m'

    elif cor == 6:
        # ciano
        i = '\033[;36m'

    elif cor == 7:
        # cinza
        i = '\033[;37m'

    print(f"{i}{txt}\033[m")

def limpaTela():
    comando = 'clear'
    if os.name in ('nt', 'dos'):
        comando = 'cls'
    os.system(comando)

