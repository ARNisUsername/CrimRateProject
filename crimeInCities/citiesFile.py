import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('estimated_crimes.csv')

#Get the data of violent and property crime in each state as of 2019
year2019 = df[df['year'] == 2019][['state_name', 'violent_crime', 'property_crime']][:-1]

#Get the party affiliation of every US state 
pol = pd.read_csv('united_states_governors.csv')

#Set of code to take the pol csv file and properly extract each state with their political party
theParty = pol[pol['year'] >= 2014][['state','party']]

eachState = theParty['state'].unique()

theParties = {}
for state in eachState:
    party = str(theParty[theParty['state']==state]['party'])
    if 'Guam' not in state and 'Virgin Islands' not in state:
        if 'Democrat' in ''.join(party):
            theParties[state] = 'Democrat'
        elif 'Republican' in ''.join(party):
            theParties[state] = 'Republican'

#Additional states not included in the csv file
theParties['Alaska'] = 'Republican'
theParties['North Dakota'] = 'Republican'
theParties['Montana'] = 'Republican'
theParties['New York'] = 'Democrat'
theParties['Washington'] = 'Democrat'

#Add the list of political parties of every state to the original csv file
theParties = dict(sorted(theParties.items()))
valuesParties = list(theParties.values())

#Get cities csv file
cities = pd.read_csv('citiesCrime.csv')
partiesForFile = ['empty', 'empty']

#Get a list of the parties for the state in the csv file(add some if statements for debugging purposes)
for state in cities['State'][2:]:
    if 'North Carolina' in state:
        state = 'North Carolina'
    if state != 'District of Columbia':
        partiesForFile.append(theParties[state])
    else:
        partiesForFile.append('Democrat')

#Insert list as a party column in csv file and eliminate first two empty rows
cities['party'] = partiesForFile
cities = cities[2:]

#Change the property and violent crime to numeric so seaborn can intepret it
cities['Property crime'] = pd.to_numeric(cities['Property crime'])
cities['Violent crime'] = pd.to_numeric(cities['Violent crime'])

#Set colors and make the graphs
colors = ['#CF2121', '#2155CF']
sns.set_palette(sns.color_palette(colors))

sns.scatterplot(x='Property crime', y='Violent crime', data=cities, hue='party')

fig, axes = plt.subplots(1,2)
sns.boxplot(x='party', y='Property crime', data=cities, ax=axes[0])
sns.boxplot(x='party', y='Violent crime', data=cities, ax=axes[1])
fig.tight_layout()

plt.show()
