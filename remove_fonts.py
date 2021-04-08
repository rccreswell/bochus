
import argparse
import io
import re


def remove_fontspec(file):
    r"""Remove all instances of '\fontspec{...}' from the document.

    It overwrites the file.

    Parameters
    ----------
    file : str
        Path to tex file
    """
    with io.open(file, mode='r', encoding='utf-8') as f:
        lines = f.readlines()

    newlines = []
    for line in lines:
        newlines.append(re.sub('\\\\fontspec{(\w|\s|\d)+}', '', line))

    with io.open(file, mode='w', encoding='utf-8') as f:
        f.writelines(newlines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str)
    args = parser.parse_args()
    remove_fontspec(args.file)
