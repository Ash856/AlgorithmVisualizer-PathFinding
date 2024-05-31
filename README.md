![AVicon](https://github.com/Ash856/AlgorithmVisualizer-PathFinding/assets/92754191/fbbb1bf4-0f6b-4c11-8cb1-de31f8bdafee)



# Algorithm Visualizer for path finding

This is a Python-based pathfinding algorithm visualizer that helps demonstrate how various pathfinding algorithms work. This visualizer is build in the form of an Interactive desktop game. It provides a graphical interface to visualize the process of finding the shortest path between two points in a grid layout.

## Features
- Visualize popular pathfinding algorithms such as:
  - A* Search
  - Dijkstra's Algorithm
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Greedy Best First Search (GBFS)
- Interactive grid for setting start and end points
- Ability to place and remove obstacles in the grid
- Real-time visualization of the algorithm's progress
- Ability to generate random mazes for the algorithm to solve
- Compare all the algorithms in the same environment via factors like time taken and comparisons done by each algorithm

## Algorithms visualized
- A* Search : A* Search is a pathfinding algorithm that uses both the actual distance from the start node and the estimated distance to the end node to find the shortest path. The formula used is f(n) = g(n) + h(n), where g(n) is the cost from the start node to the current node, and h(n) is the heuristic that estimates the cost from the current node to the end node.

- Dijkstra's Algorithm : Dijkstra's Algorithm is a pathfinding algorithm that guarantees the shortest path by expanding nodes in all directions uniformly until the end point is reached. It uses a priority queue to explore nodes with the smallest known distance from the start node.

- Breadth-First Search (BFS) : Breadth-First Search is a pathfinding algorithm that explores all nodes at the present depth level before moving on to nodes at the next depth level. This ensures that the shortest path is found in an unweighted grid.

- Depth-First Search (DFS) : Depth-First Search is a pathfinding algorithm that explores as far as possible along each branch before backtracking. It does not guarantee the shortest path but is useful for exploring all possible paths.

- Greedy Best-First Search : Greedy Best-First Search is a heuristic-based pathfinding algorithm that focuses on the estimated distance from the current node to the end node. It selects the node that appears to be closest to the goal according to the heuristic and expands it next.
## Demo

https://github.com/Ash856/AlgorithmVisualizer-PathFinding/assets/92754191/798954bb-32f1-43cf-aad4-4596ad6c9077


## Scope

This project can be used by the following :

- Students for understanding and learning about the working of algorithms
- Teachers to teach algorithms
- Curious minds to staisfy thier curiousity
- For anyone who would like to play with algorithms
- Developers for inspiration and knowledge


## Screenshots and Videoclips

### Astar
https://github.com/Ash856/AlgorithmVisualizer-PathFinding/assets/92754191/6eaa71ac-be64-4507-93dc-89293cafd62f

### BFS
https://github.com/Ash856/AlgorithmVisualizer-PathFinding/assets/92754191/93367d48-0b70-445f-aef5-61eafe40624a

### DFS
https://github.com/Ash856/AlgorithmVisualizer-PathFinding/assets/92754191/f111b0e7-59eb-4537-901b-03b273dae6b0

### Dijkstra's
https://github.com/Ash856/AlgorithmVisualizer-PathFinding/assets/92754191/98253ad4-8081-42bc-ae82-284c26772b3c

### GBFS

## Dependencies

- Pygame
- tinkter
## Installation

To get started with the pathfinding algorithm visualizer, follow these steps:

#### Clone the repository or download all the files
```bash
git clone https://github.com/Ash856/AlgorithmVisualizer-PathFinding.git
```

#### Set up Python environment

Ensure you have Python 3 installed. You can download it from the official Python website.

#### Install dependencies
The project relies on Pygame and Tkinter for its graphical interface. You need to install these dependencies using pip and your system's package manager if necessary.

For Pygame:

```bash
pip install pygame
```

For Tkinter:

Tkinter is usually included with Python, but if you need to install it separately, you can do so. 

#### Run the visualizer
Open the code in vs code or any ide and simply run the main.py

or

In terminal

Navigate to the directory where the main.py file is located and run it:

```bash
cd AlgorithmVisualizer-PathFinding
```
```bash
python main.py
```

This setup will ensure that you have all the necessary dependencies installed, allowing you to run the pathfinding algorithm visualizer without any issues.if you face any issues installing pygame or python visit their official website for step by step procedure

## Controls
#### Mouse:
- Right-click : place start , end and barriers in the respective order (drag the mouse to draw long barriers)

- Left-click : to remove start , end or barriers (Erase blocks)

#### Keyboard:
- Press H or ESC : for help or how to use instructions
- Press A : To run Astar search
- Press B : To run BFS algorithm
- Press D : To run DFS algorithm
- Press J : To run Dijkstra's algorithm
- Press G : To run Greedy best first search
- Press C : To clear everything to default
- Press K : To clear everything except start , end and the barriers
- Press M : To generate random mazes
- Press W : To compare all the algorithms in one situation and display statistics like time taken and number of comparisons done

#### Tips : 

Place the start and end after maze is generated.

Don't click outside the game window.

After a pop message appears on screen click ok and then click on screen again to resume normal functionalities



## Motivation and lessons

The main motivation of this project was to visualize popular algorithms and some how be able to create a interactive playground for learning and understanding these algorithms and also develop it in python to strengthen my programming skills and expand my learning.

Lessons I learned along and skills gained:
 - A deeper understanding of how different algorithms work.
 - Gained new skills by using tools like pygame ,tinkter and python .
 - A greater understanding of the Data structures used to implement the algorithms in python.
 - Better understanding of the Time and space complexity of each algorithm and their varied performance according to the situation(some algorithms work exceptionally well in some environment while remain average in others)


## Optimizations and future improvements

 - Use better data structures to implement the current algortihms like instead of list to implement stack for dfs use deqeue or numpy for better time complexity and improve performance.
 -  Remove tinkter and make it completely into a game with play,pause and various buttons.
 - Add music and sounds.
 - Generate better quality mazes.
 - Current version only has non weighted graph or grid so make a weighted feature.
 - Add more path finding algortihms





## Resources and references

- Youtube channels : 

    Major thanks to 
  - Tech With Tim : https://youtu.be/JtiK0DOeI4A?si=MidAi_Mzmls04R08
  for idea , inspiration and getting started.

  - Gatesmashers , Abdul bari and others for Data structures in python

- Websites :
  - Geeksforgeeks , pygame docs , github and others  
