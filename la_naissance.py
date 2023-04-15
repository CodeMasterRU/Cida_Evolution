# Imports
import pandas as pd
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

rows = []

def scrapping():
    page_url = "https://en.wikipedia.org/wiki/Epidemiology_of_HIV/AIDS" 
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(page_url)

    all = driver.find_element(By.XPATH, '//ul[@class="product-grid"]')


    for x in all.find_elements(By.XPATH, './/li[@class="product-grid-item"]'):
        year = x.find_element(By.XPATH, './/h2[@class="ds-title ds-title--s"]').text
        Infection_Incidence_Rate = x.find_element(By.XPATH, './/span[@class="product-price__amount-value"]').text
        Infection_Prevalence_Rate = x.find_element(By.XPATH, './/div[@class="ds-body-text ds-product-card-refonte__perunitlabel ds-body-text--size-s ds-body-text--color-standard-3"]').text.strip(' € / KG')
        rows.append((year, Infection_Incidence_Rate, Infection_Prevalence_Rate))

    # driver.close()
    # df = pd.DataFrame(rows, columns=["titre", "prix_barquette", "prix_par_kilo"])
    # df.to_csv(f"la_naissace.csv", index=False)
    # df.to_excel(f"test{page}.xlsx", index=False)

mydf = scrapping()