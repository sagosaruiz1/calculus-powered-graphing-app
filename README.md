# Calculus-Powered Graphing App

A desktop application built with Python and Tkinter that lets you visualize mathematical functions, compute definite integrals (area under/between curves), and display derivatives — all with an interactive GUI.

---

## Features

- **Area Under a Curve** — Calculate and visualize the definite integral of f(x) over a given interval [a, b]
- **Area Between Two Curves** — Compute the area between f(x) and g(x) over a given interval
- **Derivative Visualization** — Automatically computes and plots f'(x) alongside f(x)
- **Symbolic Math** — Uses SymPy for exact symbolic differentiation and pretty-printed results
- **Fraction Output** — Displays the computed area as both a decimal and a simplified fraction
- **Dynamic Background** — Resizable window with a custom background image
- **Graph Export** — Saves the generated plot as a PNG file

---

## Tech Stack

| Library | Purpose |
|---|---|
| `tkinter` | GUI framework |
| `sympy` | Symbolic differentiation |
| `numpy` | Numerical computation |
| `scipy` | Numerical integration (`quad`) |
| `matplotlib` | Plot generation |
| `Pillow` | Background image handling |

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/calculus-powered-graphing-app.git
cd calculus-powered-graphing-app
```

**2. Install dependencies**
```bash
pip install sympy numpy scipy matplotlib Pillow
```

**3. Add required assets**

Make sure the following files exist in an `assets/` folder:
```
assets/
├── background.jpg
└── calculus_logo.png
```

**4. Run the app**
```bash
python main.py
```

---

## Usage

1. **Select a mode** — Choose between *Area Under Curve* or *Between Curves*
2. **Enter your function(s)** — Type a valid Python/SymPy expression for f(x) (and g(x) if using Between Curves mode)
3. **Set the interval** — Enter the starting point `a` and ending point `b`
4. **Click "Calculate & Plot"** — The app will:
   - Display the computed area (decimal + fraction) and the derivative formula
   - Generate and show an interactive Matplotlib plot
   - Save the plot as `rename_this_image.png`

**Example expressions:**
```
x**2
sin(x)
x**3 - 2*x + 1
exp(-x)
```

---

## Project Structure

```
├── main.py          # Main app entry point and GUI (CalculusApp class)
├── calc_logic.py    # Core math: numerical derivative and integral functions
├── visualizer.py    # Matplotlib plot generation and export
└── assets/
    ├── background.jpg
    └── calculus_logo.png
```

---

## Notes

- Function input uses standard Python/SymPy syntax (e.g., `x**2` not `x^2`)
- The plot is saved as `rename_this_image.png` in the working directory — rename as needed
- Make sure `a < b` for correct integral computation

---

## Contributing

Pull requests are welcome! Feel free to open an issue for bugs or feature suggestions.
