import pytest
from home_ex_02_01 import count_vowels

@pytest.mark.parametrize("s, expected", [
   ("AaOeI", 5),
   ("python", 2),
   ("lEvel", 2),
   ("ghrl", 0),
   ("", 0),
])
def test_count_vowels_parametrized(s, expected):
   assert count_vowels(s) == expected