# Exceções e o módulo "os"
# Automatize a organização de arquivos de texto.

import os

# Função para ler o conteúdo de um arquivo e escrever em um novo arquivo com uma linha de cabeçalho
def processar_arquivo(arquivo_origem, arquivo_destino):
    try:
        with open(arquivo_origem, 'r', encoding='utf-8') as f_origem:
            conteudo = f_origem.read()
    except FileNotFoundError:
        print(f'Arquivo {arquivo_origem} não encontrado.')
        return
    except PermissionError:
        print(f'Sem permissão para ler {arquivo_origem}.')
        return
    except Exception as e:
        print(f'Erro inesperado ao ler {arquivo_origem}: {e}')
        return
    try:
        with open(arquivo_destino, 'w', encoding='utf-8') as f_destino:
            f_destino.write('Cabeçalho: Conteúdo do Arquivo\n')
            f_destino.write(conteudo)
            print(f'Conteúdo escrito em {arquivo_destino}.')
    except PermissionError:
        print(f'Sem permissão para escrever em {arquivo_destino}.')
    except Exception as e:
        print(f'Erro inesperado ao escrever em {arquivo_destino}: {e}')


# No script principal, defina os arquivos de origem e destino e chame a função criada
def main():
    diretorio_trabalho = 'diretorio_trabalho'
    os.makedirs(diretorio_trabalho, exist_ok=True)  # cria a pasta se não existir

    arquivo_origem = os.path.join(diretorio_trabalho, 'arquivo_origem.txt')
    arquivo_destino = os.path.join(diretorio_trabalho, 'arquivo_destino.txt')

    # Escrita no arquivo de origem
    with open(arquivo_origem, 'w', encoding='utf-8') as arquivo_escrita:
        arquivo_escrita.write('Eu amo comer amoras no café da manhã!\n')
        arquivo_escrita.write('Amora, abacaxi, abacate, banana.\n')
        arquivo_escrita.write('Carro, moto, avião\n')

    # Agora sim, passa os caminhos (strings) para a função
    processar_arquivo(arquivo_origem, arquivo_destino)


if __name__ == '__main__':
    main()
