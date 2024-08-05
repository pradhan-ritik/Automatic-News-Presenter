from dataclasses import dataclass

@dataclass
class Article:
    title: str
    body: str
    link: str

    # this is to be able to quickly identify duplicates in sets before wasting a bunch of time loading a webpage
    def __hash__(self) -> int: 
        return hash(self.title)

    def __eq__(self, other: "Article") -> bool:
        return self.title == other.title

    def __ne__(self, other: "Article") -> bool:
        return not self.__eq__(other)