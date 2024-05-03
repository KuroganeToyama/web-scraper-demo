import requests
from bs4 import BeautifulSoup

# Static content from webpage
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# Parser
soup = BeautifulSoup(page.content, "html.parser")

# Find specific element
results = soup.find(id = "ResultsContainer")

# Iterable of elements showing job
job_elements = results.find_all("div", class_ = "card-content")

for job_element in job_elements:
    # Specific data elements
    title_element = job_element.find("h2", class_ = "title")
    company_element = job_element.find("h3", class_ = "company")
    location_element = job_element.find("p", class_ = "location")

    # Final data
    title = title_element.text.strip()
    company = company_element.text.strip()
    location = location_element.text.strip()

    print(title)
    print(company)
    print(location)
    print()

