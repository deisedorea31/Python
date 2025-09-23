# Manipulação de string usando Count e Split (versão limpa e insensível a maiúsculas)

import string
from collections import Counter

# Escrita
with open('dados1.txt', 'w', encoding='utf-8') as arquivo_escrita:
    arquivo_escrita.write('Eu amo comer amoras no café da manhã! \n')
    arquivo_escrita.write('\n Amora, abacaxi, abacate, banana. \n')
    arquivo_escrita.write('\n Carro, moto, avião \n')

print('Arquivo escrito com sucesso!')

# Leitura e contagem de palavras
contador_original = 0
contador_limpo = 0
todas_palavras = []

with open('dados1.txt', 'r', encoding='utf-8') as arquivo_leitura:
    print("Representação original do arquivo | Linhas limpas | Palavras:")
    print("-" * 80)

    for linha in arquivo_leitura:
        # Representação original
        rep_original = repr(linha)
        if linha.strip():
            contador_original += 1

        # Linha limpa
        linha_limpa = linha.strip(' "\'\n\t')
        if linha_limpa:
            contador_limpo += 1

        # Remover pontuação
        linha_sem_pontuacao = linha_limpa.translate(str.maketrans('', '', string.punctuation))

        # Converter para minúsculas
        linha_minuscula = linha_sem_pontuacao.lower()

        # Separar em palavras
        palavras = linha_minuscula.split()
        todas_palavras.extend(palavras)

        print(f"{rep_original} | {linha_limpa} | {palavras}")

print("\nTotal de linhas não vazias (original):", contador_original)
print("Total de linhas limpas (após strip()):", contador_limpo)

# Contagem de palavras usando Counter
contagem_palavras = Counter(todas_palavras)
print("\nContagem de palavras no arquivo (pontuação removida, minúsculas):")
for palavra, quantidade in contagem_palavras.items():
    print(f"{palavra}: {quantidade}")
 