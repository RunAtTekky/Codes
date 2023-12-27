from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.youtube.com/playlist?list=PLQWhFQLqZ12fnOwWCDjsovt3qrqDafSVr').text

soup = BeautifulSoup(html_text, 'lxml')
videos = soup.find_all('div', id = 'contents')

# print(soup)

print(videos)
