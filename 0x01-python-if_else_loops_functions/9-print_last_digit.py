#!/usr/bin/python3
def print_last_digit(number):
    lastd = abs(number) % 10
    print("{:d}".format(lastd), end='')
    return lastd
