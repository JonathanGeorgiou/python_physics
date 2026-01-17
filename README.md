# Python Physics Simulation

A simple, modular orbital mechanics simulation built with Python, Pydantic, and Matplotlib.
The intention behind this project is to learn more about Python and apply that to my interests in physics.


## Overview

This project simulates the orbital path of the Earth around the Sun using Newton's Law of Universal Gravitation and Euler integration. It is designed with professional Python best practices in mind, including:

- **Modular Architecture**: Logic, data models, and constants are separated into distinct packages.
- **Type Safety**: Uses `Pydantic` for data validation and clear type hinting.
- **Separation of Concerns**: Decoupled physics engine from the visualization layer.

## Project Structure

```text
python_physics/
├── data/
│   └── bodies.py          # Pre-defined celestial bodies (Earth, Sun)
├── physics/
│   ├── models.py          # Pydantic data models for Vectors and Bodies
│   ├── physical_constants.py  # Scientific constants (G)
│   └── orbital_mechanics.py   # The physics engine and orbit calculations
├── main.py                # Entry point for running the simulation
├── pyproject.toml         # Dependency management
└── .gitignore             # Standard Python git exclusions
```

## Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python_physics.git
   cd python_physics
   ```

2. Install dependencies:
   ```bash
   uv sync
   # OR
   pip install matplotlib pydantic
   ```

### Running the Simulation

Execute the main script to run the simulation and view the Matplotlib plot:

```bash
python main.py
```

## How It Works

The simulation uses a discrete time-step approach:
1. **Acceleration**: Calculated using $F = G \frac{m_1 m_2}{r^2}$.
2. **Velocity**: Updated by adding acceleration $\times$ time step ($dt$).
3. **Position**: Updated by adding velocity $\times$ time step ($dt$).

## Future Plans

- [ ] Real-time animation using Pygame.
- [ ] Support for multiple bodies (Moon, Mars, etc.).
- [ ] 3D visualization.
