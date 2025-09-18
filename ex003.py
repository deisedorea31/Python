# Escrevendo um arquivo para manipulação de String usando o método strip

# Escrita
arquivo_escrita = open('dados_write.txt', 'w', encoding='utf-8')
arquivo_escrita.write('""Conteúdo da primeira linha \n') #Adiciona a primeira linha
arquivo_escrita.write('\n Conteúdo da segunda linha \n')#Adiciona a segunda linha
arquivo_escrita.write('""\n Conteúdo da terceira linha \n')#Adiciona a terceira linha
arquivo_escrita.close()

print('Arquivo escrito com sucesso!')

#Leitura
with open('dados_write.txt', 'r', encoding='utf-8') as arquivo_leitura:
    conteudo = arquivo_leitura.read() #Lê o conteúdo escrito
    print('Conteúdo escrito:')
    print(conteudo)


