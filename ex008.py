#Codificnado mensagens em Python - ZENIT POLAR


def zenit_polar_replace(text):
    #Aplicar a codificação ZENIT POLAR utilizando o método replace
    replacements = [('z', 'p'),('e', 'o'), ('n', 'l'), ('i','a'), ('t', 'r'),
                   ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for old, new in replacements:
        text = text.replace(old, new)
    return text

def main():
        #Entrada da frase e aplicação da codificação
        frase = 'The quick brown fox jumps over the lazy dog'
        frase = frase.title() #Primeira letra de cada palavra em maiúscula

        #Dividir a frase em palavras
        words = frase.split()

        #Processar cada palavra na lista usando ZENIT POLAR
        coded_words = [zenit_polar_replace(word) for word in words]

        #Juntar todas as palavras codificadas em uma frase
        coded_frase = " ".join(coded_words)
        print('Original:', frase)
        print('Coded:', coded_frase)

if __name__ == "__main__":
    main()


