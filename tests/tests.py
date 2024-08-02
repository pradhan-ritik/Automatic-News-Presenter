import sys
sys.path.append("../src")

from test_api import Test
import get_news as gn
import summarize_news as sn
import present_news as pn
import automatic_news_presenter as anp

# write tests in here

#
if __name__ == "__main__":
    test_cases: list[Test] = []
    for test_case in test_cases:
        test_case.test()
        print(test_case)