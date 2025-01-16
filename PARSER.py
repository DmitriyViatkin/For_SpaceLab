import requests 
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np


from Config import url_tamplat
produkt_list={'name':[], 'Description':[]}
FILE_NAME = 'test.csv'

def parser(url_tamplate):
    
    print(url_tamplate)
    r=requests.get(url_tamplate)
    
    soup = bs(r.text, "lxml")
    #print(soup)
    produkts = soup.find_all('div', class_= 'product-wrapper card-body')
    
    for produkt in produkts:
        
        produkt_list['name'].append(produkt.find('a').text)
        
        produkt_list['Description'].append(produkt.find(class_='description card-text').text)
        
        
    #print(produkt_list) 
    df = pd.DataFrame(produkt_list,columns=['Name','Description'])
    
    df.to_csv(FILE_NAME,index=True)
    return produkt_list
    
    
#
def scrol(url_tamplate):
    for i in range(1,21):
        url=url_tamplate+str(i)
        parser(url)
scrol(url_tamplat)
"""df = pd.DataFrame(scrol(url_tamplat))
#df = pd.DataFrame(parser(url_tamplat+str(2)))
df.to_csv(FILE_NAME,index=True)"""