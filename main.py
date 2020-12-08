import requests
import re
from bs4 import BeautifulSoup

user_agent = 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/86.0.4240.198 Safari/537.36 '
headers = {
    'User-Agent': user_agent
}

result = requests.get('https://www.gillio.be/en/leather-items/planners-covers', headers=headers)
html_body = result.text
soup = BeautifulSoup(html_body, 'html.parser')

res = re.search('<nav class="filter(.*)">(.*?)Planner model(.*?)</nav>', html_body, re.S) #

if res is not None:
    parsedSoup = BeautifulSoup(res.group(), 'html.parser')
    print(parsedSoup)
#     print(res.group(1))
