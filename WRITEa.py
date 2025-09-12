#Escrevendo conteúdo em um arquivo - WRITE com o modo 'a'

# Escrita
arquivo_escrita = open('dados_write.txt', 'a', encoding='utf-8')
arquivo_escrita.write('\nConteúdo adicionado na primeira linha')#Adiciona uma nova linha
arquivo_escrita.close()
print('Conteúdo adicionado com sucesso!')

# Leitura
arquivo_escrita = open('dados_write.txt', 'r', encoding='utf-8')
conteudo = arquivo_escrita.read()#Lê o conteúdo atualizado
print('Conteúdo atualizado:')
print(conteudo)
arquivo_escrita.close()