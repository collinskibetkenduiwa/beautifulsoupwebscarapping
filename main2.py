from bs4 import BeautifulSoup
import requests
import time


html_texts=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup=BeautifulSoup(html_texts,'lxml')



jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
# print(timesjobs)

print('Enter some skills big guy :)')
familiar_skills=input()

def find_jobs():
    for job in jobs:

        published_date=jobs.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name=jobs.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=jobs.find('span',class_='srp-skills').text.replace(' ','')
            more_info=jobs.header.h2.a['href']

            if familiar_skills not in skills:
                    
                print(f"""

                company name:{company_name}
                skills required:{skills}
                date published:{published_date}
                more info :{more_info}
                """)



if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait=10
        time.sleep(time_wait=60)
        