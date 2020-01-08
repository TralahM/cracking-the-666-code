#!python
from argparse import ArgumentParser
import beast

if __name__ == '__main__':
    ps = ArgumentParser()
    ps.add_argument('word', help="Word to compute score", default="computer")
    args = ps.parse_args()
    print(beast.score_word(args.word))
