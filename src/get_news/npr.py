import requests
from bs4 import BeautifulSoup


def get_content(url):

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    else:
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"


def read_from_file(filepath):
    with open(filepath, "r") as file:
        file_content = file.read()
    return file_content


if __name__ == "__main__":
    url = "https://www.npr.org/sections/world/"

    # print(get_content(url))

    soup = BeautifulSoup(read_from_file("output.txt"), "html.parser")

    article_tags = soup.find_all("article")

    urls = set()
    for article in article_tags:
        a_tags = article.find_all("a")
        for a in a_tags:
            href = a.get("href")
            if href:
                urls.add(href)

    keywords = [
        "/sections/",
        "/transcripts/",
        "ondemand.npr.org",
        "chrt.fm/track/",
        "/podcasts/",
        "/series/",
    ]

    for keyword in keywords:
        urls = {url for url in urls if keyword not in url}

    for url in urls:
        print(url)

    # urls = [a.get("href") for a in article_tags if a.get("href")]

    # print(urls)
