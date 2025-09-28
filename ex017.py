#Listando conteúdo de diretórios

import os

diretorio = r'C:\Users\jr\OneDrive\Desktop\PYTHON\Scripts'

try:
    entradas = os.scandir('diretorio')

    for obj in entradas:
        print("Nome:", obj.name)
        print("Caminho:", obj.path)
        print("É diretório:", obj.is_dir())
        print("É arquivo:", obj.is_file())
        if obj.is_file():
            print("Tamanho:", obj.stat().st_size, "B")
        print("============+++======================")

except FileNotFoundError:
    print("O caminho não existe.")
except NotADirectoryError:
    print("O caminho não é um diretório.")

print("Fim do programa")


