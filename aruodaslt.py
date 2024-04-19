import selenium
# import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time # dėl sleep komandos
import pandas as pd


opcijos = Options()
opcijos.add_argument('--incognito')

# driver = uc.Chrome(options=opcijos)
driver = webdriver.Chrome(options=opcijos)

url = "https://www.kaunodiena.lt"

driver.get(url)
time.sleep(3)

source = driver.page_source # pasiimam puslapio html kodą

bs = BeautifulSoup(source , "html.parser")           #teoriskai isparsinome puslapio html
resultsSet = bs.find_all("a" , {"class":'articles-list-title'})



#Surinkite visus kauno dienos straipsnių pavadinimus į pandas dataframe. V

#pridėkite naują stulpelį, kuriame būtų žodžių kiekis kiekviename pavadinime
#pridėkite naują stulpelį, kuriame būtų pavadinime esančių simbolių kiekis eksportuokite tai į CSV failą

#eksportuotą CSV failą nuskaitykite su pandas
#Koks vidutinis žodžių kiekis pavadinimuose? 
#Advanced: suraskite dažniausiai pasikartojantį žodį pavadinimuose.

sarasas = []

for elementas in resultsSet:
    # print("::Elementas:::")
    # print(elementas)
    # print(elementas["href"])   #["href"] is atrinktos klases leidzia gauti dali linko (nuoroda ,adresa)
    # print(elementas.text)        #pasiekiame elemente esanti teksta siuo atveju straipsnio pavadinima
    sarasas.append(elementas.text)

#Surinkite visus kauno dienos straipsnių pavadinimus į pandas dataframe. V

dfSarasas = pd.DataFrame()
dfSarasas['Pavadinimas'] = sarasas
dfSarasas.to_csv('20240419 darbai.csv', sep=';')

#pridėkite naują stulpelį, kuriame būtų pavadinime esančių simbolių kiekis eksportuokite tai į CSV failą

def skaiciuotZodzius(pavadinimas):
    return len(pavadinimas.split())

dfSarasas["žodžių_kiekis"] = dfSarasas["Pavadinimas"].apply(skaiciuotZodzius)
dfSarasas.to_csv('20240419 darbai.csv', sep=';')

#eksportuotą CSV failą nuskaitykite su pandas

KaunoDiena = pd.read_csv('20240419 darbai.csv')   
print(KaunoDiena)





# print(source)
# driver.close()


