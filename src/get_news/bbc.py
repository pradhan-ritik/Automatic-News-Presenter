from .article import Article
from bs4 import BeautifulSoup
from requests import get
from re import compile
from html import unescape

_BASE_LINK = "https://www.bbc.com"
_WORLD_NEWS_LINK = _BASE_LINK + "/world"
_ARTICLE_LINK = _BASE_LINK + "/news/articles"
_TYPES_OF_CARDS = ("london-card", "edinburgh-card", "manchester-card")
_GET_DIV_TEXT = compile(r"\<div\sdata\-component\=\"text-block\"\s[^\>]*\>(.*?)\<\/div\>")
_GET_TEXT_FROM_DIV = compile(r"\>(.*?)\<")

def from_bbc() -> list[Article]:
    news = set()
    soup = BeautifulSoup(get(_WORLD_NEWS_LINK).content.decode(), "html.parser");
    media = soup.find_all("div", attrs={"data-testid": _TYPES_OF_CARDS[0]})
    media.extend(soup.find_all("div", attrs={"data-testid": _TYPES_OF_CARDS[1]}))
    media.extend(soup.find_all("div", attrs={"data-testid": _TYPES_OF_CARDS[2]}))

    for m in media:
        cur = Article(
            m.h2.get_text(),
            "",
            _BASE_LINK + m.a['href'],        
        )

        if (not cur.link.startswith(_ARTICLE_LINK)) or cur in news:
            continue
        
        # bs4 hates 
        article = get(cur.link).content.decode()
        text_blocks = _GET_DIV_TEXT.findall(article)
        for block in text_blocks:
            text = _GET_TEXT_FROM_DIV.findall(block)
            cur.body += " ".join(filter(lambda x: x != "", [i for i in text]))

        cur.body = unescape(cur.body)
        news.add(cur)

    return list(news)