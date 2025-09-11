'''Utilizamos o laço for para iterar diretamente sobre a variável arquivo. Para cada iteração, 
recebemos uma nova linha do arquivo, disponibilizada na variável linha'''

# Abrindo o arquivo em modo leitura com encoding utf-8
arquivo = open('exemplo.txt', 'r', encoding='utf-8')

print('Iterando sobre o arquivo linha a linha')

# O laço for percorre cada linha do arquivo
for linha in arquivo:
    # repr() mostra os caracteres especiais (como \n)
    print(repr(linha))

# O arquivo só deve ser fechado DEPOIS do loop
arquivo.close()
