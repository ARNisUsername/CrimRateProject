import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pol = pd.read_csv('united_states_governors.csv')

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

theParties['Alaska'] = 'Republican'
theParties['North Dakota'] = 'Republican'
theParties['Montana'] = 'Republican'
theParties['New York'] = 'Democrat'
theParties['Washington'] = 'Democrat'


theParties = dict(sorted(theParties.items()))
valuesParties = list(theParties.values())


cities = pd.read_csv('citiesCrime.csv')
partiesForFile = ['empty', 'empty']

for state in cities['State'][2:]:
    if 'North Carolina' in state:
        state = 'North Carolina'
    if state != 'District of Columbia':
        partiesForFile.append(theParties[state])
    else:
        partiesForFile.append('Democrat')

cities['party'] = partiesForFile

cities = cities[2:]


cities['Property crime'] = pd.to_numeric(cities['Property crime'])
cities['Violent crime'] = pd.to_numeric(cities['Violent crime'])


colors = ['#CF2121', '#2155CF']
sns.set_palette(sns.color_palette(colors))



sns.scatterplot(x='Property crime', y='Violent crime', data=cities, hue='party')

fig, axes = plt.subplots(1,2)
sns.boxplot(x='party', y='Property crime', data=cities, ax=axes[0])
sns.boxplot(x='party', y='Violent crime', data=cities, ax=axes[1])
fig.tight_layout()

plt.show()
