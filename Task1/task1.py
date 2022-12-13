import pandas as pd
from bs4 import BeautifulSoup
import requests

#working with Textfiles
with open('text.txt') as f:
    print(f.readlines())

#working with csv files
df = pd.read_csv('test.csv')
print(df)

#import from websites
url = "https://www.recanorm.de/de/"

headers = {
     'Access-Control-Allow-Origin': '*',
     'Access-Control-Allow-Methods': 'GET',
     'Access-Control-Allow-Headers': 'Content-Type',
     'Access-Control-Max-Age': '3600',
     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
     }


req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.title)

#import from API
response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita%22)
print(response.json())