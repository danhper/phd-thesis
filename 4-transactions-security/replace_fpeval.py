import glob
import re
from os import path
import re
import sys

INT_COMMAND_REGEXP = re.compile(r'\\newcommand\{(\\[a-z0-9A-Z]+)\}\{([0-9]+)\}')

ARG_REGEXP = re.compile(r'\{(.*?)\}')


class Command:
    def __init__(self, name, args_count, func):
        self.name = name
        self.args_count = args_count
        self.func = func
        self.regexp = re.compile(r"\\" + self.name)

    def execute(self, text, i, context):
        pos = i + len(self.name) + 1
        args = []
        for _ in range(self.args_count):
            arg_match = ARG_REGEXP.match(text[pos:])
            if not arg_match:
                raise ValueError("could not get arg for {0}: {1}".format(self.name, text))
            arg = arg_match.group(1)
            for k, v in context.items():
                arg = arg.replace(k, str(v))
            args.append(arg)
            pos += arg_match.span()[1]
        result = self.func(*args)
        text = text[:i] + str(result) + text[pos:]
        return text


def numprint(s):
    if "." in s:
        return "{:.2f}".format(float(s))
    else:
        return "{:,}".format(int(s))

def tps(x, s):
    v = int(x) / 213 / 24 / 3600
    return ("{0:." + s + "f}").format(v)


COMMANDS_TO_REPLACE = [
    Command("fpeval", 1, lambda x: eval(x)),
    Command("tps", 2, tps),
    Command("numprint", 1, numprint),
    Command("blockscount", 2, lambda x, y: "{0:,}".format(int(y) - int(x) + 1)),
]


def compute_text(text):
    values = {}
    for line in text.splitlines():
        match = INT_COMMAND_REGEXP.match(line)
        if match:
            values[match.group(1)] = int(match.group(2))
    return values


def replace_occurences(text, context):
    for command in COMMANDS_TO_REPLACE:
        regexp = command.regexp
        while True:
            occurence = regexp.search(text)
            if not occurence:
                break
            text = command.execute(text, occurence.span()[0], context)
    return text

with open(sys.argv[1]) as f:
    context = compute_text(f.read())

for filename in glob.glob(sys.argv[2], recursive=True):
    with open(filename) as fin, \
         open(path.join(sys.argv[3], filename), "w") as fout:
        print("processing {0}".format(filename))
        text = fin.read()
        fixed_text = replace_occurences(text, context)
        fout.write(fixed_text)
