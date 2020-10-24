import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

morta=pd.read_excel('D:/Documents/PythonPractice/MortalityRates/MortalityRateStates.xlsx')

morta.head()
morta=morta[['Location', 'FIPS','Category','Mortality Rate, 1980*','Mortality Rate, 2014*','% Change in Mortality Rate, 1980-2014']]
mortaStates=morta[morta['FIPS']<60]
mortaStates.head()
causes = pd.pivot_table(mortaStates, index = 'Category',columns='Location', values = '% Change in Mortality Rate, 1980-2014')
causes.head()
causes.plot(figsize = (20,10))
causes.plot(kind='bar', figsize=(20,15))
states = pd.pivot_table(mortaStates, index = 'Location', values = '% Change in Mortality Rate, 1980-2014')
states.plot(kind='bar', figsize=(20,15))
categories = pd.pivot_table(mortaStates, index = 'Category', values = '% Change in Mortality Rate, 1980-2014')

categories.plot(kind='bar', figsize=(20,15))
unitedStates=mortaStates[mortaStates['FIPS']==0]
unitedStates.plot(kind='bar', figsize=(20,15))

CausesinUS = pd.pivot_table(mortaStates, index = 'Location', values = '% Change in Mortality Rate, 1980-2014')

CausesinUS.plot(kind='bar', figsize=(20,10))
unitedStates2 = pd.pivot_table(unitedStates, index = 'Category', values = '% Change in Mortality Rate, 1980-2014')
unitedStates2.plot(kind='bar', figsize=(20,10))



