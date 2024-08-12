import sys
sys.path.append("../src")

from test_api import Test
import get_news as gn
import summarize_news as sn
import present_news as pn
import automatic_news_presenter as anp

class Test_Article(Test):
    def __init__(self) -> None:
        super().__init__("Article Test")

    def test(self):
        article = gn.Article("test", "test", "test")
        self.assert_true(article.body == "test")
        self.assert_true(article.title == "test")
        self.assert_true(article.link == "test")
        self.assert_true(article == gn.Article("test", "test", "test"))
        # make sure __hash__ __eq__ and __nq__ functions work correctly
        self.assert_false(len(list(set([article, gn.Article("test", "testetsetset", "test")]))) == 2)

class Test_BBC(Test):
    def __init__(self) -> None:
        super().__init__("BBC")

    def test(self):
        articles = gn.from_bbc()
        # make sure we actually got the articles
        self.assert_true(articles)
        for article in articles:
            print(article)

if __name__ == "__main__":
    # running the test cases
    test_cases: list[Test] = [
        Test_Article(),
        Test_BBC(),
    ]
    
    for test_case in test_cases:
        test_case.run()
        print(test_case)