import requests
from bs4 import BeautifulSoup
web = "https://www.phishtank.com/phish_archive.php"
js = []

def run(page):
    r = requests.get(web+page)
    soup = BeautifulSoup(r.text)
    url = [i for i in soup.find_all('tr')]
    next_url = [i for i in soup.find_all('a') if "Older" in i.text]
    parse(url)
    page = next_url[0]['href']
    return page

def parse(next_url):
    for i in range(1,len(next_url)):
        td = next_url[i].find_all('td')
        js.append([i.text for i in td])
        
    





def main():
    r = requests.get(web)
    soup = BeautifulSoup(r.text)
    url = [i for i in soup.find_all('tr')]
    next_url = [i for i in soup.find_all('a') if "Older" in i.text]
    page = next_url[0]['href']
    for i in range(5):
        page = run(page)
        print page
    print js

if __name__ == "__main__":
    main()
