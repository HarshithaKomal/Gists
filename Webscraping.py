import requests
from bs4 import BeautifulSoup
url = "http://www.ibm.com"
data = requests.get(url).text #GET CONTEXTS OF A WEBPAGE IN TEXT FORMAT
soup = BeautifulSoup(data,'html5lib')
#SCRAPING ALL LINKS
for link in soup.find_all('a',href=True):
    print(link.get('href'))
#SCRAPING ALL IMAGES
for l in soup.find_all('img'):
    print(l)
    print(l.get('src'))