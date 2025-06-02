# 🧭 Pathfinding Visualizer (Tkinter)

A Python-based visualizer for popular pathfinding algorithms, built with Tkinter. Allows interactive drawing of obstacles, start and end points, and visual demonstration of pathfinding logic.

![demo gif](https://res.cloudinary.com/dvjkkh0tf/image/upload/v1748866201/path_finding_visualizer_a_star_algo_jqzlgj.png)

---

## ✨ Features

- Drag to draw/remove walls
- Click to place start/end points
- Real-time visualization of various popular path finding algorithms like BFS, DFS, etc.
- Reset Board options

---

## 🛠 Requirements

- Python 3.x
- No external libraries required (only Tkinter)

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pathfinding-visualizer.git
   cd pathfinding-visualizer
   ```

2. Run Program:
   ```bash
    python main.py
   ```

## 🧑‍💻 How to use

- **`Dropdowns`** : Select algorithm and block type (Source, Destination, Wall, Free Space)
- **`Left Click + Drag:`** Place or remove blocks based on selected type
- **`Start Button:`** Runs the selected pathfinding algorithm
- **`Reset Button:`** Clears the entire grid and resets the board

## 🧠 Algorithms Implemented

- **⚡ A-Star Search**  
  An informed search using heuristics to find the shortest path more efficiently.

- **🔍 Best First Search**  
  Chooses the next node based solely on heuristic estimate to the goal (greedy approach).

- **📈 Breadth-First Search (BFS)**  
  Explores all neighbors level-by-level; finds the shortest path in unweighted graphs.

- **📉 Depth-First Search (DFS)**  
  Explores as far as possible along each branch before backtracking; not guaranteed shortest.

# 🤝 Contributing

Feel free to fork and submit pull requests if you'd like to add new features, implement new searching algorithms or fix bugs.
