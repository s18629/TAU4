from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description
from hamcrest.core.helpers.hasmethod import hasmethod

class ResultHigherThanTen(BaseMatcher):
    def _matches(self, item):
        if not item < 10:
            return False
        return len(item)

    def describe_to(self, description: Description):
        return


def isEmpty():
    return ResultHigherThanTen()
