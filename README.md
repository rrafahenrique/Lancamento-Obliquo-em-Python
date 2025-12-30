<h1 align = "center"> Lançamento Oblíquo em Python </h1>

![Badge de Concluido](https://img.shields.io/badge/status-conclu%C3%ADdo-green?style=for-the-badge)
![Badge Licença](https://img.shields.io/badge/license-mit-blue?style=for-the-badge)

# Introdução
Este é um simulador de Lançamento Oblíquo feito em Python, com a intenção de ajudar alunos de Física do Ensino Médio que estejam estudando este conteúdo em sala de aula.

# Conceito Básico
**Lançamento Oblíquo** ocorre quando um objeto é lançado e o seu movimento faz um ângulo com a horizontal. Neste tipo de fenômeno o objeto realiza dois movimentos simultâneos, ao mesmo tempo em que executa um movimento na vertical (subida e descida), também se desloca horizontalmente.

# Simulação
O Tkinter foi utilizado para fazer a Interface Gráfica (GUI) da simulação, onde o usuário poderá inserir os valores de **Velocidade Inicial** e **Ângulo**,fique atento as dados que serão colocados, mas caso você digite algo errado uma mensagem de aviso irá aparecer.

Ao lado de onde a simulação e feita, existe 4 botões **Executar**, **Reiniciar**, **Gráfico** e **Sair**.
1. Botão `Executar` - inicia a simulação;
2. Botão `Reiniciar` - limpa os dados inseridos e permite uma nova execução; 
3. Botão `Gráfico` - gera um gráfico da trajetória;
4. Botão `Sair` - fechar o programa.

A ideia aqui foi constuir um ambiente gŕafico simples e intuitivo para que professores e alunos possam ter a melhor experiência de uso.

![Simulador](https://user-images.githubusercontent.com/115511374/196821761-6ab6ba0f-4a45-45b5-9a44-fef1c91ceb59.png)

Para que a simulação fique mais didática foi acrescentado a opção de mostrar o gráfico da Trajetória, isso foi feito usando a biblioteca Matplotlib.

![Grafico](https://user-images.githubusercontent.com/115511374/196822078-a0913dc2-d039-4764-9330-38ac0e7f6b07.png)

> [!IMPORTANT]
> Neste projeto foi usado a biblioteca `tkinter` para gerar a interface gráfica da simulação.
>
> Esta biblioteca já vem junto instalada com o `Python`. 
>
> Clone este projeto e excute o `requirements.txt`. O método correto depende do seu sistema operacional e de como o Python foi instalado inicialmente. 
>
> # Como verificar se o Tkinter está instalado?
> Antes de tentar qualquer instalação, verifique se o programa já está instalado no seu sistema executando o seguinte comando no terminal ou prompt de comando: 
> ```
> python -m tkinter
>```
> Se uma pequena janela do Tkinter abrir mostrando a versão do Tcl/Tk, significa que ele está instalado e funcionando corretamente. Se você receber um erro como "Nenhum módulo chamado tkinter", siga os passos de instalação para o seu sistema operacional. 
> 
> ## Windows
> No Windows, o Tkinter geralmente é incluído por padrão na instalação padrão do Python disponível no site oficial. 
> Caso você tenha perdido essa etapa durante a instalação: A solução mais fácil é executar o instalador do Python novamente, escolher a opção "Modificar" e garantir que o recurso "Tcl/Tk e IDLE" esteja selecionado antes de continuar a instalação.
>
> ## No Linux
> Em muitas distribuições Linux, o Tkinter não é instalado por padrão com o Python do sistema, mas está disponível através do gerenciador de pacotes do sistema. 
> ```
> sudo apt update
> sudo apt install python3-tk
> ```
>

