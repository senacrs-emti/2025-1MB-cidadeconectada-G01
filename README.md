# Cidade Conectada – Projeto G01  

Grupo: G01  

#Sobre o Projeto
O projeto Semáforos Inteligentes Interligados simula um sistema de mobilidade urbana onde dois semáforos se comunicam e trabalham de forma automática. Cada semáforo possui sensores que detectam a presença de veículos.

Quando um carro é identificado em um semáforo fechado, o sistema verifica o outro semáforo: se ele estiver aberto, é fechado para dar prioridade ao veículo detectado. Depois, tudo volta ao ciclo normal.

A solução integra Arduino, Python HTML, CSS e JavaScript, mostrando como tecnologias diferentes podem trabalhar juntas para criar recursos aplicáveis a cidades inteligentes.


##Tecnologias Utilizadas
-HTML, CSS & JS - Para interface WEB
-Python & Arduino - para logica e funcionamento do codigo
-Git & GitHub - para controle de versão & colaboração dos membros

##Funcionalidades Principais 
1- Detecção e Prioridade Inteligente: sensores identificam veículos e o sistema decide automaticamente qual semáforo deve abrir, dando prioridade ao fluxo necessário.

2-  Comunicação Entre Semáforos: os dois semáforos trocam informações em tempo real, garantindo que nunca fiquem abertos simultaneamente e mantendo o controle seguro do cruzamento.


##Arquitetura do Projeto
/2025-1MB-cidadeconectada-G01
│
├── html_css/
│   ├── img/
│   │
│   ├── pagina_inicial.html
│   ├── pagina_inicial.css
│   ├── sobre.html
│   └── style.css
│
├── semaforo_sss/
│   ├── sistema_semaforo.ino
│   └── sistema_semaforo.py
│
└── README.md

##Pré-requisitos e Dependências
-Python

Para executar o controlador dos semáforos, instale todas as dependências com:

pip install -r requirements.txt

-Arduino

Para rodar o código do semáforo físico é necessário:

Arduino IDE instalada

Placa configurada (ex.: Arduino Uno)

Porta COM selecionada corretamente

Upload do arquivo:

semaforo_sss/sistema_semaforo.ino

##Demonstração

-
-
-
--
-

##Equipe
Arthur Rocha
Lorenzo Lopes
Victor Muller
Felipe Fedatto

##Status do Projeto
Em desenvolvimento



