# Projeto de Análise de Sentimento atravez de PNL

## Introdução

  

Este repositório contém uma aplicação básica que combina uma API desenvolvida em Flask, um modelo de predição de sentimentos em frases usando o PySentimiento e um frontend simples em Vue.js. A aplicação permite enviar um arquivo CSV contendo dados textuais para a API Flask, que por sua vez utiliza o modelo PySentimiento para analisar o sentimento das frases no arquivo CSV.

  

Componentes da Aplicação

  

1. **API FLASK**

___________

A API Flask recebe requisições contendo arquivos CSV (datasets) e utiliza o modelo de predição de sentimentos PySentimiento para analisar o sentimento das frases contidas nos dados. O resultado da análise é retornado como uma resposta da API.

  
  
  
2. **PySentimiento**

____________________

O PySentimiento é um modelo de predição de sentimentos em frases. Ele é utilizado pela API Flask para analisar o sentimento das frases presentes nos datasets fornecidos.

  
  

3. **Frontend Vue.js**

_____________________

O frontend em Vue.js oferece uma interface básica para o usuário interagir com a aplicação. Ele permite enviar arquivos CSV para a API Flask e exibe o resultado da análise de sentimentos realizada pela API.

  

# Como Usar

---
1. Clone este repositório para sua máquina local.


2. Instale as dependências necessárias para a API Flask e o frontend Vue.js.


**Flask:**

```bash

pip3 install -r requeriments.txt

```


**Vue3:**

```bash

npm install --save-dev $(cat requeriments.txt)

```


3. Inicie a API Flask e o frontend Vue.js.


**Flask:**

```bash

python3 flaskapi.py

```

**Vue3:**

```bash

npm run dev

```

4. Acesse o frontend através do navegador e utilize a interface para enviar arquivos CSV e visualizar o resultado da análise de sentimentos.


Para facilitar os testes, disponibilizamos dois conjuntos de dados: `teste.csv` (para testes rápidos) e `dataset.csv` (conjunto de dados real). Devido ao tamanho do conjunto de dados, a API pode demorar para responder com o `dataset.csv`.
