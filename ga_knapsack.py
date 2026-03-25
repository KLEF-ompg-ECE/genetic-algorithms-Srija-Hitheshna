"""
ga_knapsack.py  —  Genetic Algorithm: 0/1 Knapsack Problem
===========================================================
This program is COMPLETE and works as-is. DO NOT rewrite it.

Your task:
  1. Read the code and understand how it works
  2. Run the 2 experiments described in README.md
  3. Save the plots and fill in your observations in README.md

HOW TO RUN
----------
    python ga_knapsack.py

PROBLEM
-------
A trekker is packing a 15 kg backpack. There are 15 items to choose from,
each with a weight and a value score. Pick items that maximise total value
without exceeding the weight limit.
"""

import random
import matplotlib.pyplot as plt
import os

# =============================================================================
# PROBLEM DATA
# =============================================================================

ITEMS = [
    # (name,                weight_kg,  value)
    ("Water bottle",          2.0,   9),
    ("First aid kit",         1.5,  10),
    ("Tent",                  4.0,  10),
    ("Sleeping bag",          3.0,   9),
    ("Torch",                 0.5,   6),
    ("Energy bars (x6)",      1.0,   7),
    ("Rain jacket",           1.0,   8),
    ("Map & compass",         0.3,   7),
    ("Camera",                1.2,   5),
    ("Extra clothes",         2.0,   4),
    ("Cooking stove",         1.5,   6),
    ("Rope (10 m)",           2.5,   5),
    ("Sunscreen",             0.3,   4),
    ("Trekking poles",        1.5,   5),
    ("Power bank",            0.8,   6),
]

NUM_ITEMS  = len(ITEMS)
MAX_WEIGHT = 15.0   # kg

WEIGHTS = [item[1] for item in ITEMS]
VALUES  = [item[2] for item in ITEMS]
NAMES   = [item[0] for item in ITEMS]


# =============================================================================
# FITNESS FUNCTION
# =============================================================================

def fitness(chromosome):
    """
    Score a knapsack solution. Higher = better.

    If total weight exceeds MAX_WEIGHT -> score = 0 (invalid solution).
    Otherwise -> score = total value packed.

    Args:
        chromosome : binary list of length NUM_ITEMS
                     1 = pack this item,  0 = leave it behind
    """
    total_weight = sum(WEIGHTS[i] for i in range(NUM_ITEMS) if chromosome[i] == 1)
    total_value  = sum(VALUES[i]  for i in range(NUM_ITEMS) if chromosome[i] == 1)
    if total_weight > MAX_WEIGHT:
        return 0
    return total_value


# =============================================================================
# GA OPERATORS
# =============================================================================

def tournament_select(population, fitnesses, k=3):
    """Pick the best individual from k random candidates."""
    candidates = random.sample(range(len(population)), k)
    winner     = max(candidates, key=lambda i: fitnesses[i])
    return population[winner][:]


def crossover(p1, p2, rate=0.8):
    """Single-point crossover: combine two parents at a random cut point."""
    if random.random() > rate:
        return p1[:]
    cut = random.randint(1, NUM_ITEMS - 1)
    return p1[:cut] + p2[cut:]


def mutate(chromosome, rate):
    """
    Bit-flip mutation: each gene flips (0->1 or 1->0) with probability rate.

    EXPERIMENT 2: this rate is controlled by mutation_rate in run_ga()
    Try: 0.01  (very rare flips  - low diversity)
         0.05  (default          - balanced)
         0.30  (frequent flips   - too chaotic)
    """
    result = chromosome[:]
    for i in range(NUM_ITEMS):
        if random.random() < rate:
            result[i] = 1 - result[i]
    return result


# =============================================================================
# GENETIC ALGORITHM
# =============================================================================

def run_ga(
    population_size = 20,
    generations     = 50,
    crossover_rate  = 0.8,
    mutation_rate   = 0.05,   # <- EXPERIMENT 2: change this value
    tournament_size = 3,
    seed            = 42,
):
    """
    Run the Genetic Algorithm to maximise knapsack value.
