# Probability Paradox Lab

A Python project exploring counterintuitive probability problems through mathematical derivations, Monte Carlo simulations, and statistical analysis.

The project investigates three probability problems:

- **Monty Hall Problem** — explores why switching doors increases the probability of winning.
- **Birthday Paradox** — demonstrates how quickly the probability of shared birthdays increases with group size.
- **Bayes' Theorem** — illustrates how prior probabilities and test accuracy affect the interpretation of a positive test result.

## Project Goals

- Explain the mathematical foundations behind each problem.
- Implement probability calculations using Python.
- Validate theoretical results through Monte Carlo simulations.
- Compare theoretical probabilities with simulated results.
- Write automated tests to verify the correctness of the implementations.

## Technologies

- Python
- NumPy
- Matplotlib
- Jupyter Notebook
- pytest
- Ruff

## Project Structure

```text
probability-paradox-lab/
├── main.ipynb
├── src/
│   ├── monty_hall.py
│   ├── birthday_paradox.py
│   └── bayes_simulation.py
├── tests/
│   ├── test_monty_hall.py
│   ├── test_birthday_paradox.py
│   └── test_bayes_simulation.py
├── README.md
└── requirements.txt
```


## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/ivanduzunov/probability-paradox-lab.git
cd probability-paradox-lab
```

Create and activate a virtual environment.

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```


## Running the Project

Open `main.ipynb` in Jupyter Notebook and run the cells sequentially to explore the mathematical explanations, simulations, and visualizations.

## Running Tests

Run the following command from the project root:

```bash
python -m pytest
```

## Code Quality

Run Ruff to check code style and identify potential issues:

```bash
ruff check .

The tests validate the mathematical calculations, input validation, and simulation results.

## Conclusion

This project demonstrates how mathematical probability and computational simulation can work together to investigate counterintuitive results and develop a deeper understanding of probability theory.
