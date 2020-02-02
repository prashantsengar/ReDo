import requests
from bs4 import BeautifulSoup as bs

def get_results(q):
    q = q.replace(' ','+')
    url = 'https://www.wikihow.com/wikiHowTo?search=' + str(q)

    res = requests.get(url)
    soup = bs(res.text, 'lxml')
    links = soup.find('div',{'id':'searchresults_list'}).findAll('a')

    how_url = []
    titles = []
    text_data = {}
    for ur in links[:2]:
        how_url.append(ur.get('href'))
        titles.append(ur.find('div',{'class':'result_title'}).text)
##        titles.append(ur.text)
        text_data[links.index(ur)]=[ur.get('href'),ur.find('div',{'class':'result_title'}).text]
    
    return text_data


