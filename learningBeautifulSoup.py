import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
#print(results.prettify())

job_list = list()
for job in job_elements:
    #print(job, end="\n"*3)
    job_name = job.find("h2", class_="title is-5")
    company_name = job.find("h3", class_="subtitle is-6 company")
    location = job.find("p", class_="location")


    #print(job_name.text)
    #print(company_name.text)
    #print(location.text)
    job_tuple = (job_name.text.strip(), company_name.text.strip(), location.text.strip())
    job_list.append(job_tuple)

#print(job_list)

while(True):
    user_input = input("What keyword do you want to search by? Or 'exit' to quit\n")
    if (user_input == ('exit').lower()):
        break

    for job in job_list:
        for element in job:
            if(user_input.lower() in element.lower()):
                print(job)
    print("-"*100 + "\n")
