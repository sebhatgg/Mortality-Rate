import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

morta=pd.read_excel('D:/Documents/PythonPractice/MortalityRates/MortalityRateStates.xlsx')
morta.head()

morta=morta[['Location', 'FIPS','Category','Mortality Rate, 1980*','Mortality Rate, 2014*','% Change in Mortality Rate, 1980-2014']]
#print(morta.head(5))

mortaStates=morta[morta['FIPS']<60]
#print(mortaStates.head(5))

mortaStates.describe()

mortaStates.shape

mortaStates['Category'].value_counts()

plt.plot(mortaStates['% Change in Mortality Rate, 1980-2014'], mortaStates['Category'])

