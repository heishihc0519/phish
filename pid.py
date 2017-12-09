import requests
from bs4 import BeautifulSoup

id = 5372289


url = "https://www.phishtank.com/phish_detail.php?phish_id="
for i in range(id,0,-1):
    r = requests.get(url+str(i))
    soup = BeautifulSoup(r.text)
    print soup.find_all("b")[1].text


