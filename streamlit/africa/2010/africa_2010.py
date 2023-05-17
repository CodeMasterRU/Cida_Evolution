# %%
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../../../csvs/no_of_deaths_by_country_clean.csv", sep=',').dropna()
df = df[['Count_median', 'Country', 'WHO Region', 'Year']]
africa = df[df['WHO Region'] == 'Africa']
africa = africa[africa['Year'] == 2010]

grouped_df = africa.groupby(['Country'])['Count_median'].median().reset_index()
result = grouped_df.merge(df[['Country', 'WHO Region']].drop_duplicates(), on='Country')


result.to_csv("africa_2010.csv", index=False)

