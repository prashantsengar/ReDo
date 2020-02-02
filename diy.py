import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.thesprucecrafts.com/search?q='

def get_data(q):
    q = q.replace(' ','+')
    res = requests.get(url+q)
    soup = bs(res.text, 'lxml')
    results = soup.findAll('ul',{'id':'search-results-list-1_1-0'})[0]#.findAll('section',{'class':'o-ArticleResult o-ResultCard'})
    return results
