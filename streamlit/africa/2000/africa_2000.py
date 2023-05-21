# %%
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../../csvs/no_of_deaths_by_country_clean.csv", sep=',').dropna()

df = df[['Count_median', 'Country', 'WHO Region', 'Year']]
africa = df[df['WHO Region'] == 'Africa']
africa = africa[africa['Year'] == 2000]
# africa = africa[['Count_median', 'Country','Year']]

grouped_df = africa.groupby(['Country'])['Count_median'].median().reset_index()
result = grouped_df.merge(df[['Country', 'WHO Region']].drop_duplicates(), on='Country')
result = result.sort_values('Count_median', ascending=False).reset_index(drop=True)

grouped_df.to_csv("africa_2000.csv", index=False)


# %%
# grouped_df = africa.groupby(['Country'])['Count_median'].median().reset_index()
# result = grouped_df.merge(df[['Country', 'WHO Region']].drop_duplicates(), on='Country')
# # result = result.sort_values('Count_median', ascending=False).reset_index(drop=True)
# print(result)

# # %%
# import plotly.graph_objects as go
# africa = pd.read_csv("./africa_2000_map.csv", sep=',')
# # Create a list of country names and their corresponding median counts
# # countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', "Côte d'Ivoire", 'Democratic Republic of the Congo', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Senegal', 'Sierra Leone', 'South Africa', 'South Sudan', 'Togo', 'Uganda', 'United Republic of Tanzania', 'Zambia', 'Zimbabwe']
# # count_median = [200.0, 10000.0, 2200.0, 7300.0, 4800.0, 5200.0, 100.0, 19000.0, 7800.0, 3500.0, 100.0, 24000.0, 34000.0, 1400.0, 620.0, 3800.0, 20000.0, 1600.0, 970.0, 17000.0, 4300.0, 1800.0, 56000.0, 7200.0, 2700.0, 1400.0, 29000.0, 6500.0, 500.0, 500.0, 54000.0, 3500.0, 1700.0, 72000.0, 5700.0, 1300.0, 2400.0, 100000.0, 9800.0, 5600.0, 56000.0, 48000.0, 26000.0, 54000.0]
# countries = africa['Country']
# count_median = africa['Count_median']
# # print(count_median)


# # Create a dictionary of country names and their corresponding median counts
# data = dict(type='choropleth',
#             locations=countries,
#             locationmode='country names',
#             z=count_median,
#             colorscale='Viridis',
#             colorbar=dict(title='Median Count')
#            )

# # Define the layout of the map
# layout = dict(title='Median Count of Countries in Africa',
#               geo=dict(scope='africa')
#              )  

# # Create the map
# fig = go.Figure(data=[data], layout=layout)
# fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()

