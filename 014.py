#Remover diretórios

import os

try:
    os.rmdir('meu_diretorio')
    print('Diretório removiso.')
except PermissionError as erro:
    print('Sem permissão para remover o diretório.', erro)
    print('Descrição', erro)
except FileNotFoundError as erro:
    print('Diretório inexistente')
    print('Descrição', erro)
except OSError as erro:
    print('Outro erro')
    print('Diretório está vazio')
    print('Descrição', erro)

print('Término do programa')