import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

article_title_description = soup.find(name="div", class_="article-title-description__text")
# print(article_title_description)

titles = soup.find_all(name="h3", class_="title")
# print(titles)

movies_to_watch = [title.text for title in titles]
movies_to_watch.reverse()
print(str(movies_to_watch))

with open(file="100_movies_to_watch.txt", mode="w", encoding="ISO-8859-1") as file:
    for movie in movies_to_watch:
        file.write(f"{movie}\n")