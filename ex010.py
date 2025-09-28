#Tratamento de exceções na manipulação
#   de Arquivos - cláusula try/except


print('Abrindo um arquivo')

try:
    open('comparacao.txt', 'w')
    print('Arquivo aberto!')
except FileNotFoundError as erro:
    print('Arquivo inexistente.')
    print('Descrição', erro)
except PermissionError as erro:
    print('Sem permissão para acessar o arquivo.')
    print('Descrição:', erro)

print("Término do programa.")