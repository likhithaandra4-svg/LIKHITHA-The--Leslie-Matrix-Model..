import numpy as np
import matplotlib.pyplot as plt
import os

def run_leslie_simulation(fecundity, survival, years=10):
    """
    Runs a population simulation using the Leslie Matrix.
    
    Parameters:
    - fecundity: List of birth rates for each age group [f0, f1, f2]
    - survival: List of survival probabilities [p0, p1]
    - years: Number of years to simulate
    """
    
    # 1. SETUP: Input Validation
    # We need to ensure the lists match the matrix size expectations.
    # If we have 3 age groups, we need 3 fecundity rates and 2 survival rates.
    num_age_groups = len(fecundity)
    
    print(f"--- Running Simulation for {num_age_groups} Age Groups ---")

    # 2. CONSTRUCT MATRIX (Syllabus Section 05 - Matrices)
    # Initialize a matrix of zeros
    L = np.zeros((num_age_groups, num_age_groups))
    
    # Fill the first row with Fecundity (Birth Rates)
    # [f0, f1, f2]
    L[0, :] = fecundity
    
    # Fill the sub-diagonal with Survival Probabilities
    # [p0, 0, 0]
    # [0, p1, 0]
    for i in range(len(survival)):
        L[i+1, i] = survival[i]
        
    print("Leslie Matrix Constructed:")
    print(L)

    # 3. EIGENVALUE ANALYSIS (Syllabus Section 05 - Eigenvalues)
    # The dominant eigenvalue determines the long-term growth rate.
    eigenvalues, eigenvectors = np.linalg.eig(L)
    
    # Get the dominant eigenvalue (growth rate lambda)
    # We use abs() because eigenvalues can be complex numbers
    idx = np.argmax(np.abs(eigenvalues))
    growth_rate = np.real(eigenvalues[idx])
    
    print(f"\nDominant Eigenvalue (Lambda): {growth_rate:.4f}")
    if growth_rate > 1:
        print(" -> Population is INCREASING.")
    elif growth_rate < 1:
        print(" -> Population is DECREASING.")
    else:
        print(" -> Population is STABLE.")

    # 4. SIMULATION LOOP (Iterative Matrix Multiplication)
    # Initial population: 100 newborns, 0 juveniles, 0 adults
    population = np.zeros(num_age_groups)
    population[0] = 100 
    
    history = [population]
    
    for t in range(years):
        # Matrix Multiplication: N(t+1) = L * N(t)
        population = np.dot(L, population)
        history.append(population)
        
    history = np.array(history)

    # 5. PLOTTING
    plt.figure(figsize=(10, 6))
    
    labels = ['Larvae (Age 0)', 'Juveniles (Age 1)', 'Adults (Age 2)']
    
    # Plot each age group
    for i in range(num_age_groups):
        # Use specific labels if we have 3 groups, otherwise generic ones
        label_name = labels[i] if (i < len(labels) and num_age_groups == 3) else f'Age Group {i}'
        plt.plot(history[:, i], marker='o', label=label_name)
        
    plt.title(f'Leslie Matrix Simulation (Lambda={growth_rate:.2f})')
    plt.xlabel('Time Steps (Years)')
    plt.ylabel('Population Size')
    plt.legend()
    plt.grid(True)
    
    # Save the plot if the folder exists, otherwise show it
    # We look for the folder two levels up from this script (../../output/plots)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    output_path = os.path.join(project_root, 'output', 'plots', 'simulation.png')
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    try:
        plt.savefig(output_path)
        print(f"\nGraph saved to: {output_path}")
        # Also show it on screen
        plt.show()
    except Exception as e:
        print(f"\nCould not save image (Error: {e}). Showing plot instead.")
        plt.show()

    plt.close()
