#!/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task 8
#SBATCH --nodelist=n226

python3 part1.py