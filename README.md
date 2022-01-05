# SSC0511-GameProject
SSC0511 - Organização de Computadores Digitais

Professor: Eduardo do Valle Simões

Email: simoes@@@@@@@icmc.usp.br

Departamento de Sistemas de Computação – ICMC - USP

Grupo de Sistemas Embarcados e Evolutivos

Laboratório de Computação Reconfigurável

# The Riddler

Descrição : O nome do jogo faz referência ao inimigo do batman Edward Nygma, mais conhecido por <b>Charada</b>. 
O jogo consiste em 8 enigmas que exigem uma resposta de apenas <b>uma</b> palavra. Cada enigma contém uma dica para resolve-lo. Alguns dos enigmas foram tirados da série Arkham e outros criados por nós mesmos. Todas as dicas foram criadas pelo grupo.

Notas sobre a implementação:
  - O jogo implementa um buffer livre para a resposta, ou seja, o usuário pode digitar a palavra e o programa fará a validação se a resposta está correta.
  - Foi necessário editar o código do simulador, particularmente o arquivo do controlador <i><b>Controller.cpp</b></i>, e adicionar a tecla BackSpace para que fosse identificada corretamente com o código ascii 08.
 
Link do vídeo de apresentação:
