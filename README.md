# SSC0511 - Projeto de jogo em Assembly
SSC0511 - Organização de Computadores Digitais

Professor: Eduardo do Valle Simões

Email: simoes@@@@@@@icmc.usp.br

Departamento de Sistemas de Computação – ICMC - USP

Grupo de Sistemas Embarcados e Evolutivos

Laboratório de Computação Reconfigurável

# The Riddler

Descrição : O nome do jogo faz referência ao inimigo do Batman Edward Nygma, mais conhecido por <b>Charada</b>. 
O jogo consiste em 8 enigmas que exigem uma resposta de apenas <b>uma</b> palavra. Cada enigma contém uma dica para resolvê-lo. Alguns dos enigmas foram tirados da série Arkham e outros criados por nós mesmos. Todas as dicas foram criadas pelo grupo.

Notas sobre a implementação:
  - O jogo implementa um buffer livre para a resposta, ou seja, o usuário pode digitar a palavra e o programa fará a validação se a resposta está correta.
  - Foi necessário editar o código do simulador, particularmente o arquivo do controlador <i><b>Controller.cpp</b></i>, e adicionar a tecla BackSpace para que fosse identificada corretamente com o código ascii 08.
 
Link do vídeo de apresentação:

# Screenshots

### Tela Inicial
<img src='https://user-images.githubusercontent.com/45838334/148437455-4ac590ae-1044-4059-aa81-fd4152793a02.png' height='375'>

### Primeira charada
<img src='https://user-images.githubusercontent.com/45838334/148437029-1ca6dedb-248b-4a34-ad60-32976340b00c.png' height='375'>

### Tela de Game Over
<img src='https://user-images.githubusercontent.com/45838334/148437146-a76405bc-19f7-40c3-9ee3-ed4e08bdd364.png' height='375'>
