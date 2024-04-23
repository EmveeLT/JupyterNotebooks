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
# opcijos.add_argument('--headless')                    #paleidzia be galvos

# driver = uc.Chrome(options=opcijos)
driver = webdriver.Chrome(options=opcijos)

#surinkite iš puslapių nuo 2 iki 11-to butų skelbimus ir tokią informaciją - kaina, kaina už 1 kv metrą, adresas, plotas, kambarių kiekis. 
# šiuos duomenis eksportuokite į csv failą, skirtukas turi būti ;.
#suraskite, kiek iš atrinktų butų buvo pagal kainą pigūs, brangūs, neįperkami. Kriterijus - 1 kv metro kaina iki 1 VDu - pigūs, iki 3 VDU - brangūs, daugiau nei 3 VDU - neįperkami.
#pavaizduokite su boxplotais kainų už 1 kv pasiskirstymą nuo kambarių skaičiaus.
#Pavaizduokiet tokią informaciją: atrinktų butų kainų pasiskirstymą tarp miestų.
#pavaizduokite tokią informaciją - kiek buvo sklebimų per skirtingus miestus jūsų atrankoje?


Adresas = []
Kaina = []
Kaina_uz_m2 = []
Plotas = []
Kambariu_skaicius = []

# puslapiai = [2,3,4,5,6,7,8,9,10,11]

for puslapis in range(2,11):
    url = f"https://www.aruodas.lt/butai/puslapis/{puslapis}/"
    driver.get(url)
    time.sleep(15)
    source = driver.page_source
    bs = BeautifulSoup(source, "html.parser")
    ResultsSet = bs.find_all("div" , {"class": "advert-flex"})  

    for skelbimas in ResultsSet:
            try:
                addres_element  = skelbimas.find('div', {'class':'list-adress-v2'})
                tag = addres_element.find("h3").find("a" , href = True)
                linkas = tag["href"]
                # tekstą galima pasiekti ir per 
                # .contents atributą
                tekstas = tag.contents     #jums gražina list objektą su teksto gabalais
                f = ''
                for i in tekstas:
                    f = f + str(i).strip() # str - kad garantuotai būtų tekstas
                adresas = f.replace('<br/>', ', ')
                Adresas.append(adresas)

                kainaRaw = addres_element.find("div" ,{"class" :"price"}).find('span', {'class':'list-item-price-v2'})
                kainaInt = kainaRaw.text.strip().replace("\n", "").replace(" ", "").replace("€", "")
                kainaInt2 = int(kainaInt)
                Kaina.append(kainaInt2)

                kainaUzM2 = addres_element.find("div" ,{"class" :"price"}).find('span', {'class':'price-pm-v2'})
                kainaUzM2Int = kainaUzM2.text.strip().replace("\n", "").replace(" ", "").replace("€/m²", "")
                kainaUzM2Int2 = int(kainaUzM2Int)
                Kaina_uz_m2.append(kainaUzM2Int2)


                plotas = skelbimas.find("div" ,{"class" :"list-AreaOverall-v2 list-detail-v2"})
                plotastext = plotas.text.strip().replace("\n", "").replace(" ", "")
                plotasFloat = float(plotastext)
                Plotas.append(plotasFloat)


                kambariai = skelbimas.find('div', {'class':'list-RoomNum-v2 list-detail-v2'})
                kambariaiTxt= kambariai.text.strip() #replace("\n", "").replace(" ", "")
                kambariaiFloat = float(kambariaiTxt)
                Kambariu_skaicius.append(kambariaiFloat)
               
                print(kainaInt2, adresas ,kainaUzM2Int2 , plotasFloat , kambariaiFloat , "=============SKELBIMAI===============")
            except Exception as klaida:
               print(klaida)  

driver.close()


dfVisiSkelbimai = pd.DataFrame(data={'Adresas':Adresas, 'Kaina':Kaina, 'Kaina_uz_m2':Kaina_uz_m2, 'Plotas':Plotas, 'Kambariu_skaicius':Kambariu_skaicius})
dfVisiSkelbimai.to_csv('uzduotisnuo2iki11.csv', sep=';')