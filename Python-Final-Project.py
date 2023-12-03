# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 17:57:01 2023

@author: emein
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Total Legal Immigration to the US by Country of Birth 1999-2021
legalpr = pd.read_csv("Legal Permanent Residents by Country of Birth.csv")
# Drop NA values
legalpr1 = legalpr.dropna()
legalpr1_all = legalpr1.iloc[:1]
legalpr1_all = legalpr1_all.melt()
legalpr1_all.rename(columns = {'variable':'Year', 'value':'Total'}, inplace = True)
legalpr1_all.drop(index=legalpr1_all.index[:1], axis=0, inplace=True)
x = legalpr1_all['Year']
y = legalpr1_all['Total']
plt.plot(x, y, color='blue', linewidth=1.0)
plt.title("Number of Legal Immigrants to the US by Year")
plt.show()


###################################################################################
# Naturalized US Citizens by Country of Birth 1999-2021
natcitizen = pd.read_csv("Naturalized Citizen by Country of Birth.csv")
# Drop NA values
natcitizen1 = natcitizen.dropna()
natcitizen1_all = natcitizen1.iloc[:1]
natcitizen1_all = natcitizen1_all.melt()
natcitizen1_all.rename(columns = {'variable':'Year', 'value':'Total'}, inplace = True)
natcitizen1_all.drop(index=natcitizen1_all.index[:1], axis=0, inplace=True)
x = natcitizen1_all['Year']
y = natcitizen1_all['Total']
plt.plot(x, y, color='green', linewidth=1.0)
plt.title("Number of Naturalized Citizens by Year")
plt.show()


###################################################################################
# Number of Immigrants and Immigrants as a percent of total US population 1850-2021
perc_pop = pd.read_csv("Immigrants_Percent_US_Population.csv")
# Line Graph
x = perc_pop['Year']
y1 = perc_pop['Number of Immigrants']
y2 = perc_pop['Immigrants as a Percentage of the U.S. Population (%)']

#plt.figure(num = 3, figsize=(8, 5))
plt.plot(x, y1, 
         color='blue', 
         linewidth=1.0)
plt.title("Number of Immigrants in the US by Year")
#plt.yticks(np.arange(min(y1), max(y1)+1, 5000000))
plt.show()

plt.plot(x, y2, 
         color='red',   
         linewidth=1.0 
        )
plt.title("Percent of Immigrants in US Population")
plt.show()


################################################################################
# Number of Removals and Returns
removals = pd.read_csv("Aliens Removed or Returned Fiscal Years 1892 to 2019.csv")
# Subset to years 2001-2019
removals1 = removals.loc[removals['Year'] >= 2001]
# Line graph
x = removals1['Year']
y1 = removals1['Removals']
y2 = removals1['Returns']

#plt.figure(num = 3, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, 
         color='red',   
         linewidth=1.0 
        )
plt.title("Removals and Returns by Year")
plt.legend()
plt.show()

# Southwest Border Encounters
border = pd.read_csv("Southwest Land Border Encounters.csv")