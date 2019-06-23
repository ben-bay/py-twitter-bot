
import shutil
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


def pop_first_line(f_name):
    source_file = open(f_name, 'r')
    line = source_file.readline()
    # this will truncate the file, so need to use a different file name:
    target_file = open(f'{f_name}', 'w')
    shutil.copyfileobj(source_file, target_file)
    return line
