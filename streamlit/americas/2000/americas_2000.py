# %%
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../../../csvs/no_of_deaths_by_country_clean.csv", sep=',')
df = df[['Count_median', 'Country', 'WHO Region', 'Year']]
americas = df[df['WHO Region'] == 'Americas']
americas = americas[americas['Year'] == 2000]

grouped_df = americas.groupby(['Country'])['Count_median'].median().reset_index()
result = grouped_df.merge(df[['Country', 'WHO Region']].drop_duplicates(), on='Country')
result = result.sort_values('Count_median', ascending=False).reset_index(drop=True)
grouped_df.to_csv("americas_2000.csv", index=False)
# print(result)


# # %%
# import plotly.graph_objects as go


# americas = pd.read_csv("./americas_2000_map.csv", sep=',')
# countries = americas['Country']
# count_median = americas['Count_median']

# # Create a dictionary of country names and their corresponding median counts
# data = dict(type='choropleth',
#             locations=countries,
#             locationmode='country names',
#             z=count_median,
#             colorscale='Viridis',
#             colorbar=dict(title='Median Count')
#            )

# # Define the layout of the map
# layout = dict(title='Median Count of Countries in North america',
#               geo=dict(scope='north america')
#              )


# # Create the map
# fig = go.Figure(data=[data], layout=layout)
# fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()

# layout = dict(title='Median Count of Countries in South america',
#               geo=dict(scope='south america')
#              )

# # Create the map
# fig = go.Figure(data=[data], layout=layout)
# fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0})

# fig.show()


# # %%
# print(americas)

# %%



