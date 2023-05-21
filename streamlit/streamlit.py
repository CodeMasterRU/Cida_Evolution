import plotly.graph_objects as go
import seaborn as sns
# import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

st.title("Evolution de sida")

st.write("""
## Le nombre de morts dans le monde
""")

# scrap1
deaths_df = pd.read_csv("./deaths.csv")
g = sns.barplot(data=deaths_df, x="year", y="deaths_due_globally")
g.set_ylabel("Number of Deaths (millions)")
g.set_title("World")
st.pyplot(g.figure)    

st.write("""
## Le nombre de morts dans le monde triee par continent
""")

# scrap2

df = pd.read_csv("deaths_all_continents.csv", index_col="id")

df = df.replace('\s+', '', regex=True).astype(int)
# Plot bar chart
ax = df.plot(kind='bar', figsize=(10, 6))
ax.set_title("Total Cumulative Deaths by Region and Time Period")
ax.set_ylabel("Number of Deaths (millions)")
ax.legend(title="Time Period", fontsize='small')

# Show plot
# plt.show()
st.pyplot(ax.figure)


st.write("""
## Continents
""")
#--------2000---------
africa_2000 = pd.read_csv("./africa/2000/africa_2000_map.csv", sep=',')
americas_2000 = pd.read_csv("./americas/2000/americas_2000_map.csv", sep=',')
europe_2000 = pd.read_csv("./europe/2000/europe_2000_map.csv", sep=',')
asia_2000 = pd.read_csv("./asia/2000/asia_2000_map.csv", sep=',')
#--------2010---------
africa_2010 = pd.read_csv("./africa/2010/africa_2010_map.csv", sep=',')
americas_2010 = pd.read_csv("./americas/2010/americas_2010_map.csv", sep=',')
europe_2010 = pd.read_csv("./europe/2010/europe_2010_map.csv", sep=',')
asia_2010 = pd.read_csv("./asia/2010/asia_2010_map.csv", sep=',')
#--------2018---------
africa_2018 = pd.read_csv("./africa/2018/africa_2018_map.csv", sep=',')
americas_2018 = pd.read_csv("./americas/2018/americas_2018_map.csv", sep=',')
europe_2018 = pd.read_csv("./europe/2018/europe_2018_map.csv", sep=',')
asia_2018 = pd.read_csv("./asia/2018/asia_2018_map.csv", sep=',')


#--------world---------
world_2000 = pd.read_csv("./world_malades/2000/world_2000_living_count_map.csv", sep=',')
world_2010 = pd.read_csv("./world_malades/2010/world_2010_living_count_map.csv", sep=',')
world_2018 = pd.read_csv("./world_malades/2018/world_2018_living_count_map.csv", sep=',')


def select_data(choix_continent, choix_anne):
    # AFRICA
    if choix_continent == 'africa':

        if choix_anne == 2000:
            countries = africa_2000['Country']
            count_median = africa_2000['Count_median']

        elif choix_anne == 2010:
            countries = africa_2010['Country']
            count_median = africa_2010['Count_median']

        elif choix_anne == 2018:
            countries = africa_2018['Country']
            count_median = africa_2018['Count_median']

    # AMERICA
    elif choix_continent == 'north america' or choix_continent == 'south america':

        if choix_anne == 2000:
            countries = americas_2000['Country']
            count_median = americas_2000['Count_median']

        elif choix_anne == 2010:
            countries = americas_2010['Country']
            count_median = americas_2010['Count_median']
        
        elif choix_anne == 2018:
            countries = americas_2018['Country']
            count_median = americas_2018['Count_median']
            
    # EUROPE
    elif choix_continent == 'europe':

        if choix_anne == 2000:
            countries = europe_2000['Country']
            count_median = europe_2000['Count_median']

        elif choix_anne == 2010:
            countries = europe_2010['Country']
            count_median = europe_2010['Count_median']
        
        elif choix_anne == 2018:
            countries = europe_2018['Country']
            count_median = europe_2018['Count_median']
    # ASIA   
    else:
                
        if choix_anne == 2000:
            countries = asia_2000['Country']
            count_median = asia_2000['Count_median']

        elif choix_anne == 2010:
            countries = asia_2010['Country']
            count_median = asia_2010['Count_median']
        
        elif choix_anne == 2018:
            countries = asia_2018['Country']
            count_median = asia_2018['Count_median']

    return countries, count_median
           
# countries = africa_2000['Country']
# count_median = africa_2000['Count_median']
# print(count_median)


# Create a dictionary of country names and their corresponding median counts
def generate_data(countries, count_median):
    data = dict(type='choropleth',
        locations=countries,
        locationmode='country names',
        z=count_median,
        colorscale='Viridis',
        colorbar=dict(title='Median Count')
        )
    return data




# Create the map
def choosezone_deaths(continent):
    # Define the layout of the map
    layout = dict(title='Median Count of Countries in Africa',
            geo=dict(scope=continent)
        )  
    country = select_data(choix_de_continent, choix_anne)[0]
    count_med = select_data(choix_de_continent, choix_anne)[1]
    fig = go.Figure(data=[generate_data(country,count_med)], layout=layout)
    fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0})
    # st.plotly_chart(fig)
    return fig

choix_de_continent = st.selectbox(
    'Des informations sur le continent que vous aimeriez voir?',
    ('africa', 'north america', 'south america',  'europe', 'asia'))
choix_anne = st.selectbox(
    'Des informations sur quelle anee vous aimeriez voir?',
    (2000, 2010, 2018))

# st.write('You selected:', choix_de_continent)
select_data(choix_de_continent, choix_anne)

def get_continent(choix_de_continent, choix_anne):
    st.write(choix_de_continent, choix_anne)
    st.plotly_chart(choosezone_deaths(choix_de_continent))
    

get_continent(choix_de_continent, choix_anne)
    # elif choix_de_continent == 'Amerique':
    #     st.write('Amerique')

    # elif choix_de_continent == 'Europe':
    #     st.write('Europe')

    # else:
    #     st.write('Asie')

    # return fig

st.write("""
## World Malades
""")

def select_data_world(choix_anne_world):
    if choix_anne_world == 2000:
        countries = world_2000['Country']
        count_median = world_2000['Count_median']

    elif choix_anne_world == 2010:
        countries = world_2010['Country']
        count_median = world_2010['Count_median']
    else:
        countries = world_2018['Country']
        count_median = world_2018['Count_median'] 
    return countries, count_median

# Create the map 
def chooseannee_malades(choix_anne_world):
    # Define the layout of the map
    layout = dict(title='Median Count of Countries in Word',
            geo=dict(scope='world')
        )  
    country = select_data_world(choix_anne_world)[0]
    count_med = select_data_world(choix_anne_world)[1]
    fig = go.Figure(data=[generate_data(country,count_med)], layout=layout)
    fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0})
    # st.plotly_chart(fig)
    return fig


choix_anne_world = st.selectbox(
    'Des informations dyu monde sur quelle anee vous aimeriez voir?',
    (2000, 2010, 2018))

def get_annee_malades(choix_anne_world):
    st.write(choix_anne_world)
    st.plotly_chart(chooseannee_malades(choix_anne_world))

get_annee_malades(choix_anne_world)

st.write("""
## Koeff de malades
""")

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

st.pyplot(ax.figure)

