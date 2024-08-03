import sys
sys.path.append("../src")

from test_api import Test
import get_news as gn
import summarize_news as sn
import present_news as pn
import automatic_news_presenter as anp

# write tests in here
class Test_Article(Test):
    def __init__(self) -> None:
        super().__init__("Article Test")

    def test(self):
        article = gn.Article("test", "test", "test")
        self.assert_true('article.body == \"test\"')
        self.assert_true('article.title == \"test\"')
        self.assert_true('article.link == \"test\"')

#
if __name__ == "__main__":
    test_cases: list[Test] = [Test_Article()]
    for test_case in test_cases:
        test_case.test()
        print(test_case)