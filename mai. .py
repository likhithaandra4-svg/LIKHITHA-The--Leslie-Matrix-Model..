# This file is the "Entry Point". 
# You run THIS file to start the program.

import sys
import os

# --- PATH SETUP ---
# This block ensures Python can find your 'models' folder no matter where 
# you run this file from (Terminal, Run Button, etc.)
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Import the function from our specific model file
# Note: Since this file is inside 'src/', and 'models' is also inside 'src/',
# we can usually import directly. 
from models.leslie_matrix import run_leslie_simulation

if __name__ == "__main__":
    print("---------------------------------------")
    print("   LESLIE MATRIX BIOLOGICAL MODEL      ")
    print("---------------------------------------")

    # --- CONFIGURATION (Change these numbers to experiment!) ---
    
    # Age Groups: [Larvae, Juveniles, Adults]
    
    # 1. Fecundity (Birth Rates): 
    # Larvae(0) and Juveniles(0) don't reproduce. 
    # Adults produce 20 offspring per cycle.
    f_rates = [0, 0, 20] 
    
    # 2. Survival Probabilities:
    # 50% (0.5) of Larvae survive to become Juveniles.
    # 30% (0.3) of Juveniles survive to become Adults.
    p_rates = [0.5, 0.3] 
    
    # --- RUN SIMULATION ---
    print(f"\nParameters Set:")
    print(f"Birth Rates: {f_rates}")
    print(f"Survival Rates: {p_rates}")
    
    print("\nStarting Simulation...")
    run_leslie_simulation(fecundity=f_rates, survival=p_rates, years=15)
    print("\nSimulation Finished.")
