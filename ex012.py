#Renomear arquivos

import os

try:
    os.rename('comparacao.txt', 'lista.txt')
    print('Arquvivo renomeado.')
except FileNotFoundError as erro:
    print('Arquivo inexistente.')
    print('Descrição', erro)
except PermissionError as erro:
    print('Arquivo inexistent'), erro
    print('Descrição', erro)
except FileExistsError as erro:
    print('Arquivo de destino já existe.')
    print('Descrição', erro)

print('Término do programa')