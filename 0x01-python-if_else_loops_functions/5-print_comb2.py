#!/usr/bin/python3
for i in range(0, 99):
    if i < 99:
        print(f"{i//10}{i%10}", end=", ")
    else:
        print(f"{i}")
