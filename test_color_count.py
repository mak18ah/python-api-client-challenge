from enum import Enum
from typing import Final, List, Tuple

import pytest
from pydantic import BaseModel

from main import query_color_count, query_api_version

API_VERSION: Final[int] = 1


class ColorDataResponsePayload(BaseModel):
    count: int


class APIVersionResponsePayload(BaseModel):
    version: int


class ColorNames(str, Enum):
    green = 'green'
    red = 'red'
    blue = 'blue'
    yellow = 'yellow'
    magenta = 'magenta'


colors: List[Tuple[str, int]] = [
    (ColorNames.green, 2),
    (ColorNames.red, 3),
    (ColorNames.blue, 1),
    (ColorNames.yellow, 1),
    (ColorNames.magenta, 0)
]


@pytest.mark.parametrize("color,expected_count", colors)
def test_query_color_count(color: str, expected_count: int) -> None:
    """Asserts that the counted colors from JSON blob matches expected"""
    color_count_response: ColorDataResponsePayload = query_color_count(color)
    assert expected_count == color_count_response.count


def test_query_api_version() -> None:
    """Asserts called API is correct version"""
    api_version: APIVersionResponsePayload = query_api_version()
    assert API_VERSION == api_version.version
