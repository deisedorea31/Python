# Manipulação de arquivos

import os

#Abrindo o arquivo em modo de escrita (write)
arquivo = open('exemplo.txt', 'w', encoding='utf-8')

#Exibindo os atributos do arquivo
print('Nome do aqurivo:', arquivo.name) #Nome do arquivo
print('Modo de abertura:', arquivo.mode) #Modo de abertura
print('Arquivo fechado?', arquivo.closed) #Verifica se o arquivo está fechado

#Escrevendo no arquivo
arquivo.write('Olá Mundo. \n Este é um exemplo de manipulação de arquivos em Python.\n')

#Fechando o arquivo
arquivo.close()

#Verificando se o arquivo está fechado
print('Aquivo está fechado agora?', arquivo.closed)

#Exibindo o caminho absoluto do arquivo
exit
print('Caminho absoluto do arquivo:', os.path.abspath('exemplo.txt'))
print('Caminho relativo do arquivo:', os.path.relpath('exemplo.txt'))