import requests
from bs4 import BeautifulSoup

URL = 'https://hh.ru/search/vacancy?&text=python&customDomain=1'

headers = {
    'Host': 'hh.ru',
    'User-Agent': 'Safari',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}


def extract_max_page():


    hh_request = requests.get(URL, headers=headers) #f позволяет писать переменные вместе с текстом

    #(hh_request.text)

    hh_soup = BeautifulSoup(hh_request.text,'html.parser')

    pages = []

    paginator = hh_soup.find_all("span", {'class': 'pager-item-not-in-short-range'})

    for page in paginator:
        pages.append((int(page.find('a')._text)))

    return pages[-1]

#max_page = pages[-1] # выводит последний элемент списка

def extract_hh_jobs(last_page):
    jobs=[]
    #for page in range (last_page):
    result= requests.get(f'{URL}&page=0', headers=headers)
    print(result.status_code)
    soup = BeautifulSoup(result.text,'html.parser')
    results = soup.find_all('div',{'class': 'vacancy-serp-item'})
    for result in results:
        title = result.find('a')._text
        print(title)
        company = result.find('div', {'class':'vacancy-serp-item__meta-info-company'}).find('a')._text
        print(company)
    return jobs
#paginator = hh_soup.find("span", {'class': 'bloko-button-group'})

#pages = paginator.find_all('a')

#print(pages)

# page in range(max_page):
 #   print(f'page={page}')