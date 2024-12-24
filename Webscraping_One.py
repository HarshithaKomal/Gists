#Scraping data from HTML Tables
import requests
from bs4 import BeautifulSoup
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/" \
      "HTMLColorCodes.html"
data = requests.get(url).text
soup = BeautifulSoup(data,'html5lib')
#Finding a table
table = soup.find('table')
#Getting all rows from the table
for rows in table.find_all('tr'):
    #Getting all columns in each row
    cols = rows.find_all('td')
    color_name = cols[2].string
    color_code = cols[3].string
    print("{}--->{}".format(color_name, color_code))

