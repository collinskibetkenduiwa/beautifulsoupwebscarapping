from bs4 import BeautifulSoup

with open('/home/collins/pythonprojects/taxapp/home.html','r') as home_file:
    content=home_file.read()
    # print(content)

    soup=BeautifulSoup(content,'lxml')
    divclases=soup.find_all('div')

    for divv in divclases:
        course_name=divv.h4.text
        course_price=divv.a.txt.split('\n')
        
        print(f'{course_price},{course_name}')



    # titlesinhtml=soup.find_all('title')
    # for titl in titlesinhtml:
    #     print(titl.txt)
