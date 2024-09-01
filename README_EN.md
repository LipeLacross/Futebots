# Futebots: Genetic Algorithms for Soccer Agents

Activity in Python designed by Professor Lucas Figueiredo. The objective is to exercise the concept of genetic algorithms using natural selection to select the best robot soccer team throughout the evolution of generations.

## 🔨 Project Features

- **Robot Soccer Simulation**: Uses genetic algorithms to simulate the behavior of robotic soccer players, evolving their strategies over generations.
- **Position and Speed Updates**: The position and speed of players and the ball are updated based on interactions and game rules.
- **Performance Evaluation**: Assesses team performance through metrics such as ball control, positioning, and shot accuracy.
- **Game Visualization**: Renders the soccer field, players, and ball, displaying the score and total game time using OpenCV for graphics and image manipulation.
- **Player Evolution**: Adjusts player parameters based on the performance of their actions, using genetic algorithms for continuous optimization.
- **Interactivity**: Allows observation of player evolution and game dynamics in real time, with visual feedback and updates during the simulation.

### Visual Example of the Project

![image](https://github.com/user-attachments/assets/63646d83-c00f-44e8-a36b-8303b6590516)

## ✔️ Techniques and Technologies Used

- **Python**: Programming language used to implement the project.
- **OpenCV**: Library used for graphical visualization and image manipulation.
- **Numpy**: Library for array manipulation and mathematical operations.

## 📁 Project Structure

- **circle.py**: Defines the `Circle` class representing a circle with methods to update position and speed, and calculate vectors.
- **genes.py**: Defines gene types and the `PlayerGenes` class to represent the genetic characteristics of players.
- **main.py**: Contains the main game logic, including simulation, updating, and visualization of the game state.
- **map.py**: Defines the `Map` class representing the soccer field and its components, such as goals.
- **painter.py**: Contains functions to draw the soccer field, players, ball, and score on the image.
- **README.md**: General information document about the project.
- **requirements.txt**: List of project dependencies.
- **LICENSE**: Project license file.

## 🌐 Deploy

To run the project locally, follow the steps below:

1. **Clone the Repository**:
```
git clone https://github.com/seu_usuario/futebots.git
cd futebots
```
2. **Create and Activate a Virtual Environment**:
```
python -m venv venv
venv\Scripts\activate
```
2. **Install Dependencies**:
```
pip install -r requirements.txt
```
4. **Run the Project**:
```
python main.py
```
