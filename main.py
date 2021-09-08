import uteis
import os


db = "banco.db"
if not uteis.existe_banco(db):
    uteis.criar_banco(db)
while True:
    os.system('cls || clear')
    menu = int(input("[1] Inserir conta\n"
                     "[2] Pesquisar por nome\n"
                     "[3] Pesquisar por data de vencimento\n"
                     "[4] Pesquisar tudo\n"                     
                     "[5] Excluir conta\n"
                     "[6] sair\n"))
    if menu == 1:
        # Inserção
        uteis.insercao(db)
    elif menu == 2:
        # pesquisa por nome
        os.system("cls")
        uteis.consulta_nome(db)
    elif menu == 3:
        # pesquisa por data
        uteis.consulta_data(db)
    elif menu == 4:
        uteis.consulta_todos(db)
    elif menu == 5:
        # Excluir no banco
        uteis.excluir(db)
    elif menu == 6:
        break
    else:
        print("Número inválido!")
print("Bye!")
