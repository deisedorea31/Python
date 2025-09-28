#Módulos os e shutil

import os
import shutil

#Verificar se os diretórios existem e, se não, criá-los
def criar_diretorios(diretorios):
    for diretorio in diretorios:
        if not os.path.exists(diretorio):
            try:
                os.makedirs(diretorio)
                print(f'Diretório {diretorio} criado.')
            except PermissionError:
                print(f'Sem permissão para cirar o diretório {diretorio}.')
            except Exception as e:
                print(f'Erro inesperado ao criar {diretorio}: {e}')

#Função para mover os arquivos para os diretórios correspondentes com base em suas extensões
def mover_arquivos(diretorio_origem):
    for arquivo in os.listdir(diretorio_origem):
        caminho_arquivo = os.path.join(diretorio_origem, arquivo)
        if os.path.isfile(caminho_arquivo):
            extensao = arquivo.split('.')[-1].lower()
            if extensao in ['pdf', 'txt', 'jpg']:
                diretorio_destino = os.path.join(diretorio_origem, extensao)
                try:
                    shutil.move(caminho_arquivo, diretorio_destino)
                    print(f'{arquivo} movido para {diretorio_destino}.')
                except PermissionError:
                    print(f'Sem permissão para mover {arquivo}.')

#No script principal, defina o diretório de trabalho e chame as funções criadas
def main():
    diretorio_trabalho = 'diretorio_trabalho'
    diretorios = [os.path.join(diretorio_trabalho, 'pdf'),
                  os.path.join(diretorio_trabalho, 'txt'),
                  os.path.join(diretorio_trabalho, 'jpg')]

    #criar diretorios se não existirem
    criar_diretorios(diretorios)

    #mover arquivos para diretórios correspondentes
    mover_arquivos(diretorio_trabalho)

if __name__ == "__main__":
    main()


