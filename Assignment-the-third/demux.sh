#!/bin/bash
#SBATCH --partition=bgmp        ### Partition 
#SBATCH --job-name=demux2     ### Job Name
#SBATCH --output=demux2_%j.out      ### File in which to store job output
#SBATCH --time=0-16:00:00       ### Wall clock time limit in Days-HH:MM:SS
#SBATCH --nodes=1               ### Number of nodes needed for the job
#SBATCH --ntasks-per-node=1    ### Number of tasks to be launched per Node
#SBATCH --account=bgmp          ### Account used for job submission
#SBATCH --nodelist=n226         ### Run on node 226

/usr/bin/time -v ./demux.py -r1 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz -i1 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz -i2 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz -r2 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz -ic 30 -sc 25