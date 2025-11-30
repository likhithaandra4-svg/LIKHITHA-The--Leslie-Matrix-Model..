Leslie Matrix Population Model

A biological simulation using Linear Algebra and Eigenvalue Analysis to predict age-structured population growth.

🧬 Overview

This project implements the Leslie Matrix model, a discrete-time model used in population ecology. It divides a population into specific age groups (Larvae, Juveniles, Adults) and uses a transition matrix to determine their survival and reproduction rates over time.

Mathematical Concepts Used

Matrices: To represent the state of the population and transition probabilities.

Eigenvalues: The dominant eigenvalue ($\lambda$) determines the long-term growth rate of the population.

$\lambda > 1$: Population grows.

$\lambda < 1$: Population declines.

$\lambda = 1$: Population is stable.

🚀 How to Run

Ensure you have Python installed.

Install the required dependencies:

pip install numpy matplotlib


Run the main simulation:

python src/main.py


Check the output/plots folder for the growth graph.

📂 Project Structure

src/models/: Contains the mathematical logic for the Leslie Matrix.

src/main.py: The entry point where biological parameters are configured.

output/: Stores generated simulation graphs.

Created as part of a Mathematical Modeling coursework.# LIKHITHA-The--Leslie-Matrix-Model..
Leslie Matrix Population Model
