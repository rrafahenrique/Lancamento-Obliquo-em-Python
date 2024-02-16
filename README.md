<h1 align = "center"> Lançamento Oblíquo em Python </h1>

![Badge de Concluido](https://img.shields.io/badge/status-conclu%C3%ADdo-green?style=for-the-badge)
![Badge Licença](https://img.shields.io/badge/license-mit-blue?style=for-the-badge)

# Introdução
Este é um simulador de Lançamento Oblíquo feito em Python, com a intenção de ajudar alunos de Física do Ensino Médio que estejam estudanto este conteúdo em sala de aula. É necessário saber o básico de programação para manusear o programa.

# Conceito Básico
Lançamento Oblíquo ocorre quando um objeto é lançado e o seu movimento faz um ângulo com a horizontal. Neste tipo de fenômeno o objeto realiza dois movimentos simultâneos, ao mesmo tempo em que executa um movimento na vertical (subida e descida), também se desloca horizontalmente.

# Linguagens e Tecnologias Usadas
- Linguagem: Python 3.10
- Bibliotecas: Tkinter e Matplolib

O Tkinter foi utilizado para fazer a Interface Gráfica (GUI) da simulação, onde o usuário poderá inserir os valores de **Velocidade Inicial** e **Ângulo** e clicar nos botões **Executar**, **Reiniciar**, **Gráfico** e **Sair**.
A ideia aqui foi constuir um ambiente gŕafico simples e intuitivo para que professores e alunos possam ter a melhor experiência de uso.

![Simulador](https://user-images.githubusercontent.com/115511374/196821761-6ab6ba0f-4a45-45b5-9a44-fef1c91ceb59.png)

Para que a simulação fique mais didática foi acrescentado a opção de mostrar o gráfico da Trajetória, isso foi feito usando a biblioteca Matplotlib.

![Grafico](https://user-images.githubusercontent.com/115511374/196822078-a0913dc2-d039-4764-9330-38ac0e7f6b07.png)

# Mode de Uso

Embaixo da área onde vemos a bola vermelha, e o chão verde, temos o menu de inserção dos dados, Velocidade Inicial e Ângulo de Lançamento, fique atento as dados que serão colocados, mas caso você digite algo errado uma mensagem de aviso irá aparecer. Dados inseridos, basta clicar em **Executar**, no menu dos botões que a simulação irá iniciar.

Depois do lançamento ser exercutado, pode clicar em **Gráfico** e irá aparecer uma segunda janela com o Gráfico da Trajetória.
A simulação pode ser feita quantas vezes quiser, basta clicar em **Reiniciar** que os dados inserido serão apagados e uma nova simulação poderá ser realizada.

