"""
objeto: contas, usuário.

Contas:
// atributos
° nome;
° valor;
° parcela; (algumas sao indeterminadas. ex.: conta de luz.)
° data;
° campo de observação;

// ações
podem ser excluidas;
vencem;
juros;

=================================================================

Usuário:
//atributos
nome;
senha;
salário;

// ações
cadastrar conta;
excluir conta;
pagar conta;
"""

class Contas:
    def __init__(self, usuario):
        self.usuario = usuario
        self.nome = ''
        self.valor = 0.0
        self.parcela = 0
        self._data = ''
        self._juros = None
        self.observação = ''
        self._status = 'amarelo'
        self._excluida = False

    def excluir(self):
        """Muda o status da conta para excluida."""
        self.excluida = True

    def vencer(self):
        """mudar cor para vermelho e cobrar juros."""
        self._status = 'vermelho'

    def _calcula_juros(self):
        """Calcula juros da conta."""
        pass


class Usuario:
    def __init__(self, nome, salario=0):
        self.nome = nome
        self.salario = salario

    def cadastrar_conta(self):
        """Insere uma conta para pagar."""
        pass

    def excluir_conta(self):
        """Exclúi uma conta."""
        pass

    def pagar_conta(self):
        """Paga uma conta."""
        pass
