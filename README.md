# Sistema de Criptografia de Mensagens

Projeto acadêmico desenvolvido para permitir a troca segura de mensagens entre diretores de diferentes cidades.

## Objetivo

O sistema permite que uma mensagem seja criptografada por um diretor, salva em um arquivo protegido e transportada por meio de um dispositivo USB.

O segundo diretor pode importar o arquivo, informar a chave correta e recuperar a mensagem original.

## Funcionamento

O sistema utiliza criptografia simétrica, na qual a mesma chave é utilizada para proteger e recuperar a mensagem.

Fluxo principal:

1. O diretor escreve uma mensagem.
2. O diretor informa uma chave.
3. O sistema criptografa a mensagem.
4. A mensagem criptografada é salva em um arquivo `.enc`.
5. O arquivo pode ser transportado por um dispositivo USB.
6. O segundo diretor seleciona o arquivo.
7. A chave é informada.
8. O sistema descriptografa a mensagem.
9. A mensagem original é apresentada na tela.
10. As mensagens são registradas no histórico.

## Estrutura de dados

O projeto utiliza uma árvore binária para armazenar as mensagens.

A árvore possui:

- Nó raiz;
- Filho esquerdo;
- Filho direito;
- Inserção de novos elementos;
- Percurso em pós-ordem.

O percurso em pós-ordem segue a sequência:

**Esquerda → Direita → Raiz**

O diagrama da estrutura está disponível no arquivo `arvore_binaria.drawio` e na imagem `arvore_binaria.png`.

## Histórico

O sistema possui uma área de histórico para registrar as mensagens enviadas e as mensagens recuperadas.

Cada registro apresenta:

- Tipo da operação;
- Data e hora;
- Conteúdo da mensagem.

## Tecnologias utilizadas

- Python
- Tkinter
- Biblioteca Cryptography
- AES-GCM
- Estrutura de dados: Árvore Binária
- GitHub para controle de versão
- draw.io para documentação da estrutura

## Arquivos do projeto

| Arquivo | Descrição |
|---|---|
| `main.py` | Interface gráfica e funcionamento principal do sistema |
| `arvore.py` | Implementação da árvore binária |
| `README.md` | Documentação do projeto |
| `arvore_binaria.drawio` | Diagrama editável da árvore binária |
| `arvore_binaria.png` | Representação visual da árvore |

## Requisitos

Para executar o projeto, é necessário possuir Python instalado.

Também é necessário instalar a biblioteca Cryptography:

```bash
pip install cryptography
