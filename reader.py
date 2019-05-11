
import random

def random_line(f_name):
    with open(f_name, "r") as f:
        lines = f.read().splitlines()
        return random.choice(lines)


def nth_line(f_name, n):
    with open(f_name) as f:
        for i, line in enumerate(f):
            if i == n - 1:
                return line


