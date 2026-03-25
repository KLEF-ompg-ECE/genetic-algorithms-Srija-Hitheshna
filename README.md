# Assignment 2 — Genetic Algorithm: Knapsack Problem
## Observation Report

**Student Name  :** B.Srija Hitheshna
**Student ID    :** 2310049143
**Date Submitted:** 21/03/2026  

---

## How to Submit

1. Run each experiment following the instructions below
2. Fill in every answer box — do not leave placeholders
3. Make sure the `plots/` folder contains all required images
4. Commit this README and the `plots/` folder to your GitHub repo

---

## Before You Begin — Read the Code

Open `ga_knapsack.py` and read through it. Then answer these questions.

**Q1. What does the `fitness()` function return? Why does an overweight solution score 0?**

```
The fitness() function calculates the total value of the selected items in the knapsack. 
If the total weight exceeds the maximum capacity of the knapsack, the solution is considered invalid and the fitness value becomes 0. 
This penalty prevents overweight solutions from being selected in the next generation.
```

**Q2. What does `tournament_select()` do? Why are higher-fitness individuals more likely to be chosen?**

```
The tournament_select() function randomly chooses a small group of individuals from the population and selects the one with the highest fitness. 
Since the individual with the best fitness wins the tournament, stronger solutions have a higher chance of being selected. 
This helps the genetic algorithm gradually improve the population over generations.
```

**Q3. Look at the `run_ga()` loop. Find this line:**
```python
next_gen = [best_chromosome[:]]
```
**What is this doing? Why is it important to always keep the best solution?**

```
This line copies the best chromosome from the current generation into the next generation. 
This technique is called elitism and ensures that the best solution found so far is not lost during crossover or mutation. 
Keeping the best solution helps maintain steady improvement in the genetic algorithm.
```

---

## Experiment 1 — Baseline Run

**Instructions:** Run the program without changing anything.
```bash
python ga_knapsack.py
```

**Fill in this table:**

| Metric                             | Your result |
| ---------------------------------- | ----------- |
| Number of generations              | 50          |
| Best value at generation 1         | 60          |
| Final best value                   | 77          |
| Total weight of best solution (kg) | 14.4 kg     |
| Is solution valid (Yes / No)       | Yes         |

**Copy the printed packing list here:**
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

**Look at `plots/experiment_1.png` and describe what you see (2–3 sentences).**  
*Where does the biggest improvement happen? Does the curve flatten at some point?*
```
The graph shows a rapid increase in the fitness value during the first few generations, indicating that the genetic algorithm quickly finds better solutions. The biggest improvement happens in the early generations as good item combinations are discovered. After several generations, the curve begins to flatten, which means the algorithm has converged to a near optimal solution.
```

---

## Experiment 2 — Effect of Mutation Rate

**Instructions:** In `ga_knapsack.py`, find the `# EXPERIMENT 2` block in `__main__`.  
Copy it three times and run with `mutation_rate` = **0.01**, **0.05**, and **0.30**.  
Save plots as `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`.

**Results table:**

| mutation_rate | Final best value | Weight (kg) | Valid? | Shape of curve                              |
| ------------- | ---------------- | ----------- | ------ | ------------------------------------------- |
| 0.01          | 75               | 14.9        | Yes    | Slow improvement, converges early           |
| 0.05          | 77               | 14.4        | Yes    | Smooth convergence                          |
| 0.30          | 78               | 14.1        | Yes    | More fluctuations but finds better solution |


**Compare the three plots. What happens when mutation is too low? Too high? (3–4 sentences)**  
*Hint: Too low = no diversity, may get stuck. Too high = random search. What is the sweet spot?*
```
When the mutation rate is very low (0.01), the genetic algorithm explores fewer new solutions and may converge slowly or get stuck in local optimum solutions. With a moderate mutation rate (0.05), the algorithm balances exploration and exploitation and shows a smoother convergence. When the mutation rate is high (0.30), the search becomes more random and the curve fluctuates more, but it may discover better solutions due to higher diversity in the population.
```

**Which mutation_rate gave the best result? Why do you think that is?**
```
The mutation rate of 0.30 produced the best result with a final value of 78. A higher mutation rate introduces more diversity in the population, allowing the algorithm to explore more possible combinations of items. This increased exploration helped the algorithm find a slightly better solution for the knapsack problem.
```

---

## Summary

**Complete this table with your best result from each experiment:**

| Experiment        | Key setting          | Final value | Main finding in one sentence                                                                           |
| ----------------- | -------------------- | ----------- | ------------------------------------------------------------------------------------------------------ |
| 1 — Baseline      | mutation_rate = 0.05 | 77          | The genetic algorithm quickly improved the solution and converged to a stable value around 77.         |
| 2 — Mutation rate | mutation_rate = 0.30 | 78          | Increasing the mutation rate introduced more diversity and helped discover a slightly better solution. |


**In your own words — what is the most important thing you learned about Genetic Algorithms from these experiments? (3–5 sentences)**
```
From these experiments I learned that genetic algorithms improve solutions gradually over generations using selection, crossover, and mutation. The mutation rate plays an important role because it controls the diversity of solutions in the population. If the mutation rate is too low, the algorithm may get stuck in local optimum solutions. If it is too high, the search becomes more random. A balanced mutation rate helps the algorithm explore new solutions while still converging toward an optimal result.
```

---

## Submission Checklist

- [x] Student name and ID filled in
- [x] Q1, Q2, Q3 answered
- [x] Experiment 1: table filled, packing list pasted, plot observation written
- [x] Experiment 2: results table filled (3 rows), observation and answer written
- [x] Summary table completed and reflection written
- [x] `plots/` contains: `experiment_1.png`, `experiment_2a.png`, `experiment_2b.png`, 
