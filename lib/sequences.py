#!/usr/bin/env python3

def print_fibonacci(length):
    list_items = []
    for n in range(length):
        if n < 2:
            list_items.append(n)
        else:
            list_items.append(list_items[n-2] + list_items[n-1])
    print(list_items)