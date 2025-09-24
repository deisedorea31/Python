# Codificando mensagens em Python - ZENIT POLAR (versão com replace)

def zenit_polar_replace(text):
    # Substituições usando símbolos temporários para não "voltar" as trocas
    replacements = [
        ('z', '#'), ('e', '$'), ('n', '%'), ('i', '&'), ('t', '*'),
        ('Z', '§'), ('E', '£'), ('N', '¢'), ('I', '¥'), ('T', '¤'),

        ('p', 'z'), ('o', 'e'), ('l', 'n'), ('a', 'i'), ('r', 't'),
        ('P', 'Z'), ('O', 'E'), ('L', 'N'), ('A', 'I'), ('R', 'T'),

        ('#', 'p'), ('$','o'), ('%', 'l'), ('&','a'), ('*','r'),
        ('§','P'), ('£','O'), ('¢','L'), ('¥','A'), ('¤','R')
    ]

    for old, new in replacements:
        text = text.replace(old, new)
    return text


def main():
    # Frase inicial
    frase = 'The quick brown fox jumps over the lazy dog'
    frase = frase.title()  # Primeira letra de cada palavra em maiúscula

    # Dividir em palavras
    words = frase.split()

    # Aplicar a cifra em cada palavra
    coded_words = [zenit_polar_replace(word) for word in words]

    # Juntar com ESPAÇO entre as palavras
    coded_frase = " ".join(coded_words)

    print('Original:', frase)
    print('Coded   :', coded_frase)


if __name__ == "__main__":
    main()




