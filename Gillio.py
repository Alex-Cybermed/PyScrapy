# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:43:20 2020

@author: ryore
"""
import requests
from bs4 import BeautifulSoup

gillio = requests.get('https://www.gillio.be/en/leather-items/planners-covers/organiser-medium-compagna-xl-2')
# print(gillio.text)

soup = BeautifulSoup(gillio.text, 'html.parser')
print(soup.title.string)

#find leather type code
temp = soup.findAll(attrs = 'priceoption color')
typeli =[]
for x in temp:
    #print(type(x))
    for y in x.findAll(name = "li"):
        if y.has_attr("data-leathertypeno"):
            if y.get('data-leathertypeno') not in typeli:
                typeli.append(y.get('data-leathertypeno'))
print(typeli)

#find leather type name
temp2 = soup.findAll(attrs = 'priceoption leather')
typena =[]
for x in temp2:
    #print(type(x))
    if x.has_attr("data-title"):
        if x.get('data-title') not in typena:
            typena.append(x.get('data-title'))
print(typena)

if len(typeli) == len(typena):
    le_type={typeli[i]: typena[i] for i in range(len(typeli))}
    print(le_type)
else:
    print("Two lists don't have the same length.")
    
#find FQ/PGD/GD
temp3 = soup.findAll(attrs = 'priceoption')
priceop=[]
for x in temp3:
    if x.has_attr('title') and 'qualities' in x.parent.parent.get('class'):
        if x.get('title') not in priceop:
            priceop.append(x.get('title'))
print(priceop)

