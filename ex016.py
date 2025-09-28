#Removendo diretórios

import os
import traceback

try:
    os.rmdir('meu_diretorio')
    print('Diretório removido.')
except OSError as erro:
    traceback.print_exc()  # imprime a stack completa

print('Término do programa')