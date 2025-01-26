# TOPSIS Implementation for Decision Analysis

This project implements the **Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS)** method for multi-criteria decision-making. The program processes an input dataset, calculates the TOPSIS score, and ranks the alternatives accordingly.

---

## How It Works

1. **Input File**:  
   The program takes a `.csv` file with data in the following format:
   - The first column contains object/variable names (e.g., M1, M2, M3, etc.).
   - All other columns (from the second onward) must contain **numeric values**.

2. **Output File**:  
   The output file contains all the columns of the input file along with two additional columns:
   - **Topsis Score**: The calculated score for each object.
   - **Rank**: The ranking of each object based on the TOPSIS score.

---

## Requirements

- Python 3.x
- Required Libraries:
  - `pandas`
  - `numpy`

---

## Instructions

1. **Input File**:  
   Rename the input file to follow the format `<RollNumber>-data.csv`. Example: `101556-data.csv`.

2. **Command to Run the Program**:
   ```bash
   python <program.py> <InputFileName> <Weights> <Impacts> <OutputFileName>
