#Manipulação de string usando método strip
'''Abre o arquivo apenas uma vez.
Mostra cada linha como está no arquivo e como fica limpa lado a lado.
Contadores separados:
contador_original → linhas não vazias na versão original.
contador_limpo → linhas não vazias após aplicar .strip().'''

with open('dados_write.txt', 'r', encoding='utf-8') as arquivo:
    contador_original = 0
    contador_limpo = 0

    print("Representação original do arquivo | Linhas limpas:")
    print("-" * 50)

    for linha in arquivo:
        # Representação original
        rep_original = repr(linha)
        if linha.strip():  # conta apenas linhas não vazias
            contador_original += 1

        # Linha limpa
        linha_limpa = linha.strip(' "\'\n\t')
        if linha_limpa:
            contador_limpo += 1

        # Mostra lado a lado
        print(f"{rep_original} | {linha_limpa}")

    print("\nTotal de linhas não vazias (original):", contador_original)
    print("Total de linhas limpas (após strip()):", contador_limpo) 