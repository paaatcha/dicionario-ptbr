# Dicionario português brasileiro para python

Este projeto tem como objetivo compilar um dicionário de português brasileiro para ser utilizado em Python, de maneira fácil e rápida, para análise sintática de palavras. Para isso, a ideia é contruir um ```dict()``` em python, na qual a chave será uma palavra qualquer e o(s) valor(es) o(s) grupo(s) gramatical(is) dessa palavra. Usando ```dict()``` a busca pelo valor sintático da palavra ocorre de maneira rápida e fácil.

O dicionário de português brasileito foi através site de dados aberto [Dicionario-XML](http://dicionario-aberto.net/). Esse dicionário possui 123390 palavras. Esse número é relativamente baixo. Por conta disso, ainda estou trabalhando em aumentar esse número.

O código atual realiza um parse nos arquivos XML's, constrói o ```dict()``` e salva um arquivo .txt utilizanod json. Para utilizar o dicionário de maneira fácil basta executar:

```python
import json
dic_pt_br = json.load(open("dic-pt-br.txt", 'r'))
```
Para verificar a classe gramatical de uma palavra, basta executar:

```python
print dic_pt_br['terra']
```
Essa chamada retornarar uma tag do tipo:
* 'm.': substantivo masculino
* 'f.': substantivo feminino
* 'v. *': verbo (o * uer dizer que o verbo pode ser transitivo, intrasitivo etc.)
* 'adj.': adjetivo
* 'adv.': advérbio
