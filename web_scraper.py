# Import BeautifulSoup and requests
from bs4 import BeautifulSoup
import requests


#Define function to input website to scrape
def input_website():
    website = input("Enter website to scrape (Make sure you add http:// or https://): ")
    return website

#Define function to input number of pages to scrape
def input_pages():
    pages = input("Enter number of pages to scrape: ")
    return pages

#Define function to scrape website
def scrape_website(website, pages):
    #Loop through number of pages
    for i in range(1, int(pages) + 1):
        #Create URL
        url = website + "?page=" + str(i)
        #Get HTML from URL
        html = requests.get(url)
        #Create BeautifulSoup object
        soup = BeautifulSoup(html.text, "html.parser")
        #Find all <a> tags
        a_tags = soup.find_all("a")
        #Loop through all <a> tags
        for a_tag in a_tags:
            #Find href attribute
            href = a_tag.get("href")
            #Print href attribute
            print(href)

#Define function to write to file
def write_to_file(website, pages):
    #Loop through number of pages
    for i in range(1, int(pages) + 1):
        #Create URL
        url = website + "?page=" + str(i)
        #Get HTML from URL
        html = requests.get(url)
        #Create BeautifulSoup object
        soup = BeautifulSoup(html.text, "html.parser")
        #Find all <a> tags
        a_tags = soup.find_all("a")
        #Loop through all <a> tags
        for a_tag in a_tags:
            #Find href attribute
            href = a_tag.get("href")
            #Write href attribute to file
            with open("links.txt", "a") as file:
                file.write(str(href) + "\n")

#Define function to read from file
def read_from_file():
    #Open file
    with open("links.txt", "r") as file:
        #Read file
        links = file.read()
        #Print file
        print(links)

#Call functions
website = input_website()
pages = input_pages()
scrape_website(website, pages)
write_to_file(website, pages)
read_from_file()


#End of program
print("Website Scraper Complete!")
