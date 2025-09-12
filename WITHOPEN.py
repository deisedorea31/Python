#Iterando sobre arquivos com WITH e OPEN

print('Escrevendo e depois lendo o arquivo...')

# Escrita
with open('dados_txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')

# Leitura
with open('dados_txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())

print('Fim do arquivo', arquivo.name)
