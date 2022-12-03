from hamcrest.core.base_matcher import BaseMatcher, T
from hamcrest.core.description import Description
from hamcrest.core.helpers.hasmethod import hasmethod


class isGivenListIsEmpty(BaseMatcher):
    def _matches(self, item: list):
        if not len(item) == 0:
            return False
        return len(item)

    def describe_to(self, description: Description):
        return


def isEmpty():
    return isGivenListIsEmpty()
