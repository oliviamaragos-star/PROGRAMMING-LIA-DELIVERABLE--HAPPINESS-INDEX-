# ================================================================
# File: LIA CODE-HAPPINESS INDEX.py
# Author: OLIVIA MARAGOS and VICTORIA MILIOTO 
# Course: Python Programming / Lab 05
# Date: October 2025
#
# Description:
#  This program contains all exercises for the Lia Deliverable .
#  It will be used to analyze the dataset of the WHI using GitHub.

# ================================================================
# Loading datset with Numpy
# ---------------------------------------------------------------
# numeric columns: Ladder, GDP, Support, LifeExp, Freedom, Generosity, Corruption
cols = (2, 6, 7, 8, 9, 10, 11)
import numpy as np
data = np.loadtxt("world-happiness-report-2021.csv", delimiter=",", skiprows=1, usecols = cols )
# each column seperately
ladder, gdp, support, life, freedom, generosity, corruption = data.T
print("Ladder sample:", ladder[:5])




