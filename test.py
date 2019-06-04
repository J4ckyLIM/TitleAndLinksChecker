import requests
from bs4 import BeautifulSoup

response = requests.get('https://qz.com/africa/latest/')

if response:
    print('Success')
else:
    print('An error has occured')

page = response.text

soup = BeautifulSoup(page, 'html.parser')

print(soup.prettify())

h3_query = soup.fin_all('h3')

link_query = soup.find_all('a')

h3_title = "{article_title}: "

link_title = "{article_link}: "

for h3 in h3_query:
    print(h3_title + str(h3))

for link in link_query:
    print(link_title + str(link))
    


    

