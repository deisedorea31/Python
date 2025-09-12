# Escrevendo conteúdo em um arquivo - WRITE com o modo 'w'

# Escrita
arquivo_escrita = open('dados_write.txt', 'w', encoding='utf-8')
arquivo_escrita.write('Conteúdo da primeira linha')#Adiciona a primeira linha
arquivo_escrita.write('\nConteúdo da segunda linha')#Adiciona a segunda linha
arquivo_escrita.close()

print('Arquivo escrito com sucesso!')

# Leitura
arquivo_leitura = open('dados_write.txt', 'r', encoding='utf-8')
conteudo = arquivo_leitura.read()#Lê o conteúdo escrito
print('Conteúdo escrito:')
print(conteudo)
arquivo_leitura.close()





