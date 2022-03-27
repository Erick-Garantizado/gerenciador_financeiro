# gerenciador_financeiro

Programa básico para ordenar as contas a pagar. 
* Biblioteca: _PySimpleGUI_ 
* Banco de dados: _sqlite_

## Inserção de uma conta
![imagem1](https://user-images.githubusercontent.com/66915867/160293975-4b48accc-974e-42f8-a494-d156d457be07.PNG) \
Na rimeira tela o usuário preencherá o nome da conta, valor, vencimento, quantidades de parcelas, juros e observação. 
Os campos nome, valor e vencimento são obrigatórios.
Para inserir a data de vencimento basta clicar no icone de calendario ![image](https://user-images.githubusercontent.com/66915867/160294161-39c327c5-6e33-4fb8-b082-b7ca118017cc.png) 
e selecionar a data clicando no dia desejado
![image](https://user-images.githubusercontent.com/66915867/160294719-6c30f991-d551-4c70-99b6-a107ddcb425b.png) 

## Consultando uma conta
![image](https://user-images.githubusercontent.com/66915867/160294053-915e5054-d401-4316-b7d9-9ba4370b0a66.png) \
Para consultar uma conta especifica basta preencher um ou os campos nome, valor e/ou vencimento e clicar no botão [Consultar]. \
Para listar todas as contas basta clicar no botão [Consultar tudo]. \
Ao clicar na conta listada no campo esquerdo e clicar no botão [Detalhes] o resumo da conta irá aparecer no campo direito.

## Excluindo uma conta
![image](https://user-images.githubusercontent.com/66915867/160295177-7a817d71-a685-431f-b843-66ad2eccb8a9.png) \
Para excluir uma conta é preciso saber o id dela para não excluir uma outra por engano. Então o usuário consultará pelo nome, valor e/ou vencimento. \
Ao clicar no botão [Pesquisar] será listada as contas no campo a baixo junto com seu id, assim basta colocar o numero do id da conta na caixa ao lado e clicar em excluir.
\
![image](https://user-images.githubusercontent.com/66915867/160295307-bdefe368-fd5e-4088-bb5f-15a3095e0a4b.png)
\
![image](https://user-images.githubusercontent.com/66915867/160295349-0b0e4cf6-39fb-4907-b55a-cdf5381a7194.png)
