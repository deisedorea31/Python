'''Abertura do arquivo pelo método read(). abrimos o arquivo na linha 1 e, na linha 3, 
utilizamos o método read() do objeto arquivo para ler o conteúdo de dados.txt e armazená-lo na variável conteúdo.'''

arquivo = open('exemplo.txt', 'r', encoding='utf-8')

conteudo = arquivo.read()
print('Conteúdo retornado pelo read:')
print(repr(conteudo)) #repr() mostra os caracteres especiais como \n
#Perceba:
#print(texto) mostra o texto como ele aparece para o usuário.
#print(repr(texto)) mostra a forma como o Python armazena a string, com caracteres de escape (\n).

arquivo.close()
print('Aquivo está fechado agora?', arquivo.closed)