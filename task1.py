import requests
from bs4 import BeautifulSoup

url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

posting_dates = []
for row in soup.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) > 0:
        cols = [col.text.strip() for col in cols]
        posting_dates.append(cols[0])

print(posting_dates)
