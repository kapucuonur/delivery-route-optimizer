# Delivery Route Optimizer 🚚

> **"From the Streets to the Codebase"**
> *Built by a former Wolt Courier Partner turned Software Developer.*

## 💡 Inspiration & Backstory

Having worked as a **Wolt Courier Partner** in Finland, I experienced firsthand how critical efficient routing is for both customer satisfaction and courier earnings. I often faced scenarios where optimal pathfinding could save precious minutes during rush hour.

This project is not just a coding exercise; it is my engineering attempt to solve a real-world logistical challenge I lived through. I wanted to build a tool that visualizes and optimizes delivery routes using the algorithms I learned during my transition from courier to developer.

---

## 🚀 Project Overview

A professional, modular Python application for **AI-Powered Logistics**. It uses **Custom Machine Learning Algorithms** to solve Fleet Management problems and heuristic algorithms for route optimization.

### Key Features

*   **🤖 AI Fleet Management**: Includes a **custom, pure Python implementation** of the **K-Means Clustering** algorithm to intelligently assign orders to multiple drivers based on geographic clusters. (No heavy dependencies like sklearn needed!)
*   **🏎️ Route Optimization**: Solves the Traveling Salesperson Problem (TSP) for each driver.
*   **📊 Business Intelligence**: Calculates efficiency gains and total fleet distance.
*   **🗺️ Interactive Visualization**: Generates responsive maps with distinct colors for each driver's route.
*   **🏗️ Modular Architecture**: Clean, testable, and scalable Python package structure.

## 📂 Project Structure

This project follows Senior Engineering standards for maintainability and scalability:

```
delivery-route-optimizer/
├── delivery_optimizer/       # Main Package
│   ├── ai_utils.py           # [AI] Custom K-Means Clustering Algorithm
│   ├── algorithm.py          # [Algo] Route Optimization Logic
│   ├── geography.py          # [Math] Coordinate Utilities
│   └── visualizer.py         # [UI] Multi-Vehicle Map Generation
├── tests/                    # Unit Tests
├── main.py                   # CLI Entry Point
└── requirements.txt          # Dependencies (folium)
```

## 🛠 Installation

The easiest way to set up the project is using `make`:

```bash
make install
```

Or manually:

1.  Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd delivery-route-optimizer
    ```

2.  Create virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

### Quick Start (Recommended)
Run the AI simulation with one command:

```bash
make run
```
This runs the full simulation with **30 stops** and **3 vehicles**.

### Manual Usage
If you prefer running commands manually, ensure you use the python from the virtual environment:

#### Single Driver (Classic Mode)
Optimize a route for a single courier:

```bash
venv/bin/python3 main.py --stops 20
```

### AI Fleet Management (Multi-Driver Mode)
Simulate a real logistics scenario. Distribute **50 orders** among **3 drivers**:

```bash
python3 main.py --stops 50 --vehicles 3
```

**Output:**
- The AI will cluster orders into 3 optimal zones.
- Each driver gets a distinct colored route on `delivery_map.html`.
- Returns total fleet distance and individual route details.

## 🏭 Production Engineering (Applied Science)

To demonstrate readiness for a production environment, this project includes:

*   **Dockerization 🐳**: Full container support to ensure the application runs consistently across any environment.
*   **CI/CD Pipeline 🔄**: Automated GitHub Actions workflow (`tests.yml`) that runs unit tests on every push, ensuring code reliability and preventing regressions.

### Running with Docker

Build the image:
```bash
docker build -t delivery-optimizer .
```

Run the container:
```bash
docker run -v $(pwd):/app delivery-optimizer
```

## 🏗 Tech Stack

*   **Python 3.10+** (Pure Python Implementation)
*   **Folium**: Geospatial Visualization.
*   **Argparse**: CLI Management.
