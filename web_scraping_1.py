from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup)
# print(soup.title)
# print(soup.title.string)

# print(soup.li)
# print(soup.li.string)

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(f'{tag.getText()}: {tag.get("href")}')

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.getText())
