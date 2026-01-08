from bs4 import BeautifulSoup

with open("33-BeatifulSoup/bs4-start/website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")
#print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")

#for tag in all_anchor_tags:
#    print(tag.getText())
#   print(tag.get("href"))
    
heading = soup.find(name="h1", id="name")
print(heading)

class_is_heading = soup.find_all(class_="heading")
print(class_is_heading)

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)