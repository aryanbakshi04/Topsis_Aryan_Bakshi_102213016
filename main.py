# Aryan Bakshi
# 102213016
# 3CO1
import sys
import os   
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading '{input_file}': {e}")
        sys.exit(1)
        
    
    if df.shape[1] < 3:
        print("Error: Input file must contain at least three columns.")
        sys.exit(1)
        
  
    identifier_col = df.iloc[:, 0]  
    numeric_df = df.iloc[:, 1:]
    
    
    for col in numeric_df.columns:
        if not pd.api.types.is_numeric_dtype(numeric_df[col]):
            print(f"Error: Column '{col}' contains non-numeric values. All columns (except the first) must be numeric.")
            sys.exit(1)
    
    
    if len(weights) != numeric_df.shape[1]:
        print(f"Error: Number of weights ({len(weights)}) does not match the number of numeric columns ({numeric_df.shape[1]}).")
        sys.exit(1)
    if len(impacts) != numeric_df.shape[1]:
        print(f"Error: Number of impacts ({len(impacts)}) does not match the number of numeric columns ({numeric_df.shape[1]}).")
        sys.exit(1)
    
    
    for imp in impacts:
        if imp not in ['+', '-']:
            print("Error: Impacts must be either '+' or '-'.")
            sys.exit(1)
    
    
    data = numeric_df.values.astype(float)
    
    
    denom = np.sqrt((data**2).sum(axis=0))
    data_normalized = data / denom
    
  
    
    weights = np.array(weights)
    data_weighted = data_normalized * weights
    

    v_best = []
    v_worst = []
    for j, imp in enumerate(impacts):
        if imp == '+':
            v_best.append(np.max(data_weighted[:, j]))
            v_worst.append(np.min(data_weighted[:, j]))
        else:  
            v_best.append(np.min(data_weighted[:, j]))
            v_worst.append(np.max(data_weighted[:, j]))
    
    v_best = np.array(v_best)
    v_worst = np.array(v_worst)
    

    
    dist_best = np.sqrt(((data_weighted - v_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((data_weighted - v_worst)**2).sum(axis=1))
    
    
    performance_score = dist_worst / (dist_best + dist_worst)
    
  
    rank = performance_score.argsort()[::-1]  
    ranks = np.empty_like(rank)
    ranks[rank] = np.arange(1, len(performance_score) + 1)
    
    
    result_df = df.copy()
    result_df['Topsis Score'] = performance_score
    result_df['Rank'] = ranks
    
    
    try:
        result_df.to_csv(output_file, index=False)
        print(f"TOPSIS analysis completed successfully. Output written to '{output_file}'.")
    except Exception as e:
        print(f"Error writing result to '{output_file}': {e}")
        sys.exit(1)


def main():
    
    
    if len(sys.argv) != 5:
        print("Usage: python YourRollNumber.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)
    
    script, input_file, weights_str, impacts_str, output_file = sys.argv
    
    try:
        weights = [float(w.strip()) for w in weights_str.split(',')]
    except ValueError:
        print("Error: Weights must be numeric and separated by commas, e.g. '1,1,1,2'.")
        sys.exit(1)
    
    
    impacts = [imp.strip() for imp in impacts_str.split(',')]
    
    
    topsis(input_file, weights, impacts, output_file)


if __name__ == "__main__":
    main()
