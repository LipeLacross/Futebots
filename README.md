# Futebots: Algoritmos Genéticos para Agentes de Futebol

Atividade em Python concebida pelo prof. Lucas Figueiredo. O objetivo é exercitar o conceito de algoritmos genéticos utilizando seleção natural para selecionar o melhor time de futebol de robôs ao longo da evolução de gerações.

## 🔨 Funcionalidades do Projeto

- **Simulação de Futebol de Robôs**: Utiliza algoritmos genéticos para simular o comportamento de jogadores de futebol robóticos, evoluindo suas estratégias ao longo das gerações.
- **Atualização de Posições e Velocidades**: A posição e a velocidade dos jogadores e da bola são atualizadas com base nas interações e nas regras do jogo.
- **Avaliação de Desempenho**: Avalia o desempenho dos times através de métricas como controle de bola, posicionamento e precisão de chutes.
- **Visualização do Jogo**: Renderiza o campo de futebol, jogadores e bola, além de exibir o placar e o tempo total de jogo, utilizando OpenCV para gráficos e manipulação de imagens.
- **Evolução dos Jogadores**: Ajusta os parâmetros dos jogadores com base na performance de suas ações, utilizando algoritmos genéticos para otimização contínua.
- **Interatividade**: Permite observar a evolução dos jogadores e a dinâmica do jogo em tempo real, com feedback visual e atualizações durante a simulação.

### Exemplo Visual do Projeto

![image](https://github.com/user-attachments/assets/63646d83-c00f-44e8-a36b-8303b6590516)


## ✔️ Técnicas e Tecnologias Utilizadas

- **Python**: Linguagem de programação usada para implementar o projeto.
- **OpenCV**: Biblioteca utilizada para visualização gráfica e manipulação de imagens.
- **Numpy**: Biblioteca para manipulação de arrays e operações matemáticas.

## 📁 Estrutura do Projeto

- **circle.py**: Define a classe `Circle` que representa um círculo com métodos para atualizar a posição e velocidade, e calcular vetores.
- **genes.py**: Define os tipos de genes e a classe `PlayerGenes` para representar as características genéticas dos jogadores.
- **main.py**: Contém a lógica principal do jogo, incluindo a simulação, atualização e visualização do estado do jogo.
- **map.py**: Define a classe `Map` que representa o campo de futebol e seus componentes, como as balizas.
- **painter.py**: Contém funções para desenhar o campo de futebol, jogadores, bola e placar na imagem.
- **README.md**: Documento de informações gerais do projeto.
- **requirements.txt**: Lista de dependências do projeto.
- **LICENSE**: Arquivo de licença do projeto.

## 🌐 Deploy

Para executar o projeto localmente, siga os passos abaixo:

1. **Clone o Repositório**:
```
git clone https://github.com/seu_usuario/futebots.git
cd futebots
```
2. **Crie e Ative um Ambiente Virtual**:
```
python -m venv venv
venv\Scripts\activate
```
2. **Instale as Dependências**:
```
pip install -r requirements.txt
```
4. **Execute o Projeto**:
```
python main.py
```
