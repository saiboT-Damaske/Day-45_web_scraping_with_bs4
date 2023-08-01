from bs4 import BeautifulSoup
import lxml  # optionally for some websites required # when Error: parser not working
import requests
# with open("./website.html", encoding="utf-8") as website:
#     content = website.read()
#
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.string)
#
# print(soup.li)
#
# list = soup.find_all(name="li")
#
# for item in list:
#     print(item.getText())
#     print(item.get("id"))
#
# certain_url = soup.select_one(selector="p a")  # select one gets the first one
# print(certain_url)
#
# print(soup.select(selector=".heading"))


response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

# get title
titles = soup.select(selector=".title a ")
print(titles)
texts = []
i = 0
for title in titles:
    if i % 2 == 0:
        texts.append(title.text)
    else:
        pass
    i += 1

links = []
i = 0
for title in titles:
    if i % 2 == 0:
        links.append(title.get("href"))
    else:
        pass
    i += 1

scores = soup.find_all(name="span", class_="score")
upvotes = [int(score.getText().split()[0]) for score in scores]

print(texts)
print(links)
max_votes_index = upvotes.index(max(upvotes))
print(upvotes[max_votes_index])
print(texts[max_votes_index])
print(links[max_votes_index])
