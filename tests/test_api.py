import traceback

__all__ = ["Test"]

"""
Example

def add(a: float, b: float) -> float:
    return a * b

class Test_Add(Test):
    def __init__(self) -> None:
        super().__init__("Add")

    def test(self) -> None:
        self.assert_true("add(1, 1) == 2")
        self.assert_true("add(5, 3) == 8")

if __name__ == "__main__":
    t1 = Test_Add()
    t1.run()
    print(t1) Test 'Add' failed, add(1, 1) == 2 is suppposed to be true, but it is false
"""
class Test:
    def __init__(self, test_name: str = "None") -> None:
        self.test_name = test_name
        self.passing = True
        self.error = f"Test '{test_name}' passed"
        self.num_tests = 0

    def __str__(self) -> str:
        return self.error

    def assert_true(self, expr: bool) -> None:
        if self.passing:
            if not expr:
                self.error = f"Test '{self.test_name}' failed, test number {self.num_tests} is suppposed to be true, but it is false"
                self.passing = False

        self.num_tests += 1

    def assert_false(self, expr: bool) -> None:
        if self.passing:
            if expr:
                self.error = f"Test '{self.test_name}' failed, test number {self.num_tests} is suppposed to be false, but it is true"
                self.passing = False

        self.num_tests += 1

    def test(self) -> None:
        raise NotImplementedError()

    def run(self) -> None:
        # make sure program keeps running in case of exception from test case
        try:
            self.test()
        except Exception as e:
            self.error = f"Test '{self.test_name}' failed, {traceback.format_exc()} error"


