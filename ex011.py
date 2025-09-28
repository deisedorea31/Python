# Remover arquivos

import os

try:
    os.remove('dados_txt')
    print('Arquivo removido.')
except FileNotFoundError as erro: #Ocorre quando o arquivo não existe
    print('Arquivo inexistente.')
    print('Descrição', erro)
except PermissionError as erro: #Ocorre quando ão temos perissão para alterar o arquivo
    print('Sem permissão para acessar o arquivo.')
    print('Descrição', erro)
except IsADirectoryError as erro: #Ocorre quando tentamos remover um diretório usando a função remove, em vez de rmdir
    print('Remove serve apenas para arquivos.')
    print('Descrição', erro)

print('Término do programa')
