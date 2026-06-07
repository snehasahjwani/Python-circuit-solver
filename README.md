# Modified Nodal Analysis: A Python Circuit Solver

A Python-based DC circuit solver built from scratch using Modified Nodal Analysis (MNA).

## What it does
- Takes a user-defined circuit as input (resistors and voltage sources)
- Automatically builds the conductance matrix G and source vector b
- Solves the matrix equation Gx = b using numpy
- Outputs all node voltages and branch currents

## How to run
1. Make sure Python and numpy are installed
2. Run solver.py
3. Enter your components when prompted
4. Get your results instantly

## Example
For a simple voltage divider (V1=5V, R1=R2=1000 ohms):
- V(node 1) = 5.0000 V
- V(node 2) = 2.5000 V
- Current through V1 = -0.002500 A

## Validated against ngspice
Results match industry-standard ngspice simulator output confirming correct MNA implementation.

## Built by
Sneha Sahjwani — Synergy Dynamics
