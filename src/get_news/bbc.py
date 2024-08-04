from .article import Article
from bs4 import BeautifulSoup
import requests

_BASE_LINK = "https://www.bbc.com"
_WORLD_NEWS_LINK = _BASE_LINK + "/world"
_ARTICLE_LINK = _BASE_LINK + "/news/articles"
_TYPES_OF_CARDS = ("london-card", "edinburgh-card", "manchester-card")

def from_bbc() -> list[Article]:
    news_list = []
    soup = BeautifulSoup(requests.get(_WORLD_NEWS_LINK).content.decode(), "html.parser");
    media = soup.find_all("div", attrs={"data-testid": _TYPES_OF_CARDS[0]})
    media.extend(soup.find_all("div", attrs={"data-testid": _TYPES_OF_CARDS[1]}))
    media.extend(soup.find_all("div", attrs={"data-testid": _TYPES_OF_CARDS[2]}))

    for m in media:
        cur = Article(
            m.h2.get_text(),
            "",
            _BASE_LINK + m.a['href'],        
        )

        if not cur.link.startswith(_ARTICLE_LINK):
            continue

        # print(cur)
        news_list.append(cur)

    return list(set(news_list))