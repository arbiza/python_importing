from example_2 import src


if __name__ == "__main__":

    lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna ...'

    for w in lorem_ipsum.split(' '):
        print(src.dumb_echo(w))
