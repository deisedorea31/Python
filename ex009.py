#Tratamento de exceções na manipulação
#   de Arquivos - cláusula try/except

print('Abrindo um arquivo')

try:
    open('comparacao.txt', 'r')
    print('Arquivo aberto')
except FileNotFoundError as erro:
    print('Arquivo inexistente')
    print('Descrição', erro)

print('Término do Programa.')
