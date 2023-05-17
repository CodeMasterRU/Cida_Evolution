# %%
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../../../csvs/no_of_deaths_by_country_clean.csv", sep=',').dropna()
df = df[['Count_median', 'Country', 'WHO Region', 'Year']]
africa = df[df['WHO Region'] == 'Africa']
africa = africa[africa['Year'] == 2018]

grouped_df = africa.groupby(['Country'])['Count_median'].median().reset_index()
result = grouped_df.merge(df[['Country', 'WHO Region']].drop_duplicates(), on='Country')


result.to_csv("africa_2018.csv", index=False)

# %%
import plotly.graph_objects as go
africa = pd.read_csv("./africa_2018_map.csv", sep=',')

countries = africa['Country']
count_median = africa['Count_median']
print(count_median)


# Create a dictionary of country names and their corresponding median counts
data = dict(type='choropleth',
            locations=countries,
            locationmode='country names',
            z=count_median,
            colorscale='Viridis',
            colorbar=dict(title='Median Count')
           )

# Define the layout of the map
layout = dict(title='Median Count of Countries in Africa',
              geo=dict(scope='africa')
             )  

# Create the map
fig = go.Figure(data=[data], layout=layout)
fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

# %%



