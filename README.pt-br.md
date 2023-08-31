<h1 align="center">Projeto comunicação com o instrumento</h1>

Projeto dedicado para se realizar a comunicação com o instrumento, utilizando comandos para serem enviados e ler as respostas.

<h2 align="center">➤ Questões📝</h2>

| Questão | Descrição | Responsável | Link |
| ------ | ------ | ------ | ------ |
| Questão A | Crie um método que armazene as temperaturas lidas em uma lista (para isso faça um laço que envie o comando TMP pelo menos 20 vezes para ter um retorno satisfatório) | <a href="https://github.com/nicolasscarvalho"><img src="https://avatars.githubusercontent.com/u/98130635?v=4" width="100px;" alt="Nicolas Carvalho"/><br /><sub><b>Nicolas Carvalho</b></sub></a><br /></td> | [Clique Aqui](funcs/func_QA.py)
| Questão B | Crie um método que dispare um erro se uma das temperaturas lidas for maior que 80 graus. Dica: use uma exception personalizada| <a href="https://github.com/nicolasscarvalho"><img src="https://avatars.githubusercontent.com/u/98130635?v=4" width="100px;" alt="Nicolas Carvalho"/><br /><sub><b>Nicolas Carvalho</b></sub></a><br /></td> | [Clique Aqui](funcs/func_QB.py)
| Questão C| Crie um método que armazene uma lista de 20 tensões  (faça como na 1) e retorne um print caso a tensão seja zero ou um erro caso seja maior que 190 | <a href="https://github.com/Valcler-Manoel"><img src="https://avatars.githubusercontent.com/u/91897674?v=4" width="100px;" alt="Válcler Manoel"/><br /><sub><b>Válcler Manoel</b></sub></a><br /></td> | [Clique Aqui](funcs/func_QC.py)
| Questão D | Crie um dicionário e armazene pelo menos 20 dados de cada atributo que representam grandezas físicas (temperatura, tensão etc) e 5 dos demais. A chave deve ser o nome do atributo do instrument e seu valor deve ser uma lista com os 20 elementos.  | <a href="https://github.com/PedroKeita"><img src="https://avatars.githubusercontent.com/u/82671771?v=4" width="100px;" alt="Pedro Lucas"/><br /><sub><b>Pedro Lucas</b></sub></a><br /></td> | [Clique Aqui](funcs/func_QD.py)
| Questão E | Colete 30 elementos de corrente e armazene apenas os valores maiores que 25 mA e menores que 800 mA. Print uma mensagem escrito “Threshold alert!” cada vez que receber menos de 25 mA. | <a href="https://github.com/Akkessatsu"><img src="https://avatars.githubusercontent.com/u/99400178?v=4" width="100px;" alt="Raul Braga"/><br /><sub><b>Raul Braga</b></sub></a><br /></td> | [Clique Aqui](funcs/func_QE.py)

<h2 align="center">➤ Estrutura de arquivo: 🏛</h2>
```bash
  comunicação-instrumento/
  │
  ├── funcs/
  │   ├── func_QA.py
  │   ├── func_QB.py
  │   ├── func_QC.py
  │   ├── func_QD.py
  │   └── func_QE.py
  │
  │── tests/
  │   ├── test_QA.py
  │   ├── test_QB.py
  │   ├── test_QC.py
  │   ├── test_QD.py
  │   └── test_QE.py
  │
  ├── README.md
  ├── README.pt-br.md
  ├── client.py
  └── instrument.py
```
<h2 align="center">➤ Como se usa? 🤔</h2>

1. Execute o seguinte comando abaixo para executar o projeto
   ```bash
   python -m pytest caminho/arquivo.py
   
#### Leia em Inglês:
<kbd>[<img title="Inglês" alt="Inglês" src="https://cdn.staticaly.com/gh/hjnilsson/country-flags/master/svg/us.svg" width="22">](README.md)</kbd>
