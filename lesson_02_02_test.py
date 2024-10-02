import pytest
from lesson_02_02 import is_palindrome, sort_list

def test_is_palindrome_true():
   assert is_palindrome("madam") == True

def test_is_palindrome_false():
   assert is_palindrome("hello") == False


@pytest.mark.parametrize("s, expected", [
   ("racecar", True),
   ("python", False),
   ("level", True),
   ("", True),  # Пустая строка является палиндромом
])
def test_is_palindrome_parametrized(s, expected):
   assert is_palindrome(s) == expected


def test_sort_list1():
   assert sort_list([3, 1, 2, 5, 4]) == [1, 2, 3, 4, 5]

def test_sort_list2():
   assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]
