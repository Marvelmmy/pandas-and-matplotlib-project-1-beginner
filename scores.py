#importing the package 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

#inserting the data
score = pd.read_csv('data.csv')
print(score.head())