# web1.python
from bs4 import BeautifulSoup

#페이지로딩:메서드체인(연속으로 함수, 메서드 호출)
page = open("c:\\work\\test01.html", "rt", encoding="utf8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#전체 페이지 보기
#print( soup.prettify())

#<p>태그 전부 검색
#print( soup.find_all("p") )
#첫번째 <p>태그
print( soup.find("p") )

#검색의 조건: <p class_="outer-text">
#파이썬의 키워드로 class제공(이름충돌): class_
print( soup.find_all("p", class_="outer-text") )


