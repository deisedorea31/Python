Objetivo

A ideia é desenvolver um programa em Python que permita a captura de texto via console, no qual um editor pode inserir trechos de textos recebidos dos autores. O programa deve salvar esses trechos em um arquivo de texto, ler o arquivo, converter todo o texto para letras maiúsculas para padronizar a formatação e finalmente sobrescrever o arquivo original com o texto formatado. Esse processo facilitará a revisão preliminar antes da edição final.


Acompanhe os passos esperados no programa!

- Captura de dados: o programa deve solicitar ao usuário que insira várias frases ou parágrafos pelo console. A entrada de dados deve continuar até o usuário digitar "sair", indicando que deseja encerrar a inserção e salvar o arquivo.
- Criação e armazenamento: o texto inserido deve ser salvo em um arquivo chamado meu_arquivo.txt.
- Manipulação do arquivo: o programa deve abrir o arquivo salvo, ler o conteúdo e converter todas as letras para maiúsculas.
- Sobrescrever o arquivo original: após a manipulação, o texto alterado deve ser usado para sobrescrever o arquivo original, garantindo que o arquivo contenha apenas o texto formatado.

Captura dados
- Acontece da seguinte maneira:
- O script inicia com uma mensagem para o usuário, solicitando que ele digite frases e termine digitando sair quando quiser finalizar.
- Um loop while True é usado para receber continuamente as entradas do usuário através da função input(). Cada entrada é adicionada a uma lista chamada frases.
- O loop é interrompido (break) quando o usuário digita sair, verificado após cada entrada com o método .lower() para garantir que a comparação seja insensível a maiúsculas e minúsculas.

Cria e armazena o arquivo
- Acontece da seguinte maneira:
- Após o término da entrada de dados, o script abre (ou cria, se não existir) um arquivo chamado meu_arquivo.txt no modo de escrita (w) usando a instrução with open(...) as arquivo:
- Dentro desse bloco, o script escreve cada frase armazenada na lista frases no arquivo. Cada frase é seguida por uma quebra de linha \n.

Lê e manipula o arquivo
- Acontece da seguinte maneira:
- Uma vez que o arquivo é criado, o script procede para abrir o mesmo arquivo, agora no modo de leitura (r).
- O conteúdo do arquivo é lido linha por linha. Cada linha é despojada de espaços extras e quebras de linha com .strip() e convertida para letras maiúsculas com .upper().
- As linhas modificadas são armazenadas em uma nova lista chamada dados_modificados.

Sobrescreve o arquivo original
- Acontece da seguinte maneira:
- O arquivo meu_arquivo.txt é novamente aberto, dessa vez, no modo de escrita (w), o que trunca o arquivo a zero antes de começar a escrever.
- O script então escreve cada linha da lista dados_modificados de volta ao arquivo, cada uma terminando com uma quebra de linha \n.

Confirma a conclusão
- Acontece da seguinte maneira:
- Após a reescrita, uma mensagem é impressa para informar que o arquivo foi sobrescrito com os dados modificados.
- É importante considerar o seguinte:
- O uso do contexto with para manipulação de arquivos é uma prática recomendada porque garante que o arquivo seja fechado corretamente após as operações, mesmo se uma exceção ocorrer durante o processo.
- A conversão de todas as entradas para maiúsculas é um exemplo de normalização de dados, útil em muitos contextos de processamento de texto para garantir consistência.
 
Esse script é uma excelente maneira de entender a manipulação básica de arquivos em Python, incluindo leitura, escrita e aplicação de transformações simples aos dados de texto.