'''Quando precisamos abrir um arquivo muito grande, é inviável utilizar os métodos read e readlines, 
pois eles retornam todo o conteúdo do arquivo de uma só vez, seja na forma de string, seja na forma de lista. 
Isso pode consumir todos os recursos do computador, travando seu programa.'''

#Abertura de arquivo e iteração linha a linha
arquivo = open('exemplo.txt', 'r', encoding='utf-8')

conteudo = arquivo.read() #Lê todas as linhas do arquivo e retorna uma lista
print('Todo o conteúdo do arquivo')
print(repr(conteudo), '\n') #repr() mostra os caracteres especiais como \n

conteudo_releitura = arquivo.read() #Tenta ler mais linhas, mas já estamos no final do arquivo
print('Conteúdo retornado na tentativa de releitura do arquivo:')
print(repr(conteudo_releitura), '\n') #repr() mostra os caracteres especiais como \n

arquivo.close()

arquivo_reaberto = open('exemplo.txt', 'r', encoding='utf-8') #Reabrindo o arquivo para reiniciar a leitura

conteudo_reaberto = arquivo_reaberto.readlines() #Lê todas as linhas do arquivo e retorna uma lista
print('Todo o conteúdo do arquivo novamente')
print(repr(conteudo_reaberto), '\n') #repr() mostra os caracteres especiais como \n

arquivo_reaberto.seek(8) #Move o cursor para a posição 8 do arquivo
conteudo_seek = arquivo_reaberto.read() #Lê todas as linhas do arquivo a
print('Conteúdo do arquivo após SEEK')
print(repr(conteudo_seek), '\n') #repr() mostra os caracteres especiais como \n

arquivo_reaberto.close()