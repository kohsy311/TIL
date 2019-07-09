import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

html = requests.get(url).text #request야 정보 좀 get해줘
soup = BeautifulSoup(html,'html.parser') #파서가 유의미한 정보를 가져와
print(type(soup))
kospi = soup.select_one('#KOSPI_now').text #선택자 복붙
print(f'오늘의 코스피 지수는 {kospi}입니다.')