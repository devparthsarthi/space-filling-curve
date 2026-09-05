# Space Filling Curve

A Python project for generating and visualizing the **Hilbert Space-Filling Curve** using coordinate transformations and recursion.

## What is a Space-Filling Curve?

A space-filling curve is a mathematical curve that maps a one-dimensional sequence into a two-dimensional space.

The **Hilbert curve**, introduced by David Hilbert in 1891, is one of the best-known examples.

As the order increases, the curve becomes increasingly detailed and approaches filling a square in the mathematical limit.

## Hilbert Curve

The number of points grows exponentially with the order:

| Order | Grid | Points |
|------:|------|-------:|
| 1 | 2 x 2 | 4 |
| 2 | 4 x 4 | 16 |
| 3 | 8 x 8 | 64 |
| 4 | 16 x 16 | 256 |
| 5 | 32 x 32 | 1,024 |
| 6 | 64 x 64 | 4,096 |

Formula:

```text
points = 4^order
```

## Features

- Generate Hilbert curve coordinates
- Convert a 1D Hilbert index into 2D coordinates
- Explore a recursive implementation
- Visualize the curve using Matplotlib
- Experiment with different curve orders

## Project Structure

```text
space-filling-curve/
|
├── hilbert.py
├── hilbert_recursive.py
└── README.md
```

### `hilbert.py`

Contains the main Hilbert curve implementation based on converting a one-dimensional index `d` into an `(x, y)` coordinate using quadrant selection, rotation/reflection, and coordinate transformations.

### `hilbert_recursive.py`

Contains an experimental recursive construction used for studying how Hilbert curves can be built recursively.

## Requirements

- Python 3
- Matplotlib

Install Matplotlib:

```bash
pip install matplotlib
```

## Run

Run the main visualizer:

```bash
python hilbert.py
```

Enter a Hilbert curve order when prompted. For example:

```text
Enter Hilbert curve order: 4
```

## How It Works

The main algorithm converts a one-dimensional index into a two-dimensional coordinate:

```text
1D index
   |
   v
Quadrant selection
   |
   v
Rotation / reflection
   |
   v
Coordinate transformation
   |
   v
(x, y)
```

The algorithm processes the curve through increasingly larger quadrants. Two bits of the index determine the quadrant at each level, while rotation and reflection preserve the required Hilbert traversal orientation.

## Applications

Space-filling curves are useful in areas such as:

- Spatial databases
- Image processing
- Geographic information systems
- Computer graphics
- Multidimensional indexing
- Cache and memory locality
- Spatial data organization

## Technologies

- Python
- Matplotlib
- Recursion
- Coordinate transformations
- Bitwise operations

## Author

Parthsarthi Sharma
