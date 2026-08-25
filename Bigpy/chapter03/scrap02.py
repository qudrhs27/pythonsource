import sys
import io
from bs4 import BeautifulSoup # uv pip install beautifulsoup4

'''
<html>
<body>
<ul id="cars">
  <li id="ge">Genesis</li>
  <li id="av">Avante</li>
  <li id="so">Sonata</li>
  <li id="gr">Grandeur</li>
  <li id="tu">Tucson</li>
</ul>
</body>
</html>
'''


fp = open("C:/source/pythonsource/Bigpy/Py_Scrap/cars.html", encoding='utf-8')

soup = BeautifulSoup(fp, 'html.parser')
# print(soup)

# 함수
def car_func(select):
    print("car_func: ", soup.select_one(select).string)

# 메인
car_func("#gr") # 가장 단순
car_func("li#gr") # li이면서 아이디가 gr
car_func("ul>#gr") # ul의 직계자식 중 id가 gr
car_func("#cars #gr") # 아이디가 #cars이면서 그 아래 어딘가에 있는 아이디가 gr
car_func("#cars > #gr") # 아이디가 #cars인 직계자식 중 id가 gr
car_func("li[id='gr']")
print("----------------------------------------------------")

# 람다식(매개변수:q)
car_lambda = lambda q: print("car_func: ", soup.select_one(q).string) 

# 메인
car_lambda("#gr") # 가장 단순
car_lambda("li#gr") # li이면서 아이디가 gr
car_lambda("ul>#gr") # ul의 직계자식 중 id가 gr
car_lambda("#cars #gr") # 아이디가 #cars이면서 그 아래 어딘가에 있는 아이디가 gr
car_lambda("#cars > #gr") # 아이디가 #cars인 직계자식 중 id가 gr
car_lambda("li[id='gr']")


print("----------------------------------------------------")
print("car_func", soup.select("li")[3].string) # select_one 한가지 엘리먼트
print("car_func", soup.find_all("li")[3].string) # find 한가지 엘리먼트