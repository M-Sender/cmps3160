import pandas as pd
import bs4
from bs4 import BeautifulSoup
import requests
#2
url = "https://www.spaceweatherlive.com/en/solar-activity/top-50-solar-flares"
webpage = requests.get(url)
print(webpage) #response 403, this means that the webserver refused to authorize the request
#to fix do this
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
webpage = requests.get(url, headers=headers)
print(webpage) #now response 200
soup_content = BeautifulSoup(webpage.content,'html.parser')
pretty = soup_content#.prettify()
#print(pretty)
table_html = pretty.find("table",{"class":"table table-striped"})#['data-value']
pd.read_html(table_html)
