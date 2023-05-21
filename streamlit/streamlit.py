import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
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
## Le nombre de morts dans le monde trié par continent
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

# Etude de cas (France/ Afrique du Sud)
st.title('Etude de cas: comparaison entre deux pays')


def plot_gdp():
    years_france = [1999, 2000, 2002, 2003, 2004, 2005, 2006,
                    2007, 2008, 2009, 2010, 2011, 2012, 2013, 2015, 2016, 2017]
    gdp_france = [1373, 1448, 1540, 1661, 1737, 1794, 1891, 2075,
                  2128, 2094, 2145, 2246, 2291, 2276, 2647, 2699, 2856]
    years_sa = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006,
                2007, 2008, 2009, 2010, 2011, 2012, 2013, 2015, 2016, 2017]
    gdp_sa = [296.1, 369, 412, 432, 456.7, 491.4, 540.8, 587.5,
              467.8, 491, 504.6, 524, 562.2, 592, 595.7, 723.5, 739.1, 767.2]

    plt.figure(figsize=(10, 6))
    plt.plot(years_france, gdp_france, marker='o',
             linestyle='-', color='blue', label='France')
    plt.plot(years_sa, gdp_sa, marker='o', linestyle='-',
             color='green', label='Afrique du Sud')
    plt.title('PIB en France et en Afrique du Sud')
    plt.xlabel('Année')
    plt.ylabel('PIB (en milliards)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()

    return plt


st.set_option('deprecation.showPyplotGlobalUse', False)

# Create Streamlit app
# st.title('Graphique du PIB en France et en Afrique du Sud')
plt_gdp = plot_gdp()
st.pyplot(plt_gdp)

# Data for total deaths from HIV/AIDS in France
years_france = [1999, 2000, 2001, 2003,
                2007, 2009, 2012, 2015, 2018, 2019, 2020]
deaths_france = [2000, 0, 800, 1000, 1600, 1700, 0, 0, 500, 500, 500]

# Data for total deaths from HIV/AIDS in South Africa
years_sa = [1999, 2000, 2001, 2003, 2007, 2009, 2012, 2015, 2018, 2019, 2020]
deaths_sa = [250000, 300000, 0, 360000, 370000,
             350000, 0, 182400, 110000, 71000, 72000]

# Data for the total population in France
years_population_france = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007,
                           2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
population_france = [61255360, 61605930, 61963620, 62311900, 62678430, 63059740, 63456870, 63852860, 64220250, 64579930,
                     64940830, 65296100, 65630690, 65951610, 66259010, 66553770, 66836150, 67106160, 67364360, 67611480, 67848160]

# Data for the total population in South Africa
years_population_sa = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
                       2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
population_sa = [44913300, 45483340, 46104940, 46770280, 47438930, 48104400, 48737070, 49371900, 50024790, 50680860,
                 51122960, 51453820, 51913820, 52425160, 53006860, 53675560, 54300700, 54841550, 55380210, 55918440, 56463620]

# Calculate the proportion of deaths per population for each country
proportion_deaths_france = [d / p * 100 for d,
                            p in zip(deaths_france, population_france)]
proportion_deaths_sa = [d / p * 100 for d, p in zip(deaths_sa, population_sa)]

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(years_france, proportion_deaths_france, marker='o',
         linestyle='-', color='blue', label='France')
plt.plot(years_sa, proportion_deaths_sa, marker='o',
         linestyle='-', color='green', label='Afrique du Sud')
plt.title('Total Deaths from HIV/AIDS (as Proportion of Total Population)')
plt.xlabel('Year')
plt.ylabel('Proportion of Deaths (%)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Display the graph using Streamlit
st.pyplot(plt)

st.write("""
## Continents
""")
# --------2000---------
africa_2000 = pd.read_csv("./africa/2000/africa_2000_map.csv", sep=',')
americas_2000 = pd.read_csv("./americas/2000/americas_2000_map.csv", sep=',')
europe_2000 = pd.read_csv("./europe/2000/europe_2000_map.csv", sep=',')
asia_2000 = pd.read_csv("./asia/2000/asia_2000_map.csv", sep=',')
# --------2010---------
africa_2010 = pd.read_csv("./africa/2010/africa_2010_map.csv", sep=',')
americas_2010 = pd.read_csv("./americas/2010/americas_2010_map.csv", sep=',')
europe_2010 = pd.read_csv("./europe/2010/europe_2010_map.csv", sep=',')
asia_2010 = pd.read_csv("./asia/2010/asia_2010_map.csv", sep=',')
# --------2018---------
africa_2018 = pd.read_csv("./africa/2018/africa_2018_map.csv", sep=',')
americas_2018 = pd.read_csv("./americas/2018/americas_2018_map.csv", sep=',')
europe_2018 = pd.read_csv("./europe/2018/europe_2018_map.csv", sep=',')
asia_2018 = pd.read_csv("./asia/2018/asia_2018_map.csv", sep=',')


# --------world---------
world_2000 = pd.read_csv(
    "./world_malades/2000/world_2000_living_count_map.csv", sep=',')
world_2010 = pd.read_csv(
    "./world_malades/2010/world_2010_living_count_map.csv", sep=',')
world_2018 = pd.read_csv(
    "./world_malades/2018/world_2018_living_count_map.csv", sep=',')


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
    colorscale = [[0.0, 'rgb(0, 255, 0)'],      # Lowest value color (e.g., green)
                  [0.25, 'rgb(128, 255, 0)'],   # Intermediate value color
                  # Intermediate value color (e.g., yellow)
                  [0.5, 'rgb(255, 255, 0)'],
                  [0.75, 'rgb(255, 128, 0)'],   # Intermediate value color
                  [1.0, 'rgb(255, 0, 0)']]      # Highest value color (e.g., red)
    data = dict(type='choropleth',
                locations=countries,
                locationmode='country names',
                z=count_median,
                colorscale=colorscale,
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
    fig = go.Figure(data=[generate_data(country, count_med)], layout=layout)
    fig.update_layout(height=500, margin={"r": 0, "t": 0, "l": 0, "b": 0})
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
    fig = go.Figure(data=[generate_data(country, count_med)], layout=layout)
    fig.update_layout(height=500, margin={"r": 0, "t": 0, "l": 0, "b": 0})
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

countries = ["Algeria", "Cameroon", "Ethiopia", "Kenya", "Nigeria", "Belarus", "France", "Finland", "Germany",
             "Spain", "Argentina", "Brazil", "Haiti", "Mexico", "Peru", "Morocco", "Cambodia", "Malaysia", "Viet Nam"]

filtered_countries_habitant = df_habitant[df_habitant['Country/Territory'].isin(
    countries)]

df_sida = pd.read_csv(
    "./../csvs/no_of_people_living_with_hiv_by_country_clean.csv", sep=',')

df_sida = df_sida[['Country', 'Count_median', 'Year']]

df_sida = df_sida[df_sida["Year"] == 2000]
df_sida = df_sida[['Country', 'Count_median']]

countries = ["Algeria", "Cameroon", "Ethiopia", "Kenya", "Nigeria", "Belarus", "France", "Finland", "Germany",
             "Spain", "Argentina", "Brazil", "Haiti", "Mexico", "Peru", "Morocco", "Cambodia", "Malaysia", "Viet Nam"]

filtered_countries_sida = df_sida[df_sida['Country'].isin(countries)]

df_merged = pd.merge(filtered_countries_habitant, filtered_countries_sida,
                     left_on='Country/Territory', right_on='Country')

df_merged = df_merged.drop(columns=['Country'])

df_merged = df_merged.rename(columns={'Country/Territory': 'Country',
                             '2000 Population': 'Population_2000', 'Count_median': 'Median_Count_2000'})

population = df_merged[['Population_2000']].astype(float)
sida = df_merged[['Median_Count_2000']].astype(float)

koeff = sida.values/population.values
df_merged.insert(3, "Koeff %", koeff * 100, True)
ax = df_merged.plot(kind='bar', x='Country', y='Koeff %', figsize=(10, 3))
ax.set_title("Deaths median in Europe in %")

st.pyplot(ax.figure)

# Define the data
years = np.array([1999, 2001, 2003, 2007, 2009, 2013,
                 2018, 2019, 2020]).reshape(-1, 1)
deaths = np.array([2000, 800, 1000, 1600, 1700, 1500, 500, 500, 500])

# Create and train the linear regression model
model = LinearRegression()
model.fit(years, deaths)

# Create Streamlit app
st.title('HIV/AIDS Deaths Prediction')
st.write('Enter a year to predict the number of deaths in France:')

# Input year from the user
year_input = st.number_input(
    'Year:', min_value=1999, max_value=2100, step=1, key='lin')

# Make prediction for the input year
prediction = model.predict(np.array([[year_input]]))

# Display the predicted number of deaths
st.write(f'Predicted number of deaths in {year_input}: {prediction[0]:.0f}')

#
# Define the data
years = np.array([1999, 2001, 2003, 2007, 2009, 2013,
                 2018, 2019, 2020]).reshape(-1, 1)
deaths = np.array([2000, 800, 1000, 1600, 1700, 1500, 500, 500, 500])

# Create polynomial features
poly_features = PolynomialFeatures(degree=3)
X_poly = poly_features.fit_transform(years)

# Create and train the polynomial regression model
model = LinearRegression()
model.fit(X_poly, deaths)

# Create Streamlit app
st.title('HIV/AIDS Deaths Prediction')
st.write('Enter a year to predict the number of deaths in France:')

# Input year from the user
year_input2 = st.number_input(
    'Year:', min_value=1999, max_value=2100, step=1, key='poly')

# Transform the input year to polynomial features
X_input = poly_features.transform(np.array([[year_input2]]))

# Make prediction for the input year
prediction = model.predict(X_input)

# Display the predicted number of deaths
st.write(f'Predicted number of deaths in {year_input2}: {prediction[0]:.0f}')
