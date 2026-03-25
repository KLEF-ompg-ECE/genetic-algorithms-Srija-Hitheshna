# Assignment 2 — Genetic Algorithm: Knapsack Problem
## Observation Report

Student Name  : B.Srija Hitheshna
Student ID    : 2310049143
Date Submitted: 21/03/2026  

---

## How to Submit

1. Run each experiment following the instructions below
2. Fill in every answer box — do not leave placeholders
3. Make sure the plots/ folder contains all required images
4. Commit this README and the plots/ folder to your GitHub repo

---

## Before You Begin — Read the Code

Open ga_knapsack.py and read through it. Then answer these questions.

Q1. What does the `fitness()` function return? Why does an overweight solution score 0?

The fitness() function calculates the total value of the selected items in the knapsack. 
If the total weight exceeds the maximum capacity of the knapsack, the solution is considered invalid and the fitness value becomes 0. 
This penalty prevents overweight solutions from being selected in the next generation.

Q2. What does `tournament_select()` do? Why are higher-fitness individuals more likely to be chosen?

The tournament_select() function randomly chooses a small group of individuals from the population and selects the one with the highest fitness. 
Since the individual with the best fitness wins the tournament, stronger solutions have a higher chance of being selected. 
This helps the genetic algorithm gradually improve the population over generations.

Q3. Look at the `run_ga()` loop. Find this line:
next_gen = [best_chromosome[:]]
What is this doing? Why is it important to always keep the best solution?

This line copies the best chromosome from the current generation into the next generation. 
This technique is called elitism and ensures that the best solution found so far is not lost during crossover or mutation. 
Keeping the best solution helps maintain steady improvement in the genetic algorithm.

---

## Experiment 1 — Baseline Run

Instructions: Run the program without changing anything.
python ga_knapsack.py

Fill in this table:

| Metric                             | Your result |
| ---------------------------------- | ----------- |
| Number of generations              | 50          |
| Best value at generation 1         | 60          |
| Final best value                   | 77          |
| Total weight of best solution (kg) | 14.4 kg     |
| Is solution valid (Yes / No)       | Yes         |

Copy the printed packing list here:
Water bottle
First aid kit
Sleeping bag
Torch
Energy bars (x6)
Rain jacket
Map & compass
Cooking stove
Rope (10 m)
Sunscreen
Power bank

Look at `plots/experiment_1.png` and describe what you see (2–3 sentences).  
*Where does the biggest improvement happen? Does the curve flatten at some point?*
The graph shows a rapid increase in the fitness value during the first few generations, indicating that the genetic algorithm quickly finds better solutions. The biggest improvement happens in the early generations as good item combinations are discovered. After several generations, the curve begins to flatten, which means the algorithm has converged to a near optimal solution.

---

## Experiment 2 — Effect of Mutation Rate

Instructions: In ga_knapsack.py, find the # EXPERIMENT 2 block in __main__.  
Copy it three times and run with mutation_rate = 0.01, 0.05, and 0.30.  
Save plots as experiment_2a.png, experiment_2b.png, experiment_2c.png.

Results table:

| mutation_rate | Final best value | Weight (kg) | Valid? | Shape of curve                              |
| ------------- | ---------------- | ----------- | ------ | ------------------------------------------- |
| 0.01          | 75               | 14.9        | Yes    | Slow improvement, converges early           |
| 0.05          | 77               | 14.4        | Yes    | Smooth convergence                          |
| 0.30          | 78               | 14.1        | Yes    | More fluctuations but finds better solution |
