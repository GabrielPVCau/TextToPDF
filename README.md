# TextToPDFLean

## Descrição
TextToPDFLean é uma ferramenta de conversão de texto para PDF que elimina espaços em branco desnecessários, criando documentos PDF mais compactos e limpos a partir de arquivos de texto simples.

## Funcionalidades
- Converte arquivos .txt em PDF.
- Remove todos os espaços em branco dos textos, incluindo espaços entre palavras e linhas.

## Como Usar
1. Instale a biblioteca necessária com `pip install fpdf`.
2. Coloque o arquivo de texto que deseja converter na mesma pasta do script ou especifique o caminho completo.
3. Execute o script e especifique o nome do arquivo de texto e o nome desejado para o arquivo PDF de saída.

## Requisitos
- Python 3.x
- Biblioteca FPDF

## Exemplo de Uso
Para converter um arquivo chamado `example.txt` em um PDF chamado `output.pdf`, simplesmente execute o seguinte comando no terminal:

```bash
python texttopdflean.py example.txt output.pdf
