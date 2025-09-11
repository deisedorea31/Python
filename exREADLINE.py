#Manipulação de Arquivos com READLINE

#Abertura do arquivo pelo método readline().
arquivo = open('exemplo.txt', 'r', encoding='utf-8')

conteudo = arquivo.readline() #Lê a primeira linha do arquivo
print('Tipo de Conteúdo:', type(conteudo)) #Mostra o tipo do conteúdo lido
print('Conteúdo retornado pelo readline:')
print(repr(conteudo)) #repr() mostra os caracteres especiais como \n

proximo_conteudo = arquivo.readline() #Lê a próxima linha do arquivo
print('Próximo conteúdo retornado pelo readline:')
print(repr(proximo_conteudo)) #repr() mostra os caracteres especiais como \n

arquivo.close()
