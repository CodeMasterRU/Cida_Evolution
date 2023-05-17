# %%
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../../../csvs/no_of_deaths_by_country_clean.csv", sep=',')
df = df[['Count_median', 'Country', 'WHO Region', 'Year']]
americas = df[df['WHO Region'] == 'Americas']
americas = americas[americas['Year'] == 2010]
grouped_df = americas.groupby(['Country'])['Count_median'].median().reset_index()
result = grouped_df.merge(df[['Country', 'WHO Region']].drop_duplicates(), on='Country')
result = result.sort_values('Count_median', ascending=False).reset_index(drop=True)
grouped_df.to_csv("americas_2010.csv", index=False)

