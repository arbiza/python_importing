
# Without src/__init__.py
# from example_2.src import main

# With src/__init__.py
from example_2 import src


def test_dumb_echo():
    test_str = 'Ran from a test using pytest!'
    assert test_str is src.main.dumb_echo(test_str)


if __name__ == "__main__":
    test_str = 'This is the main function to run using \'python\''
    print(src.main.dumb_echo(test_str))
