from turtle import title
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page="
result = []
for page_number in range(1, 20):
    response = requests.get(url+str(page_number))
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        newLaptop = []
        newDesk = []
        laptop_names = soup.find_all("a", class_="title")
        laptop_prefs = soup.find_all("p", class_="description")
        for index, laptop in enumerate(laptop_names):
            newLaptop.append(laptop.attrs['title'])
        for index, laptop in enumerate(laptop_prefs):
            newDesk.append(laptop.text)
        for i in range(len(newLaptop)):
            result.append([newLaptop[i], newDesk[i]])
    else:
        print(f"Error on page {page_number}")

print(*result, sep="\n")