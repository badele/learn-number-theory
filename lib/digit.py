def dsum(num, loop=False):
    sdigit = 0
    for s in str(num):
        sdigit += ord(s) - 48

    return sdigit


def dsub(num, loop=False):
    sdigit = int(str(num)[0])
    for s in str(num)[1:]:
        sdigit -= ord(s) - 48

    return sdigit


def digital_root(n):
    # https://mathworld.wolfram.com/DigitalRoot.html

    return 1 + ((n - 1) % 9)
