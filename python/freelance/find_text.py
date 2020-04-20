import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path')
parser.add_argument('-t', '--text')

args = parser.parse_args()
args = {key: value for key, value in vars(args).items() if value}
# print(args['path'])

text_to_find = args['text']

os.chdir(args[r'path'])
for root, dirs, files in os.walk('.', topdown=False):
    for name in files:
        filename, file_extension = os.path.splitext(os.path.join(root, name))
        if name.find(text_to_find) != - 1 and file_extension.find('txt') != -1:
            with open(os.path.join(root, name), 'r') as f:
                for line in f:
                    print(line)
