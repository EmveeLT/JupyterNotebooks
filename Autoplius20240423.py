import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import time
import selenium
# import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

opcijos = Options()
opcijos.add_argument('--incognito')
driver = webdriver.Chrome(options=opcijos)

# jūsų atrankoje, kiek automobilių buvo su automatu, mech, kokios jų buvo vidutinės kainos?            #advanced: su pie plot atvaizduokite gamintojų užimamą rinkos dalį (5 didžiausi + visi kiti)

Automatine = []
Mechanine = []

for puslapis in range(2,3):
    try: 
        url = f"https://m.autoplius.lt/skelbimai/naudoti-automobiliai?qt=&page_nr={puslapis}/"
        driver.get(url)
        time.sleep(15)
        source = driver.page_source
        bs = BeautifulSoup(source, "html.parser")
        ResultsSet = bs.find_all("div" , {"class": "description"})
    # except Exception as klaida:
    #     print(klaida)
        try:
            for skelbimas in ResultsSet:
                year  = skelbimas.find('div', {'class':'title-year'}).text.strip()
                gamintojas = skelbimas.find('div', {'class':'line1'}).text.strip()
                kaina = skelbimas.find('div', {'class':'pricing-container'}).find("strong").text.strip()
                parametras = skelbimas.find('div', {'class':'item-parameters'}).text.strip().replace("\n", ";")
                print("=============SKELBIMAI===============")
                print(year, gamintojas , parametras, kaina)
        except: 
             pass


    except Exception as klaida:
            print(klaida)  
        