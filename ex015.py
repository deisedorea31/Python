#Removendo diretórios

import os
import errno

try:
    os.rmdir('meu_diretorio')
    print('Diretório removido.')
except OSError as erro:
    if erro.errno == errno.ENOENT:   # No such file or directory
        print("O diretório não existe.")
    elif erro.errno == errno.ENOTEMPTY:  # Directory not empty
        print("O diretório não está vazio.")
    elif erro.errno == errno.EACCES:  # Permission denied
        print("Sem permissão para remover o diretório.")
    else:
        print(f"Erro inesperado: {erro.strerror} (código {erro.errno})")

print('Término do programa')
