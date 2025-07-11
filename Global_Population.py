import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('world_population.csv')
df=pd.DataFrame(data)

df.drop(['Capital','CCA3','Rank'],axis=1,inplace=True)


##Top and Bottom Countries by Population (2022)
top_countries_2022=df.sort_values(by='2022 Population',ascending=False).head(10)
top_countries_2022_name=top_countries_2022[['Country/Territory','2022 Population']]


bottom_countries_2022=df.sort_values(by='2022 Population').head(10)
bottom_countries_2022_name=bottom_countries_2022[['Country/Territory','2022 Population']]

plt, ax = plt.subplots(2,1, figsize=(10,9))

colors = [
    '#08306b',  
    '#08519c',
    '#2171b5',
    '#4292c6',
    '#6baed6',
    '#9ecae1',
    '#c6dbef',
    '#deebf7',
    '#f0f8ff',
    '#f7f8ff'   
]
sns.barplot(x=top_countries_2022_name['2022 Population'],y=top_countries_2022_name['Country/Territory'],palette=colors, ax=ax[0])
ax[0].set_title('Top 10 Countries (2022) with highest population',color='darkred',size=12,fontweight='bold')
ax[0].set_ylabel(None)
colors = [
    '#f7f8ff',
    '#f0f8ff',
    '#deebf7',
    '#c6dbef',
    '#9ecae1',
    '#6baed6',
    '#4292c6',
    '#2171b5',
    '#08519c',
    '#08306b'
]

sns.barplot(x=bottom_countries_2022_name['2022 Population'],y=bottom_countries_2022_name['Country/Territory'],palette=colors, ax=ax[1])
ax[1].set_title('Top 10 Countries (2022) with lowest population',color='darkred',size=12,fontweight='bold')
ax[1].set_ylabel(None)
sns.despine()
plt.tight_layout()
plt.savefig('01 Top 10 population countries.png',dpi=400,bbox_inches='tight')



#3 Growth over the decades (1970–2022)

growth=df.groupby('Continent')[['1970 Population','1980 Population','1990 Population','2000 Population','2010 Population','2015 Population','2020 Population','2022 Population']].sum()
growth=growth.T
import matplotlib.pyplot as plt
sns.set_style('darkgrid')
dev,ax= plt.subplots(figsize=(10,8))
sns.lineplot(growth, alpha=0.5)

plt.xticks(rotation=60)
plt.title('GROWTH OVER DECADES (1970-2022) IN EACH CONTINENT ',size=18,color='darkblue',fontweight='bold')
plt.ylabel('Population in Billions', size=13, color='darkred',fontweight='bold')
plt.xlabel('Growth over Decades (1970-2022)',size=13, color='darkred',fontweight='bold')
plt.tight_layout()
sns.despine()
plt.savefig('02 growthhh.png',dpi=400,bbox_inches='tight')




# Population Growth Analysis
# Compare population from 1970 to 2022
df['1970 Population'].astype(int)
df['2022 Population'].astype(int)
df['comparition_of_population']=(df['2022 Population']-df['1970 Population'])
#it was only a part of analysis


# Identify fastest-growing and declining countries
fastest_growing_population=df[['Country/Territory','comparition_of_population']].sort_values(by='comparition_of_population',ascending=False).head(10)
declining_population=df[['Country/Territory','comparition_of_population']].sort_values(by='comparition_of_population',ascending=False).tail(10)

import matplotlib.pyplot as plt
colors = [
    '#00441b',  
    '#006d2c',
    '#238b45',
    '#41ab5d',
    '#74c476',
    '#a1d99b',
    '#c7e9c0',
    '#e5f5e0',
    '#f7fcf5',
    '#fbfdf9'   
]

plt, ax=plt.subplots(2,1, figsize=(10,8))
plt.suptitle('Fastest Growing and Decreasing top Countries ',size=18,color='darkgreen',style='oblique',fontweight='bold')
sns.barplot(x=fastest_growing_population['comparition_of_population'],y=fastest_growing_population['Country/Territory'], orient='h',ax=ax[0],palette=colors)
ax[0].set_ylabel(None)
ax[0].set_xlabel('Fastest Growing countries in population (100 M)',size=8,fontweight='bold')
ax[0].set_title('Top 10 Fastest Growing Countries',size=14,color='#238b45',style='oblique',fontweight='bold')
colors = [
    '#fbfdf9',  
    '#f7fcf5',
    '#e5f5e0',
    '#c7e9c0',
    '#a1d99b',
    '#74c476',
    '#41ab5d',
    '#238b45',
    '#006d2c',
    '#00441b'  
]

sns.barplot(x=declining_population['comparition_of_population'],y=declining_population['Country/Territory'], orient='h',ax=ax[1],palette=colors)
ax[1].set_title('Top 10 Fastest Decreasing Countries',size=14,color='#238b45',style='oblique',fontweight='bold')
ax[1].set_ylabel(None)
ax[1].set_xlabel('Decreasing population countries (1 M)',size=8,fontweight='bold')
plt.tight_layout()
sns.despine()
plt.savefig('03 top fastest growing and decreasing countries.png',dpi=400,bbox_inches='tight')
plt.show()




# Continent-Level Analysis
# Total population per continent (2022)
continent_population_2022=df.groupby('Continent')['2022 Population'].sum().sort_values(ascending=False)
import matplotlib.pyplot as plt
fig, ax= plt.subplots(1,1,figsize=(6,6))
colors = [
    '#66c2a5',  # Soft teal
    '#8da0cb',  # Muted lavender blue
    '#a6d854',  # Light olive green
    '#ffd92f',  # Warm yellow
    '#fc8d62',  # Soft orange
    '#e78ac3'   # Soft pinkish-purple
]


continent_population_2022.plot(kind='pie',autopct='%1.1f%%',wedgeprops={'edgecolor': 'white'},startangle=90,colors=colors,ax=ax,labeldistance=1.1)
ax.set_title('Population on each Continent (%)', fontsize=14, fontweight='bold')
ax.set_ylabel('')
sns.despine()
plt.tight_layout()
plt.savefig('06 Continent population.png',dpi=400,bbox_inches='tight')

# Plot country-wise or continent-wise growth trends
continent_population=df.groupby('Continent')[['1970 Population','2022 Population']].sum().sort_values(by=['1970 Population','2022 Population'],ascending=False).sort_values(by='2022 Population',ascending=False)
import matplotlib.pyplot as plt
continent_population.plot(kind='bar',color=['#20B2AA',"#005A5A"])

plt.xticks(rotation=20,size=8)
plt.xlabel('Continents',fontweight='bold',size=10,color='darkblue')
plt.ylabel('Total Population (in Billions)',fontweight='bold',size=10,color='darkblue')
plt.grid('white')
plt.tight_layout()
plt.savefig('04 Continent bar chart.png',dpi=400,bbox_inches='tight')



# Continent with the highest average growth rate
continent_population['Growth']=((continent_population['2022 Population']-continent_population['1970 Population'])/continent_population['1970 Population'])*100
# print(continent_population['Growth'].idxmax(),' has the highest avg growth rate continent with ',continent_population['Growth'].max(),'%')
# this line prints the continent with the highest growth rate and the growth rate (no need but good for code understanding)


#  Population Density Insights
# Top 10 most densely populated countries
density_populated_10=df[['Country/Territory','Density (per km²)']].sort_values(by='Density (per km²)',ascending=False).head(10)

import matplotlib.pyplot as plt
sns.set_style('dark')
plt, ax= plt.subplots(2,1,figsize=(14,10))
plt.suptitle('Top Highest and Lowest Density Countries',fontweight='bold',size=17,color='darkred')
colors = [
    '#7f0000',  
    '#b30000',
    '#d7301f',
    '#ef6548',
    '#fc8d59',
    '#fdbb84',
    '#fdd49e',
    '#fee8c8',
    '#fff5eb',
    '#ffffff'  
]

ax[0].bar(density_populated_10['Country/Territory'],density_populated_10['Density (per km²)'],color=colors)
ax[0].set_title('Top 10 Most Densely Populated Countries',fontweight='bold',size=15,color='#b30000')
ax[0].set_xlabel('Country',fontweight='bold',size=13,color='darkred')
ax[0].set_ylabel('Density',fontweight='bold',size=13,color='darkred')
ax[0].tick_params(axis='x', labelrotation=45)  


# Countries with large areas but low populations (low density) (e.g., Australia, Canada)
Low_density_populated=df[['Country/Territory','2022 Population', 'Area (km²)', 'Density (per km²)']].sort_values(by='Density (per km²)').head(5)

colors = [
    '#ffe5e5',  
    '#fca5a5',  
    '#f87171',  
    '#ef4444',  
    '#7f1d1d'   
]

ax[1].bar(Low_density_populated['Country/Territory'],Low_density_populated['Density (per km²)'], color=colors)
ax[1].set_title('Countries with Low Population Density',fontweight='bold',size=15,color='#b30000')
ax[1].set_xlabel('Country',fontweight='bold',size=13,color='darkred')
ax[1].set_ylabel('Density',fontweight='bold',size=13,color='darkred')

sns.despine()
plt.tight_layout()
plt.savefig('05 density populated.png',dpi=400)



