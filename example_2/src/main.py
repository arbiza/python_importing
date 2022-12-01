

def dumb_echo(something):
    return something


if __name__ == "__main__":

    lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna ...'

    for w in lorem_ipsum.split(' '):
        print(dumb_echo(w))
