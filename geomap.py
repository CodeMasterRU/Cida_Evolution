import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from mapclassify import *

# Load the shapefile for the world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Load the data from the Excel file
data = pd.read_excel('./deaths_all_continents.xlsx', index_col=0)

# Rename the columns
data.columns = ['1990-1999', '2000-2009', '2010-2019', 'Total']
print(data)
# Join the data to the shapefile
merged = world.merge(data, left_on='name', right_index=True, how='left')

# Set up the choropleth map
scheme = EqualInterval(merged['Total'], k=3)
fig, ax = plt.subplots(figsize=(12, 8))
merged.plot(column='Total', cmap='Reds', linewidth=0.8, edgecolor='0.8',
            scheme=scheme, legend=True, ax=ax)
ax.set_title('Total Cumulative Deaths by Region')

# Show the map
plt.show()
