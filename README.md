```
    __  ___                      
   /  |/  /___ _____  ____ _____ 
  / /|_/ / __ `/ __ \/ __ `/ __ \
 / /  / / /_/ / / / / /_/ / / / /
/_/  /_/\__,_/_/ /_/\__,_/_/ /_/ 
                                
```

# Calculator

A modular command-line calculator built with Python, designed to handle a wide range of operations including arithmetic, algebra, trigonometry, logarithms, and calculus. This project emphasizes clean code organization, extensibility, and foundational learning in symbolic computation.

⚠️ **Note:** This project is actively being developed. Stay tuned for updates and improvements!
---

## 📁 Project Overview

```
calculator-advance/
├── basic.py              → Core arithmetic operations
├── calculus_module.py    → Symbolic differentiation & integration
├── trigno.py             → Trig functions with degree/radian support
├── algebra.py            → Simplify, expand, factor expressions
├── log.py                → Logarithmic operations (base 10, e, etc.)
├── calculator.py         → CLI interface and dispatcher logic
└── README.md             → You're reading it
```

---

## 🚀 Features

- Modular design with each domain in its own file
- Symbolic math using `sympy`
- Supports user-friendly input via CLI
- Easy to expand with more math domains

---

## 🔧 Requirements

- Python 3.10+
- Libraries:
  - [`sympy`](https://pypi.org/project/sympy/)
  - `math` (standard library)
  - `pytest`(for testing)

Install dependencies:

```bash
pip install sympy
pip install pytest
```

---

## 🕹️ How to Run

Run the main script:

```bash
python calculator.py
```

Follow the interactive menu to select the type of operation:
- Arithmetic
- Trigonometry
- Algebra
- Calculus
- Logarithms

---

## 🎯 Project Goals

This project was built to:
- Improve my understanding of modular Python code
- Learn symbolic computation with SymPy
- Practice version control and GitHub workflows
- Eventually expand into a GUI-based tool

---

## 📌 Roadmap

- [ ] Add matrix operations  
- [ ] Complex number support  
- [ ] GUI version (Tkinter or PyQT)  
- [ ] Unit tests and coverage reports  

---

## 👨‍💻 Author

**Manan Sharma**  
Aspiring computer scientist. Passionate about absurdism, logic, and building things that (sort of) make sense.

> “Embracing the absurdity of life 🌌✨”

---

## 🪪 License

This project is licensed under the MIT License.  
Feel free to use, modify, or contribute.
