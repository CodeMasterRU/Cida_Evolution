# %%
# Imports
import pandas as pd
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time



def scrap1():
    globalTab = []

    page_url = "https://en.wikipedia.org/wiki/Epidemiology_of_HIV/AIDS" 
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(page_url)
    time.sleep(5)

    all = driver.find_element(By.XPATH, '//table[@class="wikitable"]')

    rows = []
    count = 0
    for element in all.find_elements(By.XPATH, './/td'):
    
        element_text = element.text.strip()
        rows.append(element_text)
        if count % 4 == 3:
            globalTab.append(rows)
            rows = []
        count+=1
# print(globalTab)
    for i in range(len(globalTab)):
        for j in range(len(globalTab[i])):
            if globalTab[i][j].isdigit():
                globalTab[i][j] = int(globalTab[i][j].replace(' ', ''))
            elif globalTab[i][j].replace(' ', '').isdigit():
                globalTab[i][j] = int(globalTab[i][j].replace(' ', ''))
    df = pd.DataFrame(globalTab, columns=["year", "deaths_due_globally", "infection_incidence_rate", "infection_prevalence_rate"])
    df['year'] = df['year'].replace('2021[39]', '2021')
    print(df)
    df.to_excel("./deaths.xlsx", index = False)
    df.to_csv("./deaths.csv", index = False)
    driver.close()

scrap1()

# mydf = scrapping()

# # %%
# import numpy as np
# import seaborn as sns
# deaths_df = pd.read_csv("./deaths.csv")
# # print(deaths_df.dtypes)

# g = sns.barplot(data=deaths_df, x="year", y="deaths_due_globally")
# g.set_ylabel("Number of Deaths (millions)")
# g.set_title("World")


def scrap2():
    globalTab = []
    page_url = "https://fr.wikipedia.org/wiki/Épidémiologie_du_sida" 
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(page_url)
    time.sleep(5)
    count = 0
    all = driver.find_element(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]')

    rows = []
    # /html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody/tr[1]/td[2]
    for element in all.find_elements(By.XPATH, './/td'):
        rows.append(element.text)
        if count % 5 == 4:
            globalTab.append(rows)
            rows = []
        count += 1

    print(globalTab)
    df = pd.DataFrame(globalTab, columns=["id","1990-1999", "2000-2009", "2010-2019", "Total cumulé des décès"])
    # df.to_excel("deaths_all_continents.xlsx", index=False)
    df.to_csv("./deaths_all_continents.csv", index=False)
scrap2()
# # %%
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("deaths_all_continents.csv", index_col="id")
# print(df)

# df = df.replace('\s+', '', regex=True).astype(int)

# # Plot bar chart
# ax = df.plot(kind='bar', figsize=(10, 6))
# ax.set_title("Total Cumulative Deaths by Region and Time Period")
# ax.set_ylabel("Number of Deaths (millions)")
# ax.legend(title="Time Period", fontsize='small')

# # Show plot
# plt.show()
