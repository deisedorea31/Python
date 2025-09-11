#Abertura de arquivo pelo método readlines()

arquivo = open('exemplo.txt', 'r', encoding='utf-8')    

conteudo = arquivo.readlines() #Lê todas as linhas do arquivo e retorna uma lista
print('Tipo de Conteúdo:', type(conteudo)) #Mostra o tipo do conteúdo lido
print(repr(conteudo)) #repr() mostra os caracteres especiais como \n

proximo_conteudo = arquivo.readlines() #Tenta ler mais linhas, mas já estamos no final do arquivo
print('Próximo conteúdo retornado pelo readlines():')
print(repr(proximo_conteudo)) #repr() mostra os caracteres especiais como \n

arquivo.close()