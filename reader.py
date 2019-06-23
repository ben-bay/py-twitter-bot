
import shutil
import random

def random_line(f_name):
    with open(f_name, "r") as _file:
        lines = f.read().splitlines()
        return random.choice(lines)


def pop_random_line(f_name):
    with open(f_name, "r") as _input:
        lines = _input.read().splitlines()
        index = random.randint(0,len(lines)-1)
        ret = lines[index]
        lines.remove(ret)
        text = "\n".join(lines)
        with open(f_name, "w") as _output:
            _output.write(text)
            return ret


def nth_line(f_name, n):
    with open(f_name) as _file:
        for i, line in enumerate(_file):
            if i == n - 1:
                return line


def pop_first_line(f_name):
    with open(f_name, 'r') as _input:
        line = _input.readline()
        # this will truncate the file, so need to use a different file name:
        with open(f'{f_name}', 'w') as _output:
            shutil.copyfileobj(_input, _output)
            return line
