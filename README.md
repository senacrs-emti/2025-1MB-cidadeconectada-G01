# 📜 Readme Template — Semáforos Inteligentes Interligados
_____________________________________________

🚦 Projeto: Semáforos Inteligentes Interligados

Grupo: G01
_____________________________________________

📌 Sobre o Projeto

O Sistema de Semáforos Inteligentes Interligados simula um ambiente de mobilidade urbana onde dois semáforos se comunicam entre si e operam de forma automática.

Cada semáforo possui sensores que detectam veículos.
Quando um carro é identificado em um semáforo fechado, o sistema analisa o estado do outro semáforo.
Se ele estiver aberto, ele é fechado para priorizar o veículo detectado. Depois, o sistema volta ao seu ciclo normal.

A solução integra Arduino, Python, HTML, CSS e JavaScript, mostrando como tecnologias diversas podem criar soluções para cidades inteligentes.

_____________________________________________

🛠️ Tecnologias Utilizadas

HTML, CSS & JavaScript — Interface Web

Python & Arduino — Lógica e funcionamento do sistema

Git & GitHub — Controle de versão e colaboração
_____________________________________________

⚙️ Funcionalidades Principais
🔹 1. Detecção e Prioridade Inteligente

O sistema identifica a presença de veículos e abre automaticamente o semáforo necessário.

🔹 2. Comunicação Entre Semáforos

Os dois controladores se comunicam em tempo real, garantindo segurança e evitando conflitos de sinalização.
_____________________________________________

🗂️ Arquitetura do Projeto
/2025-1MB-cidadeconectada-G01
│
├── html_css/
│   ├── img/
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
_____________________________________________

📦 Pré-requisitos e Dependências
🐍 Python

Instale todas as dependências:

pip install -r requirements.txt

🛠️ Arduino

Requisitos:

Arduino IDE instalada

Placa configurada (ex.: Arduino Uno)

Porta COM correta selecionada

Upload do arquivo:

semaforo_sss/sistema_semaforo.ino
_____________________________________________

🎬 Demonstração

-----------------------

👥 Equipe

Arthur Rocha

Lorenzo Lopes

Victor Muller

Felipe Fedatto
_____________________________________________

📌 Status do Projeto

🚧 Em desenvolvimento

