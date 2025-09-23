# Manipulando strings usando método Join

minha_lista = ['Amora', 'abacaxi', 'abacate', 'banana'] #Criando a lista

# Texto com vírgula
texto1 = ','.join(minha_lista)

# Texto com quebra de linha
texto2 = '\n'.join(minha_lista)

# Criando um arquivo único com os dois resultados
with open('comparacao.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("=== Lista separada por vírgula ===\n")
    arquivo.write(texto1 + "\n\n")  # quebra de linha dupla p/ espaçamento

    arquivo.write("=== Lista em várias linhas ===\n")
    arquivo.write(texto2)


