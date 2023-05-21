# %%
import pandas as pd
import matplotlib.pyplot as plt

df_habitant = pd.read_csv("./../csvs/world_population.csv")

df_habitant = df_habitant[['Country/Territory', '2000 Population']]

countries = ["Algeria", "Cameroon", "Ethiopia", "Kenya", "Nigeria", "Belarus", "France", "Finland", "Germany", "Spain", "Argentina", "Brazil", "Haiti", "Mexico", "Peru", "Morocco", "Cambodia", "Malaysia", "Viet Nam"]

filtered_countries_habitant = df_habitant[df_habitant['Country/Territory'].isin(countries)]

df_sida = pd.read_csv("./../csvs/no_of_people_living_with_hiv_by_country_clean.csv", sep=',')

df_sida = df_sida[['Country','Count_median','Year']]

df_sida = df_sida[df_sida["Year"]==2000]
df_sida = df_sida[['Country','Count_median']]

countries = ["Algeria", "Cameroon", "Ethiopia", "Kenya", "Nigeria", "Belarus", "France", "Finland", "Germany", "Spain", "Argentina", "Brazil", "Haiti", "Mexico", "Peru", "Morocco", "Cambodia", "Malaysia", "Viet Nam"]

filtered_countries_sida = df_sida[df_sida['Country'].isin(countries)]

df_merged = pd.merge(filtered_countries_habitant, filtered_countries_sida, left_on='Country/Territory', right_on='Country')

df_merged = df_merged.drop(columns=['Country'])

df_merged = df_merged.rename(columns={'Country/Territory': 'Country' ,'2000 Population': 'Population_2000', 'Count_median': 'Median_Count_2000'})

population = df_merged[['Population_2000']].astype(float)
sida = df_merged[['Median_Count_2000']].astype(float)

koeff = sida.values/population.values
df_merged.insert(3, "Koeff %", koeff * 100, True)
ax = df_merged.plot(kind='bar', x = 'Country', y='Koeff %', figsize=(10, 3))
ax.set_title("Deaths median in Europe in %")

plt.show()
